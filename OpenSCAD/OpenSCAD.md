# OpenSCAD
OpenSCAD, the software with the simplest language yet? Yes.
After downloading it at http://www.openscad.org/downloads.html, one can open a new file in OpenSCAD:
![interface](http://2.bp.blogspot.com/-V95eP3vKxZE/VBCFkK1V2QI/AAAAAAAACzU/C7lRiaDH1qo/s1600/mug_import.png)

The editor is together with the GUI. Once you save the file, the GUI will update automatically.
OpenSCAD has a simple script language. The full library documentation is here: https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/The_OpenSCAD_Language.

In addition, you can also use Python for OpenSCAD with "SolidPython". Full version of SolidPython documentation is here: http://solidpython.readthedocs.io/en/latest/ including installation guide. The simplicity of the script is preserved.

I have not continued using OpenSCAD because it can only export in 2D file formats or STL/OFF. When iputting STL file exported from OpenSCAD, one would receive a solid object with elements on it, no surfaces, like this:
![ex](https://github.com/miaonaise/ABB-Summer-2017/blob/master/OpenSCAD/failscad.PNG)

Using functions in ANSA to convert it into surfaces:
![exx](https://github.com/miaonaise/ABB-Summer-2017/blob/master/FreeCAD/ansa-scad.PNG)

No good. 
