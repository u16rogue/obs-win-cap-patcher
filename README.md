# obs-win-cap-patcher
Automatically patches [OBS](https://github.com/obsproject/obs-studio)'s `win-capture.dll` to use `CSIDL_WINDOWS` instead of `CSIDL_COMMON_APPDATA`, allowing it to load through Counter-Strike: Global Offesnive's Trusted Mode for Game Capture

## Usage
* *[Optional]* Open a terminal with admin privilege.
* Run `py obs-win-cap-patcher.py [optional | path to win-capture.dll]`
    * If you have the default OBS installation you don't need to specify the path, you can just run the script directly. (`C:\Program Files\obs-studio\obs-plugins\64bit\win-capture.dll`)
    * A `.bak` file is generated as a backup in the same directory.
* Run OBS as Administrator.
## VAC Ban?
* No guarantees but unlikely as this (`win-capture.dll`) is a legitimate module.

## Credits
* masterlooser15 - Original concept from this [thread](https://www.unknowncheats.me/forum/counterstrike-global-offensive/409060-obs-gamecapture.html).