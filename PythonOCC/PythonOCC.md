# PythonOCC
We begin with OPEN CASCADE. 

_OpenCascade is a software development platform freely available in open source. It includes C++ components for 3D surface and solid modeling, visualization, data exchange and rapid application development. OpenCascade is extremely mature (20 years of development by experts), stable and complete. OpenCascade is written in C++, which is not the simplest of programming languages to use … PythonOCC makes it much easier to use OpenCascade functionalities by providing Python functions and objects that mimick the C++ implementation of OpenCascade. Technically speaking, PythonOCC is a Python wrapper library around OpenCascade. (https://pythonocc.wordpress.com/2013/02/25/getting-started-installing-on-windows/)_

Here is introduction and installation instructions for PythonOCC: https://github.com/tpaviot/pythonocc-core. In this repository you can also find examples.
Some examples here too: http://www.pythonocc.org/category/quick-examples/ where I find example "Hello dumb box!" most helpful yet.
And the important pythonocc API documentation: https://cdn.rawgit.com/tpaviot/pythonocc-core/3ceb6b92/doc/apidoc/0.17.3/

I failed to install pythonocc, but I receive help fast from their mailing list: https://groups.google.com/forum/#!topic/pythonocc/iG360xpSsiE. I will re-try to install if needed.

Things that put me off from trying:
- As seen in the examples, the coding language is more complicated than FreeCAD
- Difficult to understand the pythonocc API documentation
- Familiarity with FreeCAD

Note(!):
_PythonOCC is a pretty young and active project that aims at binding the whole range of OpenCasCADe functions into a python module. This is a very different approach than FreeCAD, where only certain components of OpenCasCade are used, resulting in a much simpler structure. PythonOCC, on the other hand, since it provides you access to all of OCC classes and functions, is very complex, but also very powerful. It is therefore a very fine addition to FreeCAD. When you are limited by FreeCAD's available OCC functionality in your python scripts, it's time to load pythonOCC. (https://www.freecadweb.org/wiki/PythonOCC)_

Repeat: PythonOCC aims to be a complete binding of OCC(Open CasCade) while FreeCAD does not and results into a much simpler code. 

Some additional short comments on PythonOCC vs FreeCAD:
- https://forum.freecadweb.org/viewtopic.php?t=4028
- https://stackoverflow.com/questions/14519057/python-module-for-parametric-cad
- https://forum.freecadweb.org/viewtopic.php?t=5113&start=10

This also leads to the last things where FreeCAD is better than pythonOCC, with the python console in FreeCADgui, it is much easier to learn how to use the code.
