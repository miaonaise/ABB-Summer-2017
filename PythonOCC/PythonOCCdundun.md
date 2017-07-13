## Support
https://groups.google.com/forum/#!forum/pythonocc

## Installation
PythonOCC:
  - Precompiled version
      - Miniconda - https://conda.io/miniconda.html
      - Run in Anaconda prompt: conda install -c conda-forge -c dlr-sc -c pythonocc -c oce pythonocc-core==0.18 python=***2 OR 3***
      - Usage: (in anaconda prompt, navigate to file directory and run "python docname.py")
  - Compile yourself: https://github.com/tpaviot/pythonocc-core/blob/master/INSTALL.md
 
## Creating script
API Documentation: https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/

Since PythonOCC is based on Open CASCADE Technology modules, one can read their documentation which explains the modules in more detail: https://www.opencascade.com/doc/occt-6.9.1/refman/html/index.html

Script examples: https://github.com/tpaviot/pythonocc-core/tree/master/examples


Modules I have used for my geometry:
- [BRepPrimAPI](https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/OCC.BRepPrimAPI.html#module-OCC.BRepPrimAPI) For creating primitive surface geometry
- [BRepAlgoAPI](https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/OCC.BRepAlgoAPI.html#module-OCC.BRepAlgoAPI) For booleon operations on the surface geometry
- [gp](https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/OCC.gp.html) For defining placement
- [STEPControl](https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/OCC.STEPControl.html#module-OCC.STEPControl) For exporting into STEP files


Additional links:

https://www.opencascade.com/content/difference-between-brepalgo-and-brepalgoapi

export sample: https://github.com/tpaviot/pythonocc-core/blob/master/examples/core_export_step_ap203.py

http://www.geocities.jp/penguinitis2002/study/OpenFOAM/pythonOCC/pythonOCC.html

https://github.com/tpaviot/pythonocc-core/blob/master/examples/core_topology_boolean.py
