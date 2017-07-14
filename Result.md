FreeCAD vs PythonOCC vs SALOME

_OpenCascade is a software development platform freely available in open source. It includes C++ components for 3D surface and solid modeling, visualization, data exchange and rapid application development. OpenCascade is extremely mature (20 years of development by experts), stable and complete. OpenCascade is written in C++, which is not the simplest of programming languages to use._

- PythonOCC aims to be a complete binding of OCC(Open CasCade) while FreeCAD does not and results into a much simpler code. 

FreeCAD
- object shape conversions for export + messy export
- not a complete API
- good examples for beginners
- python console in GUI
- can preview scripted geo in GUI without using gui functions

PythonOCC
- direct transfer shape and export
- complete API
- runs through anaconda prompt
- better complicated examples
- must add display functions for preview (not complicated I supposed)



 | FreeCAD | PythonOCC | SALOME
--- | --- | --- | ---
API Documentation | - Online - does not cover entire library.  | **nicely** | 23
1 | 2 | 3 | 234




I find working in all environments comfortable. I like how PythonOCC library totally corresponds to the OCCT library and its examples provided by Thomas Paviot. I can always use FreeCAD simple examples and find the same function in PythonOCC or vice versa. SALOME has a very nice documentation and a nice forum, however it is has the least convenient method for using the modules especially if one uses windows.
