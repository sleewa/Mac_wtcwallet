# -*- mode: python -*-

block_cipher = None


a = Analysis(['Mainformspec'],
             pathex=['/Users/swei/Desktop/veralalalala/WaltonWallet_Mac'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Mainformspec',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Mainformspec')
app = BUNDLE(coll,
             name='Mainformspec.app',
             icon=None,
             bundle_identifier=None)
