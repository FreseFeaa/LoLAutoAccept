# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['komarhelper.py'],
             pathex=['venv\\\\Lib\\\\site-packages', 'C:\\Users\\user\\Downloads\\lolauto'],
             binaries=[],
             datas=[
    ('img/acceptButtonImg.png', 'img'),
    ('img/acceptedButtonImg.png', 'img'),
    ('img/banActiveButton.png', 'img'),
    ('img/buttonBan.png', 'img'),
    ('img/banchamp.png', 'img'),
    ('img/championSelectionImg_emote.png', 'img'),
    ('img/playButtonImg.png', 'img'),
    ('img/championSelectionImg_flash.png', 'img'),
    ('img/supportIcon.png', 'img'),
    ('img/cryTeammateButton.png', 'img'),
],hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='KomaruHelper',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='auto_accept')
