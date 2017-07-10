
from OCC.gp import *
from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder

from OCC.STEPControl import STEPControl_Writer, STEPControl_AsIs


# creates a basic shape
box_s = BRepPrimAPI_MakeBox(10, 20, 30).Shape()
p = gp_Ax2(gp_Pnt(0,0,30),gp_DZ())
cyl_s = BRepPrimAPI_MakeCylinder(p,2,50).Shape()

# initialize the STEP exporter
step_writer = STEPControl_Writer()

# transfer shapes and write file
step_writer.Transfer(box_s,STEPControl_AsIs)
step_writer.Transfer(cyl_s,STEPControl_AsIs)
step_writer.Write("test.stp")
