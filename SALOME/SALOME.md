# SALOME
## Installation
I operate Ubuntu 16.04 here.
Download and Install Universal binaries for Linux: http://www.salome-platform.org/downloads/current-version
```
% chmod +x Salome-V8_2_0-univ_public.run
% Salome-V8_2_0-univ_public.run
```

To launch Salome, go to the Salome "appli" folder:
```cd salome\appli_V8_2_0```

Launch with interface:
```./salome```

Launch without interface:
```./salome -t```

Open salome shell:
```./salome shell```

For running your script, you want to launch without interface and then open the salome shell. 

## Sources
Latest updated documentation: http://www.salome-platform.org/user-section/documentation/current-release

For scripting 3D surface geometry go to Geometry Documentation - User Documentation

Path for geometry script examples in your downloaded package: salome/Salome-V8_2_0-univ/modules/GEOM_V8_2_0/bin/salome

My Personal Script Template:
```python
# Imports
import salome
salome.salome_init()

import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New(salome.myStudy)

import tempfile, os # for exporting

# Making Box
box = geompy.MakeBoxDXDYDZ(10,10,10)

# Export
geompy.Export( geom, "/tmp/myBox.step", "STEP")
```
It is currently exported in /tmp directory in the computer. I do not know how to modify export destination.

## Further things to look into for transformerSALOME.py
- I have not removed the shared face of the tank and the bushings from both parts.
- **Modifying export destination** - the script currently exports the geometry into a tmp directory. Have not found out how to modify the destination of export.
