import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['1.png','themes/','buffer_img/', 'defected/', 'images/', 'models/', 'modules/', 'utils/', 'weights/', 'widgets/']
packages = ['PySide6', 'numpy', 'pyqtgraph', 'cv2', 'matplotlib', 'torch', 'torchvision', 'opencv-python']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="1.png"
)

# SETUP CX FREEZE
setup(
    name = "Submarine - HSAOIS",
    version = "1.0",
    description = "Hyper Speed Automatic Optical Inspection System",
    author = "Submarine team",
    options = {'build_exe' : 
                    {'include_files' : files,
                     'packages' : packages
                    }
    },
    executables = [target]
)
