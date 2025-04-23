@echo off
python -m PyInstaller --onefile --windowed mainApp.py ^
  --add-data "hash;hash" ^
  --add-data "tabsWidget;tabsWidget" ^
  --add-data "iconsDark;iconsDark" ^
  --add-data "resources_rc.py;." ^
  --add-data "common;common" ^
  --hidden-import hash.md5 ^
  --hidden-import hash.sha1 ^
  --hidden-import hash.sha256 ^
  --hidden-import common.common ^
  --hidden-import tabsWidget.tabWidgetMD5.resources_rc ^
  --hidden-import tabsWidget.tabWidgetSHA1.resources_rc ^
  --hidden-import tabsWidget.tabWidgetSHA256.resources_rc ^
  --hidden-import bitarray
pause
