# ABB-Summer-2017
Welcome to my repository. In this repository you will find the work I have completed during my 4 week summer job at ABB Corporate Research Center in Västerås, Sweden. 

## TASK DESCRIPTION
The aim is to produce a parametrized geometry in a script file by using Python API/modules provided by a free CAD software. The task was to research which softwares would be able to fulfill the aim and then compare and evaluate their API/modules.

## MY DOCUMENTATION
The softwares I have looked into are listed down below. Each software comes with a directory that contains a INFO.md file for a description of each file within the directory and a [SOFTWARENAME].md file which is the software's main documentation. 
- FreeCAD
- Onshape
- BRL-CAD
- OpenSCAD
- PythonOCC
- SALOME

In **FreeCAD.md**, **PythonOCC.md** and **SALOME.md**, you will find installation instructions, API documentation sources and how to run your python script.

In **Onshape.md**, **BRL-CAD.md** and **OpenSCAD.md**, you will find a description of the software and its limitations for achieving the aim.

Lastly, you will find evaluation and comparisons of softwares FreeCAD, PythonOCC and SALOME in the **Result.md** file in the ROOT directory.

**Extra Information:**
- All softwares investigated have Python API for scripting geometry. (i.e. technically speaking, they are all capable of fulfilling the aim.)
- I have achieved the aim with the following softwares: FreeCAD, PythonOCC and SALOME.
- The geometry produced by my FreeCAD script is currently closest to the ideal product.
- Only FreeCAD, PythonOCC and SALOME has python as its default scripting language. The others have a different default scripting language.
- FreeCAD, PythonOCC and SALOME are all based on the Open CASCADE library.
- ANSA supporter recommends not to import geometry in STL files in ANSA. 
- When importing STEP/IGES files into ANSA, change settings in ANSA for a better and a faster translator:
  - Settings>Translators>General and set the field for the translation of neutral files to CT.
  - Once you will use CT for the translation mind to de-activate the 'Heal Model' in case it is activated. 
  - 'Heal Model' field is under All format>Neutral files with CT>Topology.

##
Please contact me via e-mail (julia970906@gmail.com) if you have any suggestions on improving my documents.

I operate on Windows 10 Version 1703 (for SALOME: Ubuntu 16.04)
