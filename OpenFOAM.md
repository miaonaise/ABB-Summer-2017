#OpenFOAM
Video Tutorials:

https://www.youtube.com/watch?v=3iZfVmFkvB8&list=PLqxhJj6bcnY9RoIgzeF6xDh5L9bbeK3BL

https://www.youtube.com/watch?v=KznljrgWSvo

Tutorial Guide: http://www.openfoam.com/documentation/tutorial-guide/introduction.php

Windows Installation: https://openfoam.org/download/windows-10/

```
mkdir -p $FOAM_RUN
cp -r $FOAM_TUTORIALS $FOAM_RUN
```
#### 1.1 Getting started
- An OpenFOAM case requires definitions for the mesh, initial fields, physical models, control parameters, etc.
- OpenFOAM data is stored in a set of files within a case directory rather than in a single case file.
- The case directory is given a suitably descriptive name, under which the required information is located in the three directories:
  - constant
  - system, and
  - initial time directory, e.g.0.
