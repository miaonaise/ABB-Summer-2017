# PythonOCC
## Support
https://groups.google.com/forum/#!forum/pythonocc

## Installation
PythonOCC:
  - Precompiled version
      - Install miniconda - https://conda.io/miniconda.html
      - Run in Anaconda prompt: conda install -c conda-forge -c dlr-sc -c pythonocc -c oce pythonocc-core==0.18 python=***2 OR 3***
      - Usage: (in anaconda prompt, navigate to file directory and run "python docname.py")
  - Compile yourself: https://github.com/tpaviot/pythonocc-core/blob/master/INSTALL.md
 
## Creating script
API Documentation: https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/

Since PythonOCC is based on Open CASCADE Technology (OCCT) modules, one can refer moduels to their documentation which explains the modules in more detail: https://www.opencascade.com/doc/occt-6.9.1/refman/html/index.html

OCCT tutorial (learn how to use some modules): https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt__tutorial.html

PythonOCC Script examples: https://github.com/tpaviot/pythonocc-core/tree/master/examples

Modules I have used for my geometry:
- [BRepPrimAPI](https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/OCC.BRepPrimAPI.html#module-OCC.BRepPrimAPI) For creating primitive surface geometry
- [BRepAlgoAPI](https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/OCC.BRepAlgoAPI.html#module-OCC.BRepAlgoAPI) For booleon operations on the surface geometry
- [BRepBuilderAPI](https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/OCC.BRepBuilderAPI.html#module-OCC.BRepBuilderAPI) For creating edges, wires, faces etc. and transforming shapes
- [gp](https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/OCC.gp.html) For defining placement
- [STEPControl](https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/OCC.STEPControl.html#module-OCC.STEPControl) For exporting into STEP files

My Personal Script Template:
```python
# Imports
from OCC.gp import * # module for defining placements, directions etc
from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox # make box function from BRepPrimAPI (module for primitive objects)
from OCC.STEPControl import STEPControl_Writer, STEPControl_AsIs # for exporting in STEP format

placement = gp_Pnt(2,0,0)
box = BRepPrimAPI_MakeBox(placement, 10, 10, 10).Shape() # box with size 10x10x10 shifted two units up x-axis.

# initialize the STEP exporter
step_writer = STEPControl_Writer()

# transfer shapes and write file
step_writer.Transfer(box,STEPControl_AsIs)
step_writer.Write("final.stp")
```

Additional links/examples (very optional):

https://www.opencascade.com/content/difference-between-brepalgo-and-brepalgoapi

https://github.com/tpaviot/pythonocc-core/blob/master/examples/core_export_step_ap203.py

http://www.geocities.jp/penguinitis2002/study/OpenFOAM/pythonOCC/pythonOCC.html

https://github.com/tpaviot/pythonocc-core/blob/master/examples/core_topology_boolean.py

https://www.opencascade.com/content/how-add-names-step-or-iges-file

https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/OCC.STEPCAFControl.html#module-OCC.STEPCAFControl

## Further things to look into for transformerPyOCC.py
- **STEPCAFControl** - This module should give you the capability of writing names on your objects when being trasnferred to a STEP entity ([source](https://www.opencascade.com/content/how-add-names-step-or-iges-file)). In the CAFtestPyOCC.py you will find the attempt on applying this module based on this [example](https://github.com/tpaviot/pythonocc-core/blob/master/examples/core_load_step_ap203_ocaf.py).
- **Cutting common surface of parts** - In this script, the overlapping surface from the bushings and the tank is still there. This should be removed for the purpose of future use. The process should go as to first finding the surface they have in common and then cut it off from both of the parts. I have attempted to turn them into shells and find the common part and then use cut. In temp.py, I am attempting to use the BRepAlgoAPI_Section which outputs a compound of edges when the input is of two solids have interfering faces.

