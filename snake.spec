# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['snake.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='snake',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/Users/giovanni/PyCharm/pythonProject/snake/image/snake.icns'],
)
app = BUNDLE(
    exe,
    name='snake.app',
    icon='/Users/giovanni/PyCharm/pythonProject/snake/image/snake.icns',
    bundle_identifier=None,
)
