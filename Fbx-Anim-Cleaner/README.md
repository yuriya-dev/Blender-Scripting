# FBX-Anim-Cleaner
Memisahkan mesh dengan animasi

✅ Input: folder berisi banyak FBX animasi (masih ada mesh di dalamnya)
✅ Output: anim-only GLB (atau FBX bersih)
  - Mesh dihapus
  - Hanya Armature + AnimationClip yang tersisa
  - Siap langsung dipakai di Three.js / React-Three-Fiber  
✅ Full otomatis via command line (tanpa GUI)

💻 Jalankan via Command Line (tanpa buka Blender GUI)
-> pastikan path folder sudah sesuai
```
"C:\Program Files\Blender Foundation\Blender 3.6\blender.exe" --background --python C:\Path\fbx_anim_cleaner.py" -- "C:\Path\InputFBX" "C:\Path\OutputGLB"
```

author:
--
<p align="center" >
  <a href="https://github.com/yuriya-dev" target="_blank">
    <img src="https://i.postimg.cc/F16xhxs4/avatar.png" alt="My Avatar" width="32" />
  </a>
  | yuriya-dev
</p>
