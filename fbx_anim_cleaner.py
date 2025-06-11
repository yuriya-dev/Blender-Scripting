import bpy
import sys
import os

# Ambil argumen CLI
argv = sys.argv
argv = argv[argv.index("--") + 1:]

input_folder = argv[0]
output_folder = argv[1]

# Buat output folder jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Bersihkan scene sebelum mulai
bpy.ops.wm.read_factory_settings(use_empty=True)

# Loop semua FBX
fbx_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".fbx")]

for fbx_file in fbx_files:
    input_path = os.path.join(input_folder, fbx_file)
    output_file = os.path.splitext(fbx_file)[0] + ".glb"
    output_path = os.path.join(output_folder, output_file)

    print(f"\nProcessing {fbx_file}...")

    # Import FBX
    bpy.ops.import_scene.fbx(filepath=input_path)

    # Hapus semua mesh, lights, cameras, empties, dsb
    for obj in bpy.context.scene.objects:
        if obj.type not in ['ARMATURE']:
            bpy.data.objects.remove(obj, do_unlink=True)

    # Hapus orphans (object yang udah gak dipakai)
    try:
        bpy.ops.outliner.orphans_purge(do_recursive=True)
    except:
        pass

    # Export ke glTF (GLB)
    bpy.ops.export_scene.gltf(
        filepath=output_path,
        export_format='GLB',
        export_apply=True,
        export_animations=True,
        export_materials='NONE',
        export_cameras=False,
        export_lights=False,
        export_skins=True,
        export_morph=False
    )

    print(f"Saved cleaned animation to {output_path}")

    # Reset scene untuk loop berikutnya
    bpy.ops.wm.read_factory_settings(use_empty=True)

print("\n✅ All FBX files processed & cleaned!")
