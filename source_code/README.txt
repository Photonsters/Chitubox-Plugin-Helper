    ###################################################
    ######## By Photonsters X3msnake v1.191122 ########
    ###################################################


This plugin needs Python 3.5+ to work, and no extra dependencies.




## INSTALLATION

    Download and install python
        https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe
    
    Make sure you select the "Add Python to PATH" checkbox
        https://docs.python.org/3/using/windows.html
    
    If you forget to check the box, you can run the installer again, then
    choose modify and add checkmark to the checkbox to set the executable search path.
    
    Download ChituboxPluginHelper.CHplugin and execute it, it will open Chitubox and self register.
    
    Choose "Debug.zip" file format when saving the sliced file to call the plugin.
	
	Notes: to compile the windows python.py into a single exe > pyinstaller --onefile --windowed win_debug.py.py



## HOW DOES THE PLUGIN WORK?

This plugin intercepts the Chitubox "execute external" program call, and keeps the chitubox temporary folder open until you confirm or cancel the MessageBox that it shows.

The Message box displays the arguments (one per line) that were passed to the executable file on the plugin folder. Everytime you run the plugin it also opens the temporary folder and this plugin install folder.

On Chitubox 1.5 the plugin is run after slicing occurs. During slicing Chitubox creates a temporary directory were it dumps the sequential numbered slice images, and a text file run.gcode that contains all the software {properties} in the header along with tags for each section of the code and the passed values of set {property names} on the gcode resin profile boxes.


## HOW DO CHITUBOX PLUGINS WORK?

A Chitubox plugin is a zip file with a .CHplugin extension, containing a plugin.jason text file and an executable.

The file plugin.jason registers the plugin and tells Chitubox what executable to run after slicing, what file extension to use, and a couple more properties.

Chitubox passes the path to the temp folder and the file name chosen by the user, with full path as as arguments that you can capture in the executable file.

With that information you can parse the gcode file and modify the contents, rename the files, even modify the images.

Once your executable file is finished, Chitubox proceeds to zip the files found in its temporary folder and renames the resulting file extension to the one you set in the json registration file.


Have fun making plugins, I hope this helps ;)

The Photonsters Team







 

