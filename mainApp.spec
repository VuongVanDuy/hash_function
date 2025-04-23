# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['mainApp.py'],
    pathex=[],
    binaries=[],
    datas=[('hash', 'hash'), ('tabsWidget', 'tabsWidget'), ('iconsDark', 'iconsDark'), ('resources_rc.py', '.'), ('common', 'common')],
    hiddenimports=['hash.md5', 'hash.sha1', 'hash.sha256', 'common.common', 'tabsWidget.tabWidgetMD5.resources_rc', 'tabsWidget.tabWidgetSHA1.resources_rc', 'tabsWidget.tabWidgetSHA256.resources_rc', 'bitarray'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='mainApp',
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
)
