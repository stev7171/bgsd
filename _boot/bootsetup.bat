:: BIG-GOOFY SOFTWARE DISTRIBUTION
:: BOOTLOADER FIRMWARE 0.1.0
@echo off
cls
echo BGSD LOADER 1.0.0
echo LOADING GOOFY-FS...
ping localhost -n 1 >nul
echo LOADING A:/KERN.PTR...
ping localhost -n 1 >nul
echo BOOTING INTO 'BIG-GOOFY SOFTWARE DISTRIBUTION'...
ping localhost -n 1 >nul
cd ..
cd _kern
color 00
python startup.py