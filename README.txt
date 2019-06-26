Author: Bob Brown
Contact Info: brownr@charlottesville.org
Created: June 2019
Purpose: Create database and data structure for Bicycle and Pedestrian One Map project.
Repo: https://github.com/strmwtr/one_map
File onemap_py2 uses python 2 to create gdb and feature class. If you have ArcMap on your computer run this version.
File onemap_py3 uses python 3 to create gdb and feature class. If you have ArcPro on your computer run this version.

If you have never run a script before follow these instructions:
- Download the .py file that matches your python version (onemap_py2 vs onemap_py3)
- Crtl + W
- Type "cmd"
- Open File Explorer, find you python.exe
	- Try these locations first, but they vary by installtion
	- ArcPro: C:Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe
	- ArcMap: C:\Python27\ArcGIS10.{x}\python.exe
- For ArcMap users, in the Command Prompt window paste the following
C:\path\to\python.exe C:\path\to\onemap_py2.py

- For ArcPro users, in the Command Prompt window paste the following
C:\path\to\python.exe C:\path\to\onemap_py3.py

The script will begin to run, soon you will be promted with 
"Existing file directory to store gdb: "

Provide an existing file directory for the gdb to be created and the polyline feature to be created.
"Existing file directory to store gdb: " C:\path\to\project\folder

