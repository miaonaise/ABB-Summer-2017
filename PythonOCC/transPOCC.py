
from OCC.gp import *
from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse 
from OCC.STEPControl import STEPControl_Writer, STEPControl_AsIs


# TANK
TL = 20; TW = 60; TH = 30
tank = BRepPrimAPI_MakeBox(TL, TW, TH).Shape()

# BUSHING
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

Btap = BRepPrimAPI_MakeCylinder(BOR,BTL)
p = gp_Ax2(gp_Pnt(0,0,BTL),gp_DZ()) # placement
Bcore = BRepPrimAPI_MakeCylinder(p,BCR,BCL)
p = gp_Ax2(gp_Pnt(0,0,BTL+BCL),gp_DZ()) # placement
Bhead = BRepPrimAPI_MakeCylinder(p,BOR,BHL)
bushing = BRepAlgoAPI_Fuse(Btap, Bcore).Shape()
bushing = BRepAlgoAPI_Fuse(bushig, Bhead).Shape()




# initialize the STEP exporter
step_writer = STEPControl_Writer()

# transfer shapes and write file
step_writer.Transfer(tank,STEPControl_AsIs)
step_writer.Transfer(cyl_s,STEPControl_AsIs)
step_writer.Write("test.stp")