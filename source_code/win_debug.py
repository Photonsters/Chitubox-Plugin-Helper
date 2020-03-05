#!/usr/bin/env python3
#######################################
## By Photonsters X3msnake v1.191122 ##
#######################################

# plugin requires python 3.5+ with windows paths set
# See readme for instalation

import ctypes
import sys
import os
import subprocess

print(sys.argv.__len__())


# Open Chitubox passed argument temp folder

if sys.argv.__len__() > 1:
    try:
        path = sys.argv[1]
        subprocess.run(['explorer', os.path.realpath(path)])
    except:
        print("Failed to open path")
        

# Show message


args = sys.argv
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    
Mbox('Debugger plugin', '\r'.join(sys.argv) , 0x00000040)

### Code References

# Mbox Styles:
# 0 : OK
# 1 : OK | Cancel
# 2 : Abort | Retry | Ignore
# 3 : Yes | No | Cancel
# 4 : Yes | No
# 5 : Retry | No 
# 6 : Cancel | Try Again | Continue

# https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
# https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments-in-python
# https://stackoverflow.com/questions/187455/counting-array-elements-in-python
# https://www.w3schools.com/python/python_try_except.asp
# https://realpython.com/python-string-split-concatenate-join/
# https://www.askvg.com/list-of-environment-variables-in-windows-xp-vista-and-7/
# https://stackoverflow.com/questions/27257018/python-messagebox-with-icons-using-ctypes-and-windll
