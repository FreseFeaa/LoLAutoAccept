# KomaruHelper

Can automatically accept a game in LoL (and ban Swain, Optional feature, and you can choose a version without it) The author just doesn't like this character very much, so there is such a scenario initially :)

## How to use:
KomaruHelper has 2 versions:
- V1 - Accepts the game, waits for the ban phase and bans Swain
- V2 - Only accepts the game

Both versions are available in English and Russian.

**Installation:**
- Download the required version in zip format
- Unzip the resulting zip file

We get the following structure:
```
KomaruHelper
    ├───img
    ├───_internal
    └───KomaruHelper.exe  
```
- **img** - Folder with images for KomaruHelper to work with
- **_internal** - Various dependencies
- **KomaruHelper.exe** - Ready KomaruHelper
  
To use, you just need to run KomaruHelper.exe, a console window will pop up, which will display the current moment of the game search script.

It is better to create a shortcut of this exe file so that it can be conveniently called, for example, from the desktop (To do this, right-click on KomaruHelper.exe, create a shortcut)

Next, you can move this shortcut to a convenient place for you, and you can also change its icon. 

**To change the icon of the shortcut:**
- Right-click on the shortcut - Properties
- Change icon
- Browse...
- And then we find our KomaruHelper folder, in it the img folder, and there is already a ready-made icon komarExee.ico

## How it works:
The main idea is implemented using python-imageseach (Library for searching for matches of a part of an image on the screen with the initially specified one)
According to the specified scenario, various checks are performed, and based on the results of these checks, further actions are performed.

**General structure of the repository**:

```
KomaruHelper
├───Ready_versions
│       KomarHelper_V1_ENG.zip - Version with Swain's ban, in English
│       KomarHelper_V1_RU.zip - Version with Swain's ban, in Russian
│       KomarHelper_V2_ENG.zip - Version WITHOUT Swain's ban, in English
│       KomarHelper_V2_RU.zip - Version WITHOUT Swain's ban, in Russian
│
└───Source_code - Source code folder
    │   .gitignore
    │   komarhelper.py - All the basic logic
    │   komar_helper.spec - File to create exe
    │   requiremets.txt
    │
    └───img - Folder with all the necessary pictures
```

