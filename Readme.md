# coffeebreak
***
### About
A lightweight system tray app that forces you to wait to take a coffee break.
***
### Installation
#### (Windows only) Precompiled binary
1. Download coffeebreak.exe from Releases
***
#### Build from source (or simply run as a Python script)
1. Clone git repository
2. `pip install -r requirements.txt`
3. Clone `feature-explicit-backends` branch of `pystray` from [here](https://github.com/moses-palmer/pystray/tree/feature-explicit-backends) and place the `pystray` directory found in `/lib/` into coffeebreak's root
4. *(Optional)* `pyinstaller coffeebreak.spec` to build binary  

Current build of `pystray` (v0.17.3) doesn't properly work with `pyinstaller` for building the executable 
  

Tested on Windows 10 and Ubuntu 20. Feel free to try it out on Mac OS and let me know if there's any issues.
***
### Notes
Thanks to [Freepik](https://www.freepik.com) for the minimal icons
