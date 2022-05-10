from setuptools import setup

APP = ['main.py']
DATA_FILES = ['app.png','themes/','file_result/', 'img_buffer/', 'images/', 'models/', 'modules/', 'utils/', 'weights/', 'widgets/'] # 附件
OPTIONS = {'iconfile': 'app.png', # 图标
           'packages': ['PySide6', 'numpy', 'pyqtgraph', 'cv2', 'matplotlib', 'torch', 'torchvision', 'opencv-python', 'scipy', 'PIL', 'paramiko']} # 第三方库

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)