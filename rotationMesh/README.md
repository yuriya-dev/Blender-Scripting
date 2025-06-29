# Add frame/5 (or -frame/5) expression to Rotation Z

- Open Blender scripting and then paste the code
- click alt + P to run the script

```
import bpy

# Daftar nama objek roda
roda_list = ["Mesh_Name", "Mesh_Name"]

for name in roda_list:
    obj = bpy.data.objects.get(name)
    if obj:
        # Tambah driver ke rotasi Y (sumbu 1)
        fcurve = obj.driver_add("rotation_euler", 1)

        # Ambil driver
        driver = fcurve.driver
        driver.type = 'SCRIPTED'

        # Hapus variabel lama
        while driver.variables:
            driver.variables.remove(driver.variables[0])

        # Ekspresi putar
        driver.expression = "-frame / 5"
    else:
        print(f"Objek '{name}' tidak ditemukan")
```
