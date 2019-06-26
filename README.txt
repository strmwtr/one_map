Author: Bob Brown
Contact Info: brownr@charlottesville.org
Created: June 2019
Purpose: Create database and data structure for Bicycle and Pedestrian One Map project.
Repo: https://github.com/strmwtr/one_map
File onemap_py2 uses python 2 to create gdb and feature class. If you have ArcMap on your computer run this version.
File onemap_py3 uses python 3 to create gdb and feature class. If you have ArcPro on your computer run this version.

If you have never run a script before follow these instructions:

1. Download the .py file that matches your python version (onemap_py2 vs onemap_py3)
2. Open File Explorer, find you python.exe. Try these locations first, but they vary by installtion
	- ArcPro: C:Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe
	- ArcMap: C:\Python27\ArcGIS10.{x}\python.exe
3. Open the Command Prompt
	- Crtl + W
	- Type "cmd", hit enter

4. Enter the following, substituting your python.exe and onemap_pyX.py paths in the Command Prompt Window
	C:\path\to\python.exe C:\path\to\onemap_pyX.py

5. Hit enter.

6. Soon the Command Prompt window with show: 
	"Existing file directory to store gdb: "

7. Provide an existing file directory for the gdb to be created and the polyline feature to be created.
	Existing file directory to store gdb: C:\path\to\project\folder

8. The Command Prompt window will state "Done" after a short period of time.

9. Go to the directory provided in step 7. In the directory will be a OneMap.gdb and inside the gdb will be a OneMap polyline feature class.
This feature class will have all of the agreed upon fields and domains for the fields. 
