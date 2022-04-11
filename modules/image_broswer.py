import shutil
import matplotlib.pyplot as plt
import main
from main import *
from PySide6.QtUiTools import QUiLoader
from global_var import *


class Window_img_broswer:

    def __init__(self):

        self.img_to_handle = [] # 图片的路径集合
        super().__init__()
        self.ui = QUiLoader().load('image_browser.ui')
        self.ui.setWindowTitle('Submarine - Image Browser')
        self.ui.pushButton_1.clicked.connect(self.scroll_up)
        self.ui.pushButton_2.clicked.connect(self.scroll_down)
        self.ui.pushButton_3.clicked.connect(self.generate_vis)
        self.num_img = 0
        self.img_set = []
        
        list_all_img = os.listdir(os.getcwd()+"/buffer_img")
        for i in list_all_img:
            if os.path.splitext(i)[1] == '.jpg':
                self.img_to_handle.append(i)
        self.ui.label_img.setAlignment(Qt.AlignCenter)
        current_img = QPixmap(os.getcwd()+"/buffer_img/"+self.img_to_handle[self.num_img])
        current_img = self.scale_img(780/665,current_img.width()/current_img.height(),current_img)
        self.ui.label_img.setPixmap(current_img)
        self.ui.tb_img.setAlignment(Qt.AlignCenter)
        self.ui.tb_img.clear()
        self.ui.tb_img.setText("Current/All:\n"+f"{self.num_img+1}/{len(self.img_to_handle)}")

    def scroll_up(self):
        self.num_img = self.num_img - 1
        img_to_handle = self.img_to_handle
        if self.num_img < 0:
            self.num_img = 0 
        if self.num_img >= 0:
            img = QPixmap(os.getcwd()+"/buffer_img/"+img_to_handle[self.num_img])
            img = self.scale_img(780/665,img.width()/img.height(),img)
            self.ui.label_img.setPixmap(img)
        self.ui.tb_img.clear()
        self.ui.tb_img.setText("Current/All:\n"+f"{self.num_img+1}/{len(self.img_to_handle)}")


    def scroll_down(self):
        self.num_img += 1 
        img_to_handle = self.img_to_handle
        if self.num_img <= len(img_to_handle)-1:
            img = QPixmap(os.getcwd()+"/buffer_img/"+img_to_handle[self.num_img])
            img = self.scale_img(780/665,img.width()/img.height(),img)
            self.ui.label_img.setPixmap(img)
        if self.num_img >= len(img_to_handle):
            self.num_img = len(img_to_handle)-1
        self.ui.tb_img.clear()
        self.ui.tb_img.setText("Current/All:\n"+f"{self.num_img+1}/{len(self.img_to_handle)}")

    def generate_vis(self):
        x = ["MotherBoard","CPU_FAN","FAN_Port"]
        y = [0,0,0]
        for i in global_var.get_value('list_for_vis'):
            if i == 0 or i == 1:
                y[1] += 1
            elif i == 6 or i == 7:
                y[0] += 1
            elif i == 5:
                y[2] += 1
        plt.figure(dpi=100)
        plt.bar(x,y)
        plt.savefig("./fileResult.jpg")
        self.ui.label_img.setPixmap(QPixmap("fileResult.jpg").scaledToWidth(self.ui.label_img.width(), Qt.SmoothTransformation))
        self.num_img = 0

    def scale_img(self,tar_hwr,hwr,current_img):
        if hwr > tar_hwr:
            current_img = current_img.scaledToWidth(self.ui.label_img.width(), Qt.SmoothTransformation)
        if hwr < tar_hwr:
            current_img = current_img.scaledToHeight(self.ui.label_img.height(), Qt.SmoothTransformation)
        return current_img


def get_pure_list(list_org, to_delete):
    list_tar = [i for i in list_org if i != to_delete]
    return list_tar

