import salome
salome.salome_init()

import math
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New(salome.myStudy)

import tempfile, os
# TANK
TL = 20; TW = 60; TH = 30 # size dimension
tank = geompy.MakeBoxDXDYDZ(TL,TW,TH)


# BUSHING
# variables
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

# build bushing shape
Btap = geompy.MakeCylinderRH(BOR,BTL)
Bcore = geompy.MakeCylinderRH(BCR,BCL)
Bcore = geompy.MakeTranslation(Bcore, 0, 0, BTL)
Bhead = geompy.MakeCylinderRH(BOR,BHL)
Bhead = geompy.MakeTranslation(Bhead, 0, 0, BTL+BCL)
bushing = geompy.MakeFuseList([Btap,Bcore,Bhead])

# adding composite insulators to shape
BIinit = BTL+float(BIrem)/2+BIS # initial height for first cone
for i in range(0,BIno):
	Bconez = BIinit + i*BIHPack # local height for cones
	BconeLg = geompy.MakeConeR1R2H(BIRLg,BCR,BIHLg)
	BconeLg = geompy.MakeTranslation(BconeLg, 0, 0, Bconez)
	BconeSm = geompy.MakeConeR1R2H(BIRSm,BCR,BIHSm)
	BconeSm = geompy.MakeTranslation(BconeSm, 0, 0, Bconez+BIHLg+BIS)
	bushing = geompy.MakeFuseList([bushing,BconeLg,BconeSm])

BSIN = BOR*math.sin(math.radians(BA)) ; BCOS = BOR*math.cos(math.radians(BA))

# create unit vector along x-axis
p1 = geompy.MakeVertex(0,0,0); p2 = geompy.MakeVertex(1,0,0)
v = geompy.MakeVector(p1,p2)

# create left bushing
leftBush = geompy.MakeRotation(bushing, v, math.radians(BA))
leftBush = geompy.MakeTranslation(leftBush, BIn+BOR, float(TW)/2-BS-BCOS, TH-BSIN)
leftBush = geompy.MakeCut(leftBush,tank)

# create middle bushing
midBush = geompy.MakeTranslation(bushing, BIn+BOR, float(TW)/2, TH)

# create right bushing
rightBush = geompy.MakeRotation(bushing, v, math.radians(360-BA))
rightBush = geompy.MakeTranslation(rightBush, BIn+BOR, float(TW)/2+BS+BCOS, TH-BSIN)
rightBush = geompy.MakeCut(rightBush,tank)


# EXPANSION VESSEL
EL = 30 # length
ER = 5  # radius
ESX = 8 # how much it pops out relative to tank (along x-axis)
ESY = 4 # sep along y-axis
ESZ = 7 # sep along z-axis
EX = TL-(EL-ESX); EY = -(ESY+ER); EZ = TH+ESZ+ER
p1 = geompy.MakeVertex(EX,EY,EZ)
p2 = geompy.MakeVertex(EX+EL,EY,EZ)
v = geompy.MakeVector(p1,p2)
expVessel = geompy.MakeCylinder(p1,v,ER,EL)


# RADIATOR
# symmetric at y = TW/2
RL = 12; RW = 25; RH = 15 # size dimension
RS = 0                    # radiator's top is RD higher than tank's top
Rgap = 1                  # gap between radiator and tank
RX = TL+Rgap; RY = float(TW-RW)/2; RZ = TH-RH+RS
radiator = geompy.MakeBoxDXDYDZ(RL,RW,RH)
radiator = geompy.MakeTranslation(radiator,RX,RY,RZ)


# FANS on radiator
FR = 3 # radius
FD = 2 # depth
FS = 2 # fan's distance from radiator's bottom
FX = float(RL)/2+RX; FYleft = RY; FYright = RY+RW; FZ = RZ+FS+FR

p1 = geompy.MakeVertex(FX,FYleft,FZ)
p2 = geompy.MakeVertex(FX,FYleft-FD,FZ)
v = geompy.MakeVector(p1,p2)
leftFan = geompy.MakeCylinder(p1,v,FR,FD)

p1 = geompy.MakeVertex(FX,FYright,FZ)
p2 = geompy.MakeVertex(FX,FYright+FD,FZ)
v = geompy.MakeVector(p1,p2)
rightFan = geompy.MakeCylinder(p1,v,FR,FD)

# exporting
multiple_geometry_list = [tank, leftBush, midBush, rightBush, expVessel, radiator, leftFan, rightFan]

geom = geompy.MakeCompound(multiple_geometry_list)
geompy.Export( geom, "/tmp/transformerSALOME.step", "STEP")



