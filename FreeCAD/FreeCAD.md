# FreeCAD

## Installation
Install Python 2.7: https://www.python.org/downloads/release/python-2713/

Install FreeCAD: https://www.freecadweb.org/wiki/Download

During installation, select the option Add PythonPATH.

Make sure the FreeCAD version and the Python version are compatible, i.e. both should be 64 bit version or 32 bit.

Once you are ready, you can open your FreeCAD application and change some settings:
- [Swedish to English] Redigera > Alternativ... > Allmänt > Allmänt > _Välj ditt språk under_ Språk > Verkställ > OK
- Edit > Preferences > General > Editor > _Select_ Insert spaces _under_ Indentation > Apply > OK
- Edit > Preferences > General > Output Window > _Select both boxes under_ Python interpreter > Apply > OK
- View > Panels > Report view
- View > Panels > Python console

Whatever you do in the GUI it will output as a python command in the python console.
## Scripting
Begin with studying a simple script of box. This script includes the essential code you need in order to run it in the command prompt.
```python
import sys #  Helping the computer finding the FreeCAD modules
sys.path.append("/Program Files/FreeCAD 0.16/bin")

import FreeCAD
import Part  #  Esssential modules

doc = App.newDocument("docName") #  Creating new document

boxShape = Part.makeBox(2,4,3) #  Creating a shape with Part
doc.addObject("Part::Feature","myBox") #  myBox is the object name
doc.myBox.Shape = boxShape

doc.recompute()

__objs__=[] #  List for all objects to be exported
__objs__.append(FreeCAD.getDocument("docName").getObject("myBox"))

Part.export(__objs__, "C:/Users/XJULLI/Desktop/testBox.step") # exporting into a step file
```
**Alternative export method**
```
# create a compound shape and export one object instead
# this method doesn't require you to convert every shape to an independent object

box = Part.makeBox(10,10,10)
cyl = Part.makeCylinder(2,10)
compSHP = Part.makeCompound([box,cyl]) # make compound

doc.addObject("Part::Feature","comp")
doc.comp.Shape = compSHP

# export
Part.export([FreeCAD.getDocument("docName").getObject("comp")], "C:/Users/XJULLI/Desktop/testComp.step")
```
Scripts can also be run within the FreeCAD application by opening the python file in FreeCAD. 

Script Tutorial: https://www.freecadweb.org/wiki/Topological_data_scripting

Part API: https://www.freecadweb.org/wiki/Part_API

Object API: https://www.freecadweb.org/wiki/Object_API

These tools have helped me to achieve the aim.

## Import Results Sample

**STL**
- Only elements are imported
![stl](https://github.com/miaonaise/ABB-Summer-2017/blob/master/FreeCAD/ansa-stl.PNG)

**STEP/IGES**
- Change settings in ANSA: Settings>Translators>General and set the field for the translation of neutral files to CT. Once you will use CT for the translation mind to de-activate the 'Heal Model' in case it is activated. 'Heal Model' field is under All format>Neutral files with CT>Topology.
![geo](https://github.com/miaonaise/ABB-Summer-2017/blob/master/FreeCAD/ansa-step.PNG)

