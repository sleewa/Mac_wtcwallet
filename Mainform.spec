# -*- mode: python -*-

block_cipher = None


a = Analysis(['Mainform.py'],
             pathex=['/Users/swei/Desktop/veralalalala/WaltonWallet_Mac'],
             binaries=[],
             datas=[('/usr/local/lib/python3.6/site-packages/matplotlib-2.2.2.dist-info', 'matplotlib-2.2.2-py3.6.egg-info'),('/usr/local/lib/python3.6/site-packages/eth_utils-1.0.3.dist-info', 'eth_utils-1.0.3-py3.6.egg-info'),('/usr/local/lib/python3.6/site-packages/eth_keyfile-0.5.1.dist-info', 'eth_keyfile-0.5.1-py3.6.egg-info'),('/usr/local/lib/python3.6/site-packages/eth_abi-1.1.1.dist-info', 'eth_abi-1.1.1-py3.6.egg-info'),('/usr/local/lib/python3.6/site-packages/web3-4.3.0.dist-info', 'web3-4.3.0-py3.6.egg-info')],
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
          name='Mainform',
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
               name='Mainform')
app = BUNDLE(coll,
             name='Mainform.app',
             icon=None,
             bundle_identifier=None)
