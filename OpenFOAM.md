#OpenFOAM
Video Tutorials:

- https://www.youtube.com/watch?v=3iZfVmFkvB8&list=PLqxhJj6bcnY9RoIgzeF6xDh5L9bbeK3BL

- https://www.youtube.com/watch?v=KznljrgWSvo

Tutorial Guide: http://www.openfoam.com/documentation/tutorial-guide/introduction.php

Windows Installation: https://openfoam.org/download/windows-10/

http://www.openfoam.com/documentation/tutorial-guide/tutorialse2.php#x6-60002.1
https://cfd.direct/openfoam/user-guide/dambreak/

```
mkdir -p $FOAM_RUN
cp -r $FOAM_TUTORIALS $FOAM_RUN
```
### 1.1 Getting started
- An OpenFOAM case requires definitions for the mesh, initial fields, physical models, control parameters, etc.
- OpenFOAM data is stored in a set of files within a case directory rather than in a single case file.
- The case directory is given a suitably descriptive name, under which the required information is located in the three directories:
  - constant
  - system, and
  - initial time directory, e.g.0.

### 2.1 Lid-driven cavity flow
#### 2.1.1 Pre-processing
    cd $FOAM_RUN/tutorials/incompressible/icoFoam/cavity/cavity
- OpenFOAM solves the case in 3 dimensions by default but can be instructed to solve in 2 dimensions by specifying a ‘special’ empty boundary condition on boundaries normal to the (3rd) dimension for which no solution is required. Here, the mesh must be 1 cell layer thick, and the empty patches planar. 
