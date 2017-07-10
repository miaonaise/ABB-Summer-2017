import sys
sys.path.append("/Program Files/FreeCAD 0.16/bin") 

import math
import FreeCAD
import Part
from FreeCAD import Base,Placement,Rotation

doc = App.newDocument("cooler")

#  L,W,H defined along x,y,z axis respectively

#  COOLER
CL = 100; CW = 260; CH = 20
coolerSHP = Part.makeBox(CL,CW,CH)

#  ADDING CHANNELS
n = input("number of channels: ")
length = input("lengths of channels: ")
sep = input("separation distance of channels from left to right of front face: ")

height = 10
bhd = 7 #  bottom height difference

decoy = 0
for i in range(0,n):
  channelSHP = Part.makeBox(length[i],CW,height,Base.Vector(decoy+sep[i],0,bhd))
  coolerSHP = coolerSHP.cut(channelSHP)
  decoy += length[i] + sep[i]
  
doc.addObject("Part::Feature","cooler")
doc.cooler.Shape = coolerSHP

__objs__=[]
__objs__.append(FreeCAD.getDocument("cooler").getObject("cooler"))

Part.export(__objs__,"C:/Users/XJULLI/Documents/MacroJuju/extra.step")
