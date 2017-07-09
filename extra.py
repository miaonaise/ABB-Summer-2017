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
doc.addObject("Part::Feature","cooler")
doc.cooler.Shape = coolerSHP

#  CHANNELS
n = input("number of channels: ")
length = input("lengths of channels: ")
sep = input("separation distance of channels from left to right of front face: ")

height = 10
thd = CH - height - bhd #  top height difference
bhd = 7 #  bottom height difference

puppy = 0
for i in range(0,n):
  channelSHP = Part.makeBox(length[i],CW,height,Base.Vector(puppy+sep[i],0,bhd))
  
