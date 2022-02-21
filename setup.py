import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "Submarine",
    version = "1.0",
    description = "Hyper Speed Optical Inspection",
    author = "Submarine team",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
