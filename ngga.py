# -*- coding: utf-8 -*-

# Macro Begin: C:\Users\XJULLI\Documents\MacroJuju\test.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++

import sys
sys.path.append("/Program Files/FreeCAD 0.16/bin")

import math
import FreeCAD
import Part
from FreeCAD import Base,Placement,Rotation
import FreeCADGui

doc = App.newDocument("transformer")

# TANK
TL = 20; TW = 50; TH = 30
doc.addObject("Part::Box","tank")
doc.tank.Length = TL
doc.tank.Width = TW
doc.tank.Height = TH

# BUSHING
BA = 30  # angle between bushings in degrees
BR = 3   #radius
BH = 30 # height
BS = 10 # seperation distance between two bushings
BI = 3 # how far in bushing comes from the y-axis
BSIN = math.sin(math.radians(BA)) ; BCOS = math.cos(math.radians(BA))

doc.addObject("Part::Cylinder","centerBush")
doc.centerBush.Radius = BR
doc.centerBush.Height = BH
doc.centerBush.Placement = Placement(Base.Vector(BI+BR,TW/2,TH),Rotation(0,0,0))

doc.addObject("Part::Cylinder","leftBush")
doc.leftBush.Radius = BR
doc.leftBush.Height = BH
doc.leftBush.Placement = Placement(Base.Vector(BI+BR,TW/2-10-BR*BCOS,TH-BR*BSIN),Rotation(0,0,BA))

doc.addObject("Part::Cylinder","rightBush")
doc.rightBush.Radius = BR
doc.rightBush.Height = BH
doc.rightBush.Placement = Placement(Base.Vector(BI+BR,TW/2+10+BR*BCOS,TH-BR*BSIN),Rotation(0,0,360-BA))

__objs__=[]
__objs__.append(FreeCAD.getDocument("transformer").getObject("tank"))
__objs__.append(FreeCAD.getDocument("transformer").getObject("rightBush"))
__objs__.append(FreeCAD.getDocument("transformer").getObject("centerBush"))
__objs__.append(FreeCAD.getDocument("transformer").getObject("leftBush"))

doc.recompute() 


Part.export(__objs__,"C:/Users/XJULLI/Documents/MacroJuju/test02.step")

del __objs__
