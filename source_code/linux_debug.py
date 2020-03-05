#!/usr/bin/env python3
#######################################
## By Photonsters X3msnake v2.200305 ##
#######################################

# plugin requires python 3.5+
# See readme for instalation

import sys
import subprocess

# Check number of passed arguments
print(sys.argv.__len__())

messagebox_txt = "The number of args is "+ str(sys.argv.__len__())

# Open Chitubox passed argument temp folder
if sys.argv.__len__() > 1:
    try:
        for i in range(len(sys.argv)):
        	print (sys.argv[i])
        	messagebox_txt = messagebox_txt+"\r"+str(i)+" > "+str(sys.argv[i])
    except:
        print("Failed to open path")

# Popup window with Ctypes

subprocess.run(["/usr/bin/notify-send", "--icon=dialog-warning", messagebox_txt])
