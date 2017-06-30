# ABB-Summer-2017
Welcome to my repository. In this repository you will find the work I have completed during my 4 week summer job at ABB Corporate Research Center in Västerås, Sweden. 

## TASK DESCRIPTION
The aim is to produce a geometry in a script file by using Python API/modules from a free CAD software. The task was to research which softwares would be able to fulfill the aim and then compare and evaluate their API/modules.
More details:
- Script language: Python 2.7
- Parameters of the geometry should be easily editable in a Python editor.
- The file format should be readable by ANSA (software used for mesh). 
- **Description of the types of geometry to be scripted**
- (Example) Edit python file (.py) - Run module - STEP file exported - open STEP file in ANSA - a geometry ready for mesh.

## HOW TO NAVIGATE THROUGH MY WORK
After you finish reading this document, please read the following documents in the given order:
1. FreeCAD
2. Onshape
3. BRL-CAD
4. OpenSCAD
5. PythonOCC/Open CasCade
These are the names of the free CAD softwares.

The best software for achieving the aim is FreeCAD. By reading about it first you will realize why the others are worse.
Things good to know before starting to read:
- All softwares in the list have Python API for scripting geometry. (i.e. technically speaking, they are all capable of fulfilling the aim. I have only achieved the aim with FreeCAD.)
- Only FreeCAD and PythonOCC has Python as its "main" scripting language. The others have their own scripting language linked to their GUI and require a Python wrapper library to sript the geometry in Python. (OBS! FreeCAD and PythonOCC are actually also wrapper libraries around Open CasCade (which is in C++).)
- Open CasCade is very powerful.

--The End--
