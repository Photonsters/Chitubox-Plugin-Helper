# Chitubox-Plugin-Helper


    ###################################################
    ######## By Photonsters X3msnake v1.191122 ########
    ###################################################


This plugin needs Python 3.5+ to work and no extra dependencies


## INSTALLATION

    Download and install python
        https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe
    
    Make sure you select add python to PATH checkbox
        https://docs.python.org/3/using/windows.html
        
    If you forget to check the box you can run the installer again
    choose modify and add checkmark to the checkbox
    
    Download ChituboxPluginHelper.CHplugin and execute it, it will open Chitubox and self register
    
    Choose Debug.zip file when saving the sliced file to call the plugin


## HOW DOES THE PLUGIN WORK

This plugin intercepts Chitubox execute external program call, and keeps chitubox temporary folder open until you confirm or cancel the MessageBox that it pops up

The Message box displays the arguments (one per line) that are being passed to the executable file on the plugin folder

On Chitubox 1.5 the plugin is run after the slicing occured, during slicing chitubox creates a temporary directory were it dumps the sequential numbered slice images alongside with a text file run.gcode that contains all the software {properties} in the header along with tags for each section of the code and the passed values of set {property names} on the gcode resin profile boxes.


## HOW DOES CHITUBOX PLUGINS WORK

A chitubox plugin is a zip file with a .CHplugin extension with a plugin.jason text file and a executable.

The file plugin.jason registers the plugin and tells Chitubox what executable to run after slicing what extension to use and a couple of more properties.

Chitubox passes the path to the temp folder and the file name chosen by the user with full path as as arguments that you can captutre on the executable file

With that information you can parse the gcode file and modify it's contents, rename the files, even modify the images.

Once your executable file is finished Chitubox proceeds to zip the files found on its temporary folder and renames the file extension to the one you set in the json registration file.


Have fun making plugins, hope this helps ;)


The Photonsters Team
 

