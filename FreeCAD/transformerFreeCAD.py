import sys
sys.path.append("/Program Files/FreeCAD 0.16/bin") # for the system to find the FreeCAD modules

import math
import FreeCAD
import Part
from FreeCAD import Base,Placement,Rotation

doc = App.newDocument("transformer")

# L,W,H defined along x,y,z axis respectively

# TANK AND BUSHING

# tank initial shape
TL = 20; TW = 60; TH = 30 # size dimension
tankSHP = Part.makeBox(TL,TW,TH)

# bushing variables
BA = 20 # angle between bushings in degrees
BS = 10 # seperation distance between two bushings
BIn = 3 # how far in bushing comes from the y-axis

BH = 40          # bush height/total length
BHL = 4          # head length
BTL = 5          # tap length
BCL = BH-BHL-BTL # core length
BOR = 3          # outer radius
BCR = 2.7        # core radius

BIRSm = 3.5                      # radius of small CI
BIHSm = 0.5                      # height of small CI
BIRLg = 4                        # radius of large CI
BIHLg = float(BIRLg*BIHSm)/BIRSm # height of large CI (proportional)
BIS = 0.5                        # seperation between CIs

BIHPack = BIHSm+BIHLg+2*BIS # pack length
BIno = int(BCL//BIHPack)    # number of packs fitted into core length
BIrem = BCL % BIHPack       # remainder length

# building bushing shapes
Btap = Part.makeCylinder(BOR,BTL)
Bcore = Part.makeCylinder(BCR,BCL,Base.Vector(0,0,BTL))
Bhead = Part.makeCylinder(BOR,BHL,Base.Vector(0,0,BTL+BCL))
midBushSHP = Btap.fuse(Bcore).fuse(Bhead)
leftBushSHP = Btap.fuse(Bcore).fuse(Bhead)
rightBushSHP = Btap.fuse(Bcore).fuse(Bhead)

# adding composite insulators to bushing shape
BIinit = BTL+float(BIrem)/2+BIS # initial height for first cone
for i in range(0,BIno):
	Bconez = BIinit + i*BIHPack	
	BconeLg = Part.makeCone(BIRLg,BCR,BIHLg,Base.Vector(0,0,Bconez))
	BconeSm = Part.makeCone(BIRSm,BCR,BIHSm,Base.Vector(0,0,Bconez+BIHLg+BIS))
	midBushSHP = midBushSHP.fuse(BconeLg).fuse(BconeSm)
	leftBushSHP = leftBushSHP.fuse(BconeLg).fuse(BconeSm)
	rightBushSHP = rightBushSHP.fuse(BconeLg).fuse(BconeSm)

# creating tank and bushing shapes
BSIN = BOR*math.sin(math.radians(BA)) ; BCOS = BOR*math.cos(math.radians(BA))

midBushSHP.translate(Base.Vector(BIn+BOR,float(TW)/2,TH))
midBushSHP = midBushSHP.Shells[0] # convert to shell to cut off face
midcommon = midBushSHP.common(tankSHP)
midBushSHP = midBushSHP.cut(midcommon)

leftBushSHP.rotate(Base.Vector(0,0,0),Base.Vector(1,0,0),BA)
leftBushSHP.translate(Base.Vector(BIn+BOR,float(TW)/2-BS-BCOS,TH-BSIN))
leftBushSHP = leftBushSHP.cut(tankSHP)
leftBushSHP = leftBushSHP.Shells[0] # convert to shell to cut off face
leftcommon = leftBushSHP.common(tankSHP)
leftBushSHP = leftBushSHP.cut(leftcommon)

rightBushSHP.rotate(Base.Vector(0,0,0),Base.Vector(1,0,0),360-BA)
rightBushSHP.translate(Base.Vector(BIn+BOR,float(TW)/2+BS+BCOS,TH-BSIN))
rightBushSHP = rightBushSHP.cut(tankSHP)
rightBushSHP = rightBushSHP.Shells[0] # convert to shell to cut off face
rightcommon = rightBushSHP.common(tankSHP)
rightBushSHP = rightBushSHP.cut(rightcommon)

tankSHP = tankSHP.Shells[0] # convert to shell to cut off faces
tankSHP = tankSHP.cut(midcommon)
tankSHP = tankSHP.cut(leftcommon)
tankSHP = tankSHP.cut(rightcommon)


# EXPANSION VESSEL
EL = 30 # length
ER = 5  # radius
ESX = 8 # pop out length alonng x-axis
ESY = 4 # sep along y-axis
ESZ = 7 # sep along z-axis
EX = TL-(EL-ESX); EY = -(ESY+ER); EZ = TH+ESZ+ER
expVesselSHP = Part.makeCylinder(ER,EL,Base.Vector(EX,EY,EZ),Base.Vector(1,0,0))


# RADIATOR
# symmetric at y = TW/2
RL=12; RW=25; RH=15 # size dimension
RS = 0              # radiator's top is RD higher than tank's top
Rgap = 1            # gap between radiator and tank
RX = TL+Rgap; RY = float(TW-RW)/2; RZ = TH-RH+RS
radiatorSHP = Part.makeBox(RL,RW,RH,Base.Vector(RX,RY,RZ))


# FANS on radiator
FR = 3 # radius
FD = 2 # depth
FS = 2 # fan's distance from radiator's bottom
FX = float(RL)/2+RX; FYleft = RY; FYright = RY+RW; FZ = RZ+FS+FR
leftFanSHP = Part.makeCylinder(FR,FD,Base.Vector(FX,FYleft,FZ),Base.Vector(0,-1,0))
rightFanSHP = Part.makeCylinder(FR,FD,Base.Vector(FX,FYright,FZ),Base.Vector(0,1,0))


# Exporting
compSHP = Part.makeCompound([tankSHP,midBushSHP,leftBushSHP,rightBushSHP,expVesselSHP,radiatorSHP,leftFanSHP,rightFanSHP])
doc.addObject("Part::Feature","comp")
doc.comp.Shape = compSHP

# filetypes: step, iges, stl
Part.export([FreeCAD.getDocument("transformer").getObject("comp")],"tester.step")
