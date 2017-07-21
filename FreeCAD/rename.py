## Edit STEPFILENAME
## names in namelist to be put in order of the item exporting
## Export default name begins with: "Open CASCADE STEP translator"
##      when translated into STEP file in FreeCAD, PythonOCC & Salome,
##      double check for confirmation.

namelist = ["tank",
            "center_bushing",
            "left_bushing",
            "right_bushing",
            "expansion_vessel",
            "radiator",
            "left_fan",
            "right_fan"]

searchfile = open("STEPFILENAME.step","r") # Open file
original = []
for line in searchfile:
    if "Open CASCADE STEP translator" in line:
        original.append(line)
searchfile.close() # Close file

for i in range(len(original)-2,-1,-2):
    original.pop(i)

init = len(original) - len(namelist)

replace = []
for x in range(len(namelist)):
    split = original[x+init].split("'")
    split[1] = namelist[x]
    join = "'".join(split)
    replace.append(join)


# Read in the file
with open('STEPFILENAME.step', 'r') as file :
  filedata = file.read()

# Replace the target string
for i in range(len(namelist)):
    filedata = filedata.replace(original[i+init], replace[i])

# Write the file out again
with open('STEPFILENAME.step', 'w') as file:
  file.write(filedata)
