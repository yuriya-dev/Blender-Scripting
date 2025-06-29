# Infinite Rotate Animation in Blender
This script adds an infinite rotation animation to objects by applying a driver to the X/Y/Z-axis rotation using the expression -frame (clockwise) / 5 and frame/5 (counterclockwise)

How to Use
Open the Scripting tab in Blender.
- Replace "Mesh_Name" in the script with the actual names of your objects.
- Paste the script into the text editor.
- Press Alt + P to run the script

# Script
```
import bpy

# List of object names to rotate
nesh_list = ["Mesh_Name", "Mesh_Name"]

for name in mesh_list:
    obj = bpy.data.objects.get(name)
    if obj:
        # Add driver to Y-axis rotation (index 1) or X-axis rotation (index 0) or Z-axis rotation (index 3)
        fcurve = obj.driver_add("rotation_euler", 1) # (0/1/2)

         # Get the driver
        driver = fcurve.driver
        driver.type = 'SCRIPTED'

        # Remove existing variables
        while driver.variables:
            driver.variables.remove(driver.variables[0])

        # Set driver expression "-frame / 5" or "frame / 5"
        driver.expression = "-frame / 5" # 
    else:
        print(f"Objek '{name}' not found.")
```
