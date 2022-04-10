from PySide6.QtWidgets import QWidget

class Upload(QWidget):
    """实现文件拖放功能"""

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True) # 设置接受拖放动作

    def dragEnterEvent(self, e):
        if e.mimeData().text().endswith('.png'): # 如果是.srt结尾的路径接受
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e): # 放下文件后的动作
        global selectedFile
        path = e.mimeData().text().replace('file:///', '') # 删除多余开头
        selectedFile.append(path)