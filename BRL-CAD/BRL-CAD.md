# BRL-CAD
After you have downloaded BRL-CAD at https://brlcad.org/, you begin drawing with MGED. 

Here's a picture of how the user interface looks like:
![hmmm](http://3.bp.blogspot.com/-AjkhD3HnpyA/UHUWFU0Ul6I/AAAAAAAAWdU/rLAyv7oA4ck/s1600/Screenshot.png)

You have your command window and a graphics window.
In the command window you create a data file and store objects in them. Objects are cretaed and modified using commands.
Here is the complete documentation to the script language: https://brlcad.org/w/images/c/cf/Introduction_to_MGED.pdf

The disadvantage of using BRL-CAD is that it does not have an editor. Objects are stored in the data file. When you save the data file and exit MGED and open the data file again, you will not see anything on the graphics window. You must enter a command to show them all. (https://sourceforge.net/p/brlcad/support-requests/112/#ab3f)

To script with Python, one must use "python-brlcad". _python-brlcad is an on-going effort to wrap BRL-CAD functionality with python code. The project is in its early development stage, the source code allows for now the scripting (read/modify/write) of only a selected set of primitives using libwdb._ (https://brlcad.org/w/index.php?title=Python_Geometry&oldid=6518).

Installing instructions and examples of python scripts using BRL-CAD can be found here: https://github.com/kanzure/python-brlcad

Reasons I did not continue with python-brlcad:
- I failed to install it on windows - failed to provide gcc during installation.
- It is not easy to test if the coding is right compared to FreeCAD
- FreeCAD's documentation is easier to use as it is not compiled into one big pdf file. 
