# CyberiusUnzipCracker.spec
# Generado para empaquetar Main.py como .exe con ícono personalizado

block_cipher = None

a = Analysis(
    ['Main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('cyberius.ico', '.'),  # icono
        ('unrar.exe', '.'),     # descompresor RAR
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CyberiusUnzipCracker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # ⛔ sin consola
    icon='cyberius.ico'  # ✅ icono personalizado
)
