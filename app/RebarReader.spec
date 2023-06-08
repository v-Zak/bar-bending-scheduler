# -*- mode: python ; coding: utf-8 -*-

import sys
sys.setrecursionlimit(5000) # (or some big number)

from kivy_deps import sdl2, glew

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['ezdxf', 'sys', 'os', 'csv'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz, Tree('C:\\Dev\\Github\\bar-bending-scheduler\\app\\'),
     a.scripts,
     a.binaries,
     a.zipfiles,
     a.datas,
     *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
     upx=True,
     console=False,
     name='RebarReader')
