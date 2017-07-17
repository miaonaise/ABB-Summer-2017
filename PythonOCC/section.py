from OCC.gp import *
from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeCone
from OCC.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse, BRepAlgoAPI_Common, BRepAlgoAPI_Section
from OCC.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.BRepBuilderAPI import BRepBuilderAPI_Transform, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeFace
import math


# TANK
TL = 20; TW = 60; TH = 30
tank = BRepPrimAPI_MakeBox(TL, TW, TH).Shape()


# BUSHING
BA = 20  # angle between bushings in degrees
BS = 10 # seperation distance between two bushings
BIn = 3 # how far in bushing comes from the y-axis

BH = 40 # bush height/total length
BHL = 4 # head length
BTL = 5 # tap length
BCL = BH-BHL-BTL # core length
BOR = 3 # outer radius
BCR = 2.7 # core radius

BIRSm = 3.5 # radius of small CI
BIHSm = 0.5 # height of small CI
BIRLg = 4 # radius of large CI
BIHLg = float(BIRLg*BIHSm)/BIRSm # height of large CI (proportional)
BIS = 0.5 # seperation between CIs

BIHPack = BIHSm+BIHLg+2*BIS # pack length
BIno = int(BCL//BIHPack) # number of packs fitted into core length
BIrem = BCL % BIHPack # remainder length

# building a bushing shape
Btap = BRepPrimAPI_MakeCylinder(BOR,BTL).Shape()
p = gp_Ax2(gp_Pnt(0,0,BTL),gp_DZ()) # placement
Bcore = BRepPrimAPI_MakeCylinder(p,BCR,BCL).Shape()
p = gp_Ax2(gp_Pnt(0,0,BTL+BCL),gp_DZ()) # placement
Bhead = BRepPrimAPI_MakeCylinder(p,BOR,BHL).Shape()
bushing = BRepAlgoAPI_Fuse(Btap, Bcore).Shape()
bushing = BRepAlgoAPI_Fuse(bushing, Bhead).Shape()

BIinit = BTL+float(BIrem)/2+BIS # initial height for first cone
for i in range(0,BIno):
	Bconez = BIinit + i*BIHPack # local height for cones
  	p = gp_Ax2(gp_Pnt(0,0,Bconez),gp_DZ()) # placement
	BconeLg = BRepPrimAPI_MakeCone(p,BIRLg,BCR,BIHLg).Shape()
  	bushing = BRepAlgoAPI_Fuse(bushing, BconeLg).Shape()
  	p = gp_Ax2(gp_Pnt(0,0,Bconez+BIHLg+BIS),gp_DZ()) # placement
	BconeSm = BRepPrimAPI_MakeCone(p,BIRSm,BCR,BIHSm).Shape()
	bushing = BRepAlgoAPI_Fuse(bushing, BconeSm).Shape()

BSIN = BOR*math.sin(math.radians(BA)) ; BCOS = BOR*math.cos(math.radians(BA))

ltrsf = gp_Trsf() # create and set up transformation for leftBush
ltrsf.SetRotation(gp_Ax1(gp_Pnt(0,0,0),gp_Dir(1,0,0)),math.radians(BA))
leftBush = BRepBuilderAPI_Transform(bushing, ltrsf).Shape()
ltrsf.SetTranslation(gp_Vec(BIn+BOR,float(TW)/2-BS-BCOS,TH-BSIN))
leftBush = BRepBuilderAPI_Transform(leftBush, ltrsf).Shape()
leftBush = BRepAlgoAPI_Cut(leftBush,tank).Shape() # cut common part of bushing and tank

meh = BRepAlgoAPI_Section(leftBush,tank).Shape()
leftBush = BRepAlgoAPI_Cut(leftBush,hoho).Shape()

mtrsf = gp_Trsf() # create and set up transformation for midBush
mtrsf.SetTranslation(gp_Vec(BIn+BOR,float(TW)/2,TH))
midBush = BRepBuilderAPI_Transform(bushing, mtrsf).Shape()
common = BRepAlgoAPI_Common(midBush,tank).Shape()


rtrsf = gp_Trsf() # create and set up transformation for rightBush
rtrsf.SetRotation(gp_Ax1(gp_Pnt(0,0,0),gp_Dir(1,0,0)),math.radians(360-BA))
rightBush = BRepBuilderAPI_Transform(bushing, rtrsf).Shape()
rtrsf.SetTranslation(gp_Vec(BIn+BOR,float(TW)/2+BS+BCOS,TH-BSIN))
rightBush = BRepBuilderAPI_Transform(rightBush, rtrsf).Shape()
rightBush = BRepAlgoAPI_Cut(rightBush,tank).Shape() # cut common part of bushing and tank


# EXPANSION VESSEL
EL = 30 # length
ER = 5 # radius
ESX = 8 # how much it pops out relative to tank (along x-axis)
ESY = 4 # sep along y-axis
ESZ = 7 # sep along z-axis
EX = TL-(EL-ESX); EY = -(ESY+ER); EZ = TH+ESZ+ER
p = gp_Ax2(gp_Pnt(EX,EY,EZ),gp_DX()) # placement
expVessel = BRepPrimAPI_MakeCylinder(p,ER,EL).Shape()


# RADIATOR
# symmetric at y = TW/2
RL = 12; RW = 25; RH = 15
RS = 0 # radiator's top is RD higher than tank's top
RX = TL; RY = float(TW-RW)/2; RZ = TH-RH+RS
p = gp_Pnt(RX,RY,RZ)
radiator = BRepPrimAPI_MakeBox(p,RL,RW,RH).Shape()


# FANS on radiator
FR = 3 # radius
FD = 2 # depth
FS = 2 # fan's distance from radiator's bottom
FX = float(RL)/2+RX; FYleft = RY; FYright = RY+RW; FZ = RZ+FS+FR
p = gp_Ax2(gp_Pnt(FX,FYleft,FZ),-gp_DY())
leftFan = BRepPrimAPI_MakeCylinder(p,FR,FD).Shape()
p = gp_Ax2(gp_Pnt(FX,FYright,FZ),gp_DY())
rightFan = BRepPrimAPI_MakeCylinder(p,FR,FD).Shape()


# initialize the STEP exporter
step_writer = STEPControl_Writer()

# transfer shapes and write file
step_writer.Transfer(tank,STEPControl_AsIs)
step_writer.Transfer(leftBush,STEPControl_AsIs)
step_writer.Transfer(midBush,STEPControl_AsIs)
step_writer.Transfer(rightBush,STEPControl_AsIs)
step_writer.Transfer(expVessel,STEPControl_AsIs)
step_writer.Transfer(radiator,STEPControl_AsIs)
step_writer.Transfer(leftFan,STEPControl_AsIs)
step_writer.Transfer(rightFan,STEPControl_AsIs)
step_writer.Write("section.stp")
