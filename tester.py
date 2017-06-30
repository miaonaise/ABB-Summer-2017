# -*- coding: utf-8 -*-

# Macro Begin: C:\Users\XJULLI\Documents\MacroJuju\test.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++

import sys
sys.path.append("/Program Files/FreeCAD 0.16/bin")

import math
import FreeCAD
import Part
from FreeCAD import Base,Placement,Rotation

doc = App.newDocument("transformer")


cyl = Part.makeCylinder(1,10)

Part.show(cyl)


doc.recompute() 

