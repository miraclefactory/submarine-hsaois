from setuptools import setup

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