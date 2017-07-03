# -*- coding: utf-8 -*-

# Macro Begin: C:\Users\XJULLI\Documents\MacroJuju\test.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++

import sys
sys.path.append("/Program Files/FreeCAD 0.16/bin")

import math
import FreeCAD
import Part
from FreeCAD import Base,Placement,Rotation

doc = App.newDocument("transformer")

# L,W,H defined along x,y,z axis respectively

# TANK
TL = 20; TW = 50; TH = 30 # tank dimension
tankSHP = Part.makeBox(TL,TW,TH)
doc.addObject("Part::Feature","tank")
doc.tank.Shape = tankSHP

# BUSHING
BA = 30  # angle between bushings in degrees
BR = 3   #radius
BH = 30 # height
BS = 10 # seperation distance between two bushings
BI = 3 # how far in bushing comes from the y-axis
BSIN = math.sin(math.radians(BA)) ; BCOS = math.cos(math.radians(BA))

midBushSHP = Part.makeCylinder(BR,BH,Base.Vector(BI+BR,TW/2,TH))
doc.addObject("Part::Feature","midBush")
doc.midBush.Shape = midBushSHP

leftCyl = Part.makeCylinder(BR,BH,Base.Vector(BI+BR,TW/2-10-BR*BCOS,TH-BR*BSIN),Base.Vector(0,-BSIN,BCOS))
leftBushSHP = leftCyl.cut(tankSHP)
doc.addObject("Part::Feature","leftBush")
doc.leftBush.Shape = leftBushSHP

rightCyl = Part.makeCylinder(BR,BH,Base.Vector(BI+BR,TW/2+10+BR*BCOS,TH-BR*BSIN),Base.Vector(0,BSIN,BCOS))
rightBushSHP = rightCyl.cut(tankSHP)
doc.addObject("Part::Feature","rightBush")
doc.rightBush.Shape = rightBushSHP

# RADIATOR
# symmetric at y = TW/2
RL = 12; RW = 25; RH = 15
RS = 3 # radiator's top is RD higher than tank's top
RX = TL; RY = (TW-RW)/2; RZ = TH-RH+RS
radiatorSHP = Part.makeBox(RL,RW,RH,Base.Vector(RX,RY,RZ))
doc.addObject("Part::Feature","radiator")
doc.radiator.Shape = radiatorSHP



__objs__=[]
__objs__.append(FreeCAD.getDocument("transformer").getObject("tank"))
__objs__.append(FreeCAD.getDocument("transformer").getObject("midBush"))
__objs__.append(FreeCAD.getDocument("transformer").getObject("leftBush"))
__objs__.append(FreeCAD.getDocument("transformer").getObject("rightBush"))
__objs__.append(FreeCAD.getDocument("transformer").getObject("radiator"))


Part.export(__objs__,"C:/Users/XJULLI/Documents/MacroJuju/shapefied.step")
