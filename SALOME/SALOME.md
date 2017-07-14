# SALOME
## Installation
I operate Ubuntu 16.04 here.
Download and Install Universal binaries for Linux: http://www.salome-platform.org/downloads/current-version
```
% chmod +x Salome-V8_2_0-univ_public.run
% Salome-V8_2_0-univ_public.run
```

To launch Salome, go to the Salome "appli" folder:
```cd salome\appli_V8_2_0```

Launch with interface:
```./salome```

Launch without interface:
```./salome -t```

Open salome shell:
```./salome shell```

For running your script, you want to launch without interface and then open the salome shell. 

## Sources
Latest updated documentation: http://www.salome-platform.org/user-section/documentation/current-release

For scripting 3D surface geometry go to Geometry Documentation - User Documentation

Geometry script examples path: salome/Salome-V8_2_0-univ/modules/GEOM_V8_2_0/bin/salome

My Simple Script Example:
```python
# Imports
from OCC.gp import * # module for defining placements, directions etc
from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox # make box function from BRepPrimAPI (module for primitive objects)
from OCC.STEPControl import STEPControl_Writer, STEPControl_AsIs # for exporting in STEP format

placement = gp_Pnt(2,0,0)
box = BRepPrimAPI_MakeBox(p, 10, 10, 10).Shape() # box with size 10x10x10 shifted two units up x-axis.

# initialize the STEP exporter
step_writer = STEPControl_Writer()

# transfer shapes and write file
step_writer.Transfer(box,STEPControl_AsIs)
step_writer.Write("final.stp")
```
