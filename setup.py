import sys
import os
# from cx_Freeze import setup, Executable
from setuptools import setup

# ADD FILES
# files = ['1.png','themes/','buffer_img/', 'defected/', 'images/', 'models/', 'modules/', 'utils/', 'weights/', 'widgets/']
# packages = ['PySide6', 'numpy', 'pyqtgraph', 'cv2', 'matplotlib', 'torch', 'torchvision', 'opencv-python']

# # TARGET
# target = Executable(
#     script="main.py",
#     base="Win32GUI",
#     icon="1.png"
# )

# # SETUP CX FREEZE
# setup(
#     name = "Submarine - HSAOIS",
#     version = "1.0",
#     description = "Hyper Speed Automatic Optical Inspection System",
#     author = "Submarine team",
#     options = {'build_exe' : 
#                     {'include_files' : files,
#                      'packages' : packages
#                     }
#     },
#     executables = [target]
# )


APP = ['main.py']
DATA_FILES = ['logo.png','themes/','buffer_img/', 'defected/', 'images/', 'models/', 'modules/', 'utils/', 'weights/', 'widgets/'] # 附件
OPTIONS = {'iconfile': 'logo.png', # 图标
           'packages': ['PySide6', 'numpy', 'pyqtgraph', 'cv2', 'matplotlib', 'torch', 'torchvision', 'opencv-python']} # 第三方库

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)