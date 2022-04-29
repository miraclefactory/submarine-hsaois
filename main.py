# ///////////////////////////////////////////////////////////////
#
# BY: Submarine
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import os
import sys
import time
import scipy
import shutil
import random
import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import Signal
from threading import Thread, Lock
from cv2 import getTickCount, getTickFrequency
from concurrent.futures import ThreadPoolExecutor
# IMPORT MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from widgets import *
from modules import *
from modules.db import *
from modules.detect import *
from modules import global_var
from modules.letterbox import *
from modules.report_text import *
from modules.sync_database import *
from modules.shit_algorithm import *
from modules.data_visualization import *
from utils.torch_utils import select_device
from models.experimental import attempt_load
from modules.splash_screen import SplashScreen
from modules.image_broswer import Window_img_broswer, get_pure_list
from widgets.custom_grips.custom_grips import Widgets
from utils.general import (check_img_size, non_max_suppression, scale_coords, plot_one_box)

# SET DPI AND SCALING
# ///////////////////////////////////////////////////////////////
# os.environ["QT_FONT_DPI"] = "70"    # FIX Problem for High DPI and Scale above 100%
# os.environ["QT_SCALE_FACTOR"] = "2"
QT_AUTO_SCREEN_SCALE_FACTOR=2

# SET GLOBAL VARIABLES
# ///////////////////////////////////////////////////////////////
widgets = None          # GLOBAL CLASS VARIABLE FOR ALL UI COMPONENTS
img_broswer = None      # GLOBAL CLASS VARIABLE FOR IMAGE UI COMPONENTS
selectedFile = []       # BUFFER FOR SELECTED FILE
lock = Lock()           # LOCK FOR THREADS
flag = False            # CHECK IF CAMERA IS LOADED
is_live_mode = False    # TOGGLE DETECTION
hashpool = []
input_list = []
is_new_img = True
cnt = 0
is_defetced = False
is_scan_mode = False
seq = 1                 # SERIAL NUMBER
class_total = [0 for i in range(12)]
defected_total = 0
global_var._init()

init_table()
if verify_general_table():
    init_batch()
batch_num = fetch_last_batch_num()


class MainWindow(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        # INITIALIZE MODEL
        # ///////////////////////////////////////////////////////////////
        parser = argparse.ArgumentParser()
        parser.add_argument('--weights', nargs='+', type=str, default='weights/focus_bs9.pt', help='model.pt path(s)')
        parser.add_argument('--source', type=str, default='images', help='source')  # file/folder, 0 for webcam
        parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
        parser.add_argument('--conf-thres', type=float, default=0.3, help='object confidence threshold')
        parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
        parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
        parser.add_argument('--view-img', action='store_true', help='display results')
        parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
        parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
        parser.add_argument('--save-dir', type=str, default='results', help='directory to save results')
        parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
        parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
        parser.add_argument('--augment', action='store_true', help='augmented inference')
        parser.add_argument('--update', action='store_true', help='update all models')
        self.opt = parser.parse_args()
        ut, source, weights, view_img, save_txt, imgsz = self.opt.save_dir, self.opt.source, self.opt.weights, \
            self.opt.view_img, self.opt.save_txt, self.opt.img_size
        self.device = select_device(self.opt.device)
        self.half = self.device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        self.model = attempt_load(weights, map_location=self.device)  # load FP32 model
        self.imgsz = check_img_size(imgsz, s=self.model.stride.max())  # check img_size
        if self.half:
            self.model.half()  # to FP16

        cudnn.benchmark = True  # set True to speed up constant image size inference

        # Get names and colors
        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names
        self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(self.names))]

        # INITIALIZE UI
        # ///////////////////////////////////////////////////////////////

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.centerWindow()

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = False

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Submarine - HSAOIS®"
        description = "Submarine - Hyper Speed Automatic Optical Inspection System®"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_detect.clicked.connect(self.buttonClick)
        widgets.btn_dash.clicked.connect(self.buttonClick)
        widgets.btn_report.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # BOTTOM BOX
        # ///////////////////////////////////////////////////////////////
        widgets.btn_python.clicked.connect(self.pythonInfo)

        # HOME PAGE
        # ///////////////////////////////////////////////////////////////
        widgets.video_tu.clicked.connect(self.openURL)
        widgets.label_documentation.setOpenExternalLinks(True)
        widgets.label_database.setOpenExternalLinks(True)
        widgets.label_custom_model.setOpenExternalLinks(True)

        # DETECT PAGE
        # ///////////////////////////////////////////////////////////////
        # widgets.upload = Upload()

        # SIGNAL
        # ///////////////////////////////////////////////////////////////
        self.es = EmitSignal()
        self.es.text_print.connect(self.printToTextBrowser)
        self.es.message_box.connect(self.createMessageBox)
        self.es.video.connect(self.updateImage)
        self.es.clear.connect(self.clearVideoBox)
        self.es.stop.connect(self.stopTimer)
        self.es.update_graph.connect(self.updateGraph)
        self.es.update_table.connect(self.updateTable)

        # DETECT
        # ///////////////////////////////////////////////////////////////
        widgets.btn_start_file.clicked.connect(self.fileDetectMode)
        widgets.btn_stop_file.clicked.connect(self.terminate)
        widgets.btn_result.clicked.connect(self.open_result)
        widgets.btn_file.clicked.connect(self.selectFiles)

        # STREAM
        # ///////////////////////////////////////////////////////////////
        self.cap = cv2.VideoCapture()
        self.timer_camera = QTimer()
        self.timer_camera.timeout.connect(self.openFrame)
        widgets.btn_start_live.clicked.connect(self.liveDetectMode)
        widgets.top_start_live.clicked.connect(self.liveDetectMode)
        widgets.btn_stop_live.clicked.connect(self.stopStream)
        widgets.top_stop_live.clicked.connect(self.stopStream)
        widgets.top_stop_live.setEnabled(False)
        widgets.btn_stop_live.setEnabled(False)
        widgets.btn_scan.clicked.connect(self.scanDetectMode)
        widgets.video_viewer.setAlignment(Qt.AlignCenter)
        # widgets.video_viewer.setPixmap(QPixmap(":images/images/images/smile.png").scaledToWidth(50))

        # REPORT PAGE
        # ///////////////////////////////////////////////////////////////
        widgets.btn_search.clicked.connect(self.search_for_batch_results)
        widgets.search_box.returnPressed.connect(self.search_for_batch_results)

        # PYQTGRAPH
        # ///////////////////////////////////////////////////////////////
        widgets.line_graph.setBackground((240, 240, 245))
        widgets.line_graph.setLabel('left', 'Defective(%)', color='#705597')
        widgets.line_graph.setLabel('bottom', 'Class', color='#705597')
        widgets.line_graph.showGrid(x=True, y=True)
        # widgets.line_graph.setYRange(min=0, max=1)
        widgets.line_graph.setXRange(min=0, max=6)
        widgets.line_graph.setMouseEnabled(x=False, y=False)
        pg.setConfigOptions(leftButtonPan=False, antialias=True)
        pen = pg.mkPen({'color': "#705597", 'width': 3})
        self.curve = widgets.line_graph.plot(pen=pen, symbol='o', symbolBrush=QColor("#705597"))
        self.xtick = [list(zip(range(7), ("mbns", "mbls", "cfns", "cfls", "cfpd", "mbs", "mbws")))]
        xax = widgets.line_graph.getAxis('bottom')
        xax.setTicks(self.xtick)
        self.x_axis = [0, 1, 2, 3, 4, 5, 6]
        self.y_axis = [0, 0, 0, 0, 0, 0, 0]
        self.curve.setData(self.x_axis, self.y_axis)
        widgets.progressBar_1.setValue(0)
        widgets.progressBar_2.setValue(0)
        widgets.progressBar_3.setValue(0)

        # PYQTGRAPH_report
        # ///////////////////////////////////////////////////////////////
        widgets.batch_data_graph.setBackground((245, 245,248))
        widgets.batch_data_graph.setLabel('left', 'Defective per Batch(%)', color='#705597')
        widgets.batch_data_graph.setLabel('bottom', 'Class', color='#705597')
        widgets.batch_data_graph.showGrid(x=True, y=True)
        widgets.batch_data_graph.setXRange(min=0, max=20)
        widgets.batch_data_graph.setYRange(min=0, max=100)
        widgets.batch_data_graph.setMouseEnabled(x=True, y=False)
        pg.setConfigOptions(leftButtonPan=False, antialias=True)
        pen = pg.mkPen({'color': "#705597", 'width': 3})
        self.curve2 = widgets.batch_data_graph.plot(pen=pen, symbol='s', symbolBrush=QColor("#705597"))
        self.x_axis_batch = fetch_batch_num()
        self.y_axis_batch = self.handle_per_list(fecth_defective_data())

        # DATABASE
        # ///////////////////////////////////////////////////////////////
        widgets.btn_data_upload.clicked.connect(self.uploadDatabase)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        themeFile = "themes/py_quiet_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            app_functions.AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_detect":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_dash":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_report":
            widgets.stackedWidget.setCurrentWidget(widgets.report)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # REPOSITION EVENTS
    def centerWindow(self):
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    # SLOT FUNCTIONS FOR THREAD EMITTED SIGNALS
    # ///////////////////////////////////////////////////////////////
    def printToTextBrowser(self, text):
        # PRINT TEXT FROM THREAD
        widgets.textBrowser.append(str(text))
        widgets.textBrowser.ensureCursorVisible()

    def createMessageBox(self, title, text):
        QMessageBox.information(None, title, text)

    def updateImage(self, image):
        widgets.video_viewer.setPixmap(
            QPixmap.fromImage(image).scaledToWidth(widgets.video_viewer.width(), Qt.SmoothTransformation))

    def clearVideoBox(self):
        widgets.video_viewer.clear()

    def stopTimer(self):
        self.timer_camera.stop()

    def updateGraph(self, data, seq, frac):
        self.curve.setData(self.x_axis, data)
        widgets.detected.setText(str(seq))
        widgets.frac_defective.setText(str(round(frac, 2) * 100) + "%")
        text = [self.xtick[0][int(i[1])][1] for i in zip(data, self.x_axis) if i[0] == max(data)]
        if len(text) > 0:
            widgets.most_defected.setText(str(text[0]))
        mb = class_total[6]+class_total[7]+class_total[8]+class_total[9]
        widgets.progressBar_1.setValue(mb)
        cpu_fan = class_total[0] + class_total[2]
        widgets.progressBar_2.setValue(cpu_fan)
        fan_port = class_total[5]
        widgets.progressBar_3.setValue(fan_port)
        update_class_table(mb, cpu_fan, fan_port)

    def updateTable(self, ls, num):
        widgets.tableWidget.setItem(num, 0, QTableWidgetItem(str(num)))
        widgets.tableWidget.setItem(num, 1, QTableWidgetItem(ls[0]))
        widgets.tableWidget.setItem(num, 2, QTableWidgetItem(ls[1]))
        widgets.tableWidget.setItem(num, 3, QTableWidgetItem(ls[2]))
    
    # OPEN LINKS
    # ///////////////////////////////////////////////////////////////
    def openURL(self):
        QDesktopServices.openUrl(QUrl("https://www.osl.ink"))

    # BUTTON FUNCTIONS
    # ///////////////////////////////////////////////////////////////
    def pythonInfo(self):
        py_info = QMessageBox()
        py_info.setText("Python version: \n\n" + sys.version)
        py_info.setIconPixmap(QPixmap("images/icons/python.svg"))
        py_info.exec_()

    def selectFiles(self):
        # OPEN FILES
        widgets.textBrowser.append("Working Directory: " + os.getcwd())
        file_path = QFileDialog.getOpenFileNames(self, "Open File", "",
                                                 "image/video files (*.jpg *.png *.jpeg *.heic *.bmp *.mp4)")
        global selectedFile
        selectedFile = file_path[0]
        for i in selectedFile:
            widgets.textBrowser.append("Open File: " + i)

    def dragEnterEvent(self, e):
        if e.mimeData().text().endswith('.png') or e.mimeData().text().endswith('.jpg'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, event: QDropEvent):
        global selectedFile
        try:
            if event.mimeData().hasUrls:
                event.setDropAction(Qt.Qt.CopyAction)
                event.accept()
                for url in event.mimeData().urls():
                    selectedFile.append(str(url.toLocalFile()))
                print(selectedFile)
            else:
                event.ignore()
        except Exception as e:
            print(e)

    def open_result(self):
        path_to_delete = os.getcwd()+""
        global img_broswer
        img_broswer = Window_img_broswer()
        img_broswer.ui.show()

    def stopStream(self):
        global is_live_mode, is_scan_mode, pool
        is_live_mode = False
        is_scan_mode = False
        # pool.shutdown()
        widgets.btn_start_live.setEnabled(True)
        widgets.top_start_live.setEnabled(True)
        widgets.top_stop_live.setEnabled(False)
        widgets.btn_stop_live.setEnabled(False)
        widgets.btn_scan.setEnabled(True)
        widgets.status_label.setText("Ready")
        self.updateDataGraph()
        self.uploadDatabase()

    def terminate(self):
        # RAISE INTERRUPT EXCEPTION
        raise (InterruptedError("Session Terminated"))
    
    def uploadDatabase(self):
        widgets.btn_data_upload.setIcon(QIcon(":/icons/images/icons/upload.svg"))
        thread = Thread(target=self.sync_db)
        thread.start()

    # LIVE DETECT
    # ///////////////////////////////////////////////////////////////
    def liveDetectMode(self):
        global is_live_mode, pool
        self.cap.release()
        if self.timer_camera.isActive() is False:
            flag = self.cap.open("test.mp4")
            if flag is False:
                QMessageBox.warning(self, u"Warning", u"Please Check Your Camera Source",
                                    buttons=QMessageBox.Ok,
                                    defaultButton=QMessageBox.Ok)
            else:
                self.reset_all()
                is_live_mode = True
                widgets.btn_start_live.setEnabled(False)
                widgets.top_start_live.setEnabled(False)
                widgets.top_stop_live.setEnabled(True)
                widgets.btn_stop_live.setEnabled(True)
                widgets.btn_scan.setEnabled(False)
                widgets.status_label.setText("Live Detecting")
                widgets.textBrowser.append("\n<h4 style='color: #705597; font-weight: normal;\
                                           font-family: monaco;'>[Run] Live Detecing...</h4>\n")
                self.timer_camera.start(50)
                pool = ThreadPoolExecutor(max_workers=5)
        else:
            self.timer_camera.stop()
            self.cap.release()
            widgets.video_viewer.clear()
            widgets.textBrowser.setText(u'Please Open Your Camera')

    def scanDetectMode(self):
        global is_scan_mode, pool
        self.cap.release()
        if self.timer_camera.isActive() is False:
            flag = self.cap.open(0)
            if flag is False:
                QMessageBox.warning(self, u"Warning", u"Please Check Your Camera Source",
                                    buttons=QMessageBox.Ok,
                                    defaultButton=QMessageBox.Ok)
            else:
                self.reset_all()
                is_scan_mode = True
                widgets.btn_start_live.setEnabled(False)
                widgets.top_start_live.setEnabled(False)
                widgets.top_stop_live.setEnabled(True)
                widgets.btn_stop_live.setEnabled(True)
                widgets.btn_scan.setEnabled(False)
                widgets.status_label.setText("Scan Detecting")
                widgets.textBrowser.append("\n<h4 style='color: #705597;font-weight: normal;\
                                           font-family: monaco;'>[Run] Scan Detecing...</h4>\n")
                self.timer_camera.start(50)
                pool = ThreadPoolExecutor(max_workers=5)
        else:
            self.timer_camera.stop()
            self.cap.release()
            widgets.video_viewer.clear()
            widgets.textBrowser.setText(u'Please Open Your Camera')

    def reset_all(self):
        global seq, defected_total, class_total, hashpool, input_list, batch_num, trig
        self.x_axis_batch = fetch_batch_num()
        self.y_axis_batch = self.handle_per_list(fecth_defective_data())
        seq = 1
        trig = True
        hashpool = []
        input_list = []
        batch_num += 1
        defected_total = 0
        self.y_axis = [0, 0, 0, 0, 0, 0, 0]
        class_total = [0 for i in range(11)]
        self.es.update_graph.emit(self.y_axis, seq-1, defected_total/seq)
        widgets.most_defected.setText("None")
        widgets.batch_number.setText(str(batch_num))
        widgets.tableWidget.clearContents()
        widgets.tableWidget.setItem(0, 0, QTableWidgetItem("Log Entry"))
        widgets.tableWidget.setItem(0, 1, QTableWidgetItem("Serial Number"))
        widgets.tableWidget.setItem(0, 2, QTableWidgetItem("Result Class"))
        widgets.tableWidget.setItem(0, 3, QTableWidgetItem("Notes"))

    def openFrame(self):
        global pool, is_scan_mode, is_live_mode
        if is_scan_mode:
            pool.submit(self.scanDetectThread)
        if is_live_mode:
            pool.submit(self.liveDetectThread)
        pass

    def liveDetectThread(self):
        lock.acquire()
        global is_live_mode, flag, hashpool, input_list, is_new_img, \
            cnt, is_defetced, seq, class_total, defected_total
        flag, img = self.cap.read()
        if img is not None:
            showimg = img
            cvimg = img
            total_name = []
            handleimg = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            class_list = self.process_image(img, showimg, total_name)
            hsv = caculateHashValue(handleimg)
            hashpool.append(hsv)
            if len(hashpool) > 1:
                for i in range(len(hashpool)-1):
                    hmd = caculateHammingDistance(hashpool[i], hashpool[i+1])
                    if is_live_mode is False:
                        hmd = 5
                    if hmd == 0:
                        cnt += 1
                        if len(class_list) > 1:
                            input_list.append(class_list)
                        if cnt > 10 and is_new_img:
                            is_new_img = False
                            if is_defetced == False and len(input_list) > 1:
                                is_defetced = True
                        hashpool = hashpool[i+1:]
                        break
                    if hmd >= 5:
                        if len(input_list) > 0:
                            a = feature_max_pooling([length_weighted_average_pooling(i)
                                                for i in segementation(input_list, 4)])
                            if detect_error(self, a, seq) is True:
                                defected_total += 1
                                bn = batch_num
                                self.es.update_table.emit(["BN-"+str(bn)+"-SN-"+str(seq),
                                                          str(a), "none"], defected_total)
                                for i in a:
                                   if i in [0, 1, 3, 5, 6, 7, 8, 9]:
                                        update_error_pic(cvimg)
                                        break
                                update_error_details(Vector_output=a, \
                                                     serial_number="BN-"+str(bn)+"-SN-"+str(seq))
                            self.y_axis = update_line_graph(self.y_axis, a, class_total, seq)
                            self.es.update_graph.emit(self.y_axis, seq, defected_total/seq)
                            seq += 1
                        is_defetced = False
                        input_list = []
                        is_new_img = True
                        cnt = 0
                        hashpool = hashpool[i+1:]
                        break
            if is_live_mode is False:
                self.es.stop.emit()
                self.cap.release()
                self.es.text_print.emit("<h4 style='color: rgb(49,107,205);font-weight: normal;\
                                        font-family: monaco;'>[Stop] Live Detect Session Suspended</h4>")
        else:
            flag = False
            self.es.clear.emit()
        lock.release()

    def scanDetectThread(self):
        lock.acquire()
        global is_live_mode, flag, hashpool, input_list, is_new_img, \
            cnt, is_defetced, seq, class_total, defected_total
        flag, img = self.cap.read()
        if img is not None:
            showimg = img
            cvimg = img
            total_name = []
            handleimg = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            class_list = self.process_image(img, showimg, total_name)
            hsv = caculateHashValue(handleimg)
            hashpool.append(hsv)
            if len(hashpool) > 1:
                for i in range(len(hashpool)-1):
                    hmd = caculateHammingDistance(hashpool[i], hashpool[i+1])
                    if hmd <= 2:
                        cnt += 1
                        if len(class_list) > 1:
                            input_list.append(class_list)
                        if cnt > 5 and is_new_img:
                            is_new_img = False
                            if is_defetced == False and len(input_list) > 1:
                                is_defetced = True
                            if cnt >= 6:
                                if len(input_list) > 0:
                                    a = feature_max_pooling([length_weighted_average_pooling(i)
                                                        for i in segementation(input_list, 4)])
                                    if detect_error(self, a, seq) is True:
                                        defected_total += 1
                                        bn = batch_num
                                        self.es.update_table.emit(["BN-"+str(bn)+"-SN-"+str(seq),
                                                                  str(a), "none"], defected_total)
                                        for i in a:
                                            if i in [0, 1, 3, 5, 6, 7, 8, 9]:
                                                update_error_pic(cvimg)
                                                break
                                        update_error_details(Vector_output=a, \
                                            serial_number="BN-"+str(bn)+"-SN-"+str(seq))                          
                                    self.y_axis = update_line_graph(self.y_axis, a, class_total, seq)
                                    self.es.update_graph.emit(self.y_axis, seq, defected_total/seq)
                                    seq += 1
                        hashpool = hashpool[i+1:]
                        break
                    if hmd >= 5:
                        is_defetced = False
                        input_list = []
                        is_new_img = True
                        cnt = 0
                        hashpool = hashpool[i+1:]
                        break
            if is_scan_mode is False:
                self.es.stop.emit()
                self.cap.release()
                self.es.text_print.emit("<h4 style='color: rgb(49,107,205);font-weight: normal;\
                                        font-family: monaco;'>[Stop] Scan Detect Session Suspended</h4>")
        else:
            flag = False
            self.es.clear.emit()
        lock.release()

    def process_image(self, img, showimg, total_name):
        with torch.no_grad():
            img = letterbox(img, new_shape=self.opt.img_size)[0]
            # CONVERT MATRIX
            img = img[:, :, ::-1].transpose(2, 0, 1)
            img = np.ascontiguousarray(img)
            img = torch.from_numpy(img).to(self.device)
            img = img.half() if self.half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)
            # INFERENCE
            pred = self.model(img, augment=self.opt.augment)[0]
            # APPLY NMS
            pred = non_max_suppression(pred, self.opt.conf_thres, self.opt.iou_thres,
                                       classes=self.opt.classes, agnostic=self.opt.agnostic_nms)
            # PROCESS DETECTIONS
            class_list = []
            for i, det in enumerate(pred):  # DETECTTIONS PER IMAGE
                if det is not None and len(det):
                    # RESCALE BOXES FROM img_size TO im0 SIZE
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], showimg.shape).round()
                    # WRITE RESULTS
                    for *xyxy, conf, cls in reversed(det):
                        label = '%s %.2f' % (self.names[int(cls)], conf)
                        total_name.append(label)
                        box = str(str(int(xyxy[0])) + ' ' + str(int(xyxy[1])) + ' ' + \
                            str(int(xyxy[2])) + ' ' + str(int(xyxy[3])))
                        total_name.append(box)
                        plot_one_box(xyxy, showimg, label=label, color=self.colors[int(cls)],
                                     line_thickness=2)  # DRAW A BOUNDING BOX ON THE IMAGE
                        class_list.append(int(cls.item()))
        tl = round(0.002 * (showimg.shape[0] + showimg.shape[1]) / 2) + 1 # LINE/FONT THICKNESS
        self.reclabel = total_name
        self.result = cv2.cvtColor(showimg, cv2.COLOR_BGR2RGB)
        showImage = QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                           QImage.Format_RGB888)
        self.es.video.emit(showImage)
        return class_list

    # FILE DETECT
    # ///////////////////////////////////////////////////////////////
    def fileDetectMode(self):
        if len(selectedFile) == 0:
            QMessageBox.warning(None, "Warning",
                                "Please select a file first!", QMessageBox.Ok)
        else:
            widgets.textBrowser.append("\n[Run] File Detecting...\n")
            thread = Thread(target=self.fileDetectThread)
            thread.start()

    def fileDetectThread(self):
        shutil.rmtree(os.getcwd()+"/file_result")
        os.mkdir(os.getcwd()+"/file_result")
        global status_code
        status_code = 0
        e1 = getTickCount()                                     # START TIME
        for i in selectedFile:
            try:
                sys.argv[1:4] = ["--source", i, "--save-txt"]   # SET ARGUMENTS
                input_class = detect()                          # RECEIVE ClASS RESULT
                for i in input_class:
                    global_var.set_value_list(
                        "list_for_vis", global_var.get_value("list_for_vis").append(i))
                self.es.text_print.emit("Detect Class Result: " + str(input_class))
            except FileNotFoundError:
                self.es.text_print.emit("Detect Mode Error: " + "File Not Found")
                status_code = 1
            except InterruptedError:
                self.es.text_print.emit("Detect Mode Warning: " + "Session Terminated")
                status_code = 99
            except:
                self.es.text_print.emit("Detect Mode Error: " + "Unknown Error")
                status_code = 2
        e2 = getTickCount()                                     # END TIME
        time = (e2 - e1) / getTickFrequency()                   # CALCULATE TIME
        self.es.text_print.emit("\n[Done] Detect Mode: " +
                                "Process Finished in " + str(round(time, 3)) +
                                "s, " + "results saved to 'modules/runs/detect'.\n")
        if status_code == 0:
            self.es.message_box.emit("Success", "Success:\n\nProcess Finished in "
                                     + str(round(time, 3)) + "s.")
        else:
            self.es.message_box.emit("Warning",
                                     "Warning:\n\nAn Error Occurred During Process.\nProcess Finished in "
                                     + str(round(time, 3)) + "s.")
        len_of_dir = len(os.listdir(os.getcwd()+"/modules/runs/detect"))
        try:
            os.remove(os.getcwd()+"/modules/runs/detect/.DS_Store")
            os.remove(os.getcwd()+"/file_result/.DS_Store")
        except Exception as e:
            print(e)
        for i in range(len_of_dir):
            target = os.getcwd()+"/file_result/"
            if i == 0:
                ori_path = os.getcwd()+f"/modules/runs/detect/exp/"
            elif i != 0:
                ori_path = os.getcwd()+f"/modules/runs/detect/exp{i+1}/"
            file_list = os.listdir(ori_path)
            file_list = get_pure_list(file_list, "labels")
            if len(file_list) > 0:
                for file in file_list:
                    shutil.move(ori_path+file, target+file)
    
    # REPORT FUNCTIONS
    # ///////////////////////////////////////////////////////////////
    def handle_str_table(self, ls):
        for i in range(len(ls)):
            for j in range(len(ls[i])):
                ls[i][j] = int(ls[i][j])
        return ls

    def cal_frac(self, ls) -> None:
        frac = 0
        count = 0
        dam_cnt = 0
        dam_point = False
        len_ls = len(ls)
        if len_ls == 0:
            return None
        for i in ls:
            if i == 0:
                continue
            if i != 0:
                count += 1
            if i < 10 and i > 5:
                frac += 0.05
                continue
            if i > 10:
                dam_cnt += 1
                continue
        if dam_cnt/len_ls >= 0.02:
            dam_point = True
        frac += count/len_ls
        if frac >= 0.20 or dam_point is True:
            widgets.textBrowser_report.setMarkdown(f"### Generally Bad\n\
> The defective rate of the current batch is **{ls[-1]}%**, \
overall deviation has failed the testing standard;  \n\
> Seek the most defected class on the green section below.  \n\
### More details on this graph\n\
> Highest recorded deviation: **{round(max(ls), 2)}%**;  \n\
> Lowest recorded deviation: **{round(min(ls), 2)}%**;  \n\
> Average recorded deviation: **{round(sum(ls)/len_ls, 2)}%**.  \n")
        if frac > 0.10 and frac <= 0.20 and dam_point is False:
            widgets.textBrowser_report.setMarkdown(f"### Generally Average\n\
> The defective rate of the current batch is **{ls[-1]}%**, \
limited overall deviation but can still be improved;  \n\
> Seek the most defected class on the green section below.  \n\
### More details on this graph\n\
> Highest recorded deviation: **{round(max(ls), 2)}%**;  \n\
> Lowest recorded deviation: **{round(min(ls), 2)}%**;  \n\
> Average recorded deviation: **{round(sum(ls)/len_ls, 2)}%**.  \n")
        elif frac <= 0.10 and dam_point is False:
            widgets.textBrowser_report.setMarkdown(f"### Generally Good\n\
> The defective rate of the current batch is **{ls[-1]}%**, minimum deviation overall;  \n\
> Keep it on track;  \n\
> Predictions are given below.  \n\
### More details on this graph\n\
> Highest recorded deviation: **{round(max(ls), 2)}%**;  \n\
> Lowest recorded deviation: **{round(min(ls), 2)}%**;  \n\
> Average recorded deviation: **{round(sum(ls)/len_ls, 2)}%**.  \n")
        return None

    def cal_class(self, ls):
        if len(ls) == 0:
            return None
        cls_pool = [0,0,0]
        cl_mb = 0
        cl_cpu_fan = 0
        cl_fan_port = 0
        for i in range(1,len(ls)):
            for idx,j in enumerate(ls[i]):
                if idx == 0:
                    cl_mb += int(j)
                if idx == 1:
                    cl_cpu_fan += int(j)
                if idx == 2:
                    cl_fan_port += int(j)
        # comment on the res
        cls_pool[0]=cl_mb
        cls_pool[1]=cl_cpu_fan
        cls_pool[2]=cl_fan_port
        tmp_max = cls_pool.index(max(cls_pool))
        tmp_min = cls_pool.index(min(cls_pool))
        # return tmp_max,tmp_min
        l = ["Motherboard", "CPU_FAN", "FAN_Port"]
        widgets.def_total_text.setMarkdown(f"Overall, the highest yield is on {l[tmp_min]}  \n\
                                        Overall, the lowest yield is on {l[tmp_max]}")

    def cal_slope_intercept(self, ls)->list:
        x = []
        y = []
        for i,j in enumerate(ls):
            x.append(i)    
            y.append(j)
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
        return slope,intercept

    def prac_res_frac(self, slope,intercept,ls)->float:
        x_new = len(ls)
        y_new = slope*x_new+intercept
        if(y_new<0):
            y_new = 0
        if(y_new>100):
            y_new = 100
        if(y_new>=0 and y_new<=3):
            widgets.final_words.setText(f"The predicted value is {round(y_new,2)}%,\
                which is very profound.")
        elif(y_new>3 and y_new<=6):
            widgets.final_words.setText(f"The predicted value is {round(y_new,2)}%,\
                which is so-so.")
        elif(y_new>6):
            widgets.final_words.setText(f"The predicted value is {round(y_new,2)}%,\
                which is not good.")

    # DATABASE OPERATIONS
    # ///////////////////////////////////////////////////////////////
    def updateDataGraph(self):
        frac_d_n = self.handle_per(widgets.frac_defective.text())
        update_general_table(batch_num, frac_d_n)
        self.x_axis_batch = fetch_batch_num()
        self.y_axis_batch = self.handle_per_list(fecth_defective_data())
        self.cal_frac(self.y_axis_batch)
        self.cal_class(fetch_general_class())
        x, y = self.cal_slope_intercept(self.y_axis_batch)
        self.prac_res_frac(x, y, self.y_axis_batch)
        self.update_report_frac(self.x_axis_batch, self.y_axis_batch)
        self.update_table_report(fetch_general_class())
        delete_class_table()

    def update_table_report(self, ls):
        for i in range(1, len(ls)):
            for j in range(len(ls[i])):
                widgets.tableWidget_2.setItem(i, j, QTableWidgetItem(ls[i][j]))

    def handle_per(self, strwithper):  # for cloud side
        strx = strwithper.split("%", 1)[0]
        return float(strx)

    def update_report_frac(self, ls, list):
        self.curve2.setData(ls, list)

    def handle_per_list(self, ls) -> list:
        data = []
        for i in ls:
            i = i.split("%", 1)[0]
            data.append(float(i))
        return data

    def search_for_batch_results(self):
        search_string = widgets.search_box.text()
        self.x_axis_batch = fetch_limited_batch_num(search_string)
        self.y_axis_batch = self.handle_per_list(fetch_frac_limited(search_string))
        self.cal_frac(self.y_axis_batch)
        x,y = self.cal_slope_intercept(self.y_axis_batch)
        self.prac_res_frac(x,y,self.y_axis_batch)
        self.cal_class(fetch_general_class_limited(search_string))
        self.update_report_frac(self.x_axis_batch, self.y_axis_batch)
        widgets.tableWidget_2.clearContents()
        widgets.tableWidget_2.setItem(0, 0, QTableWidgetItem("Log Entry"))
        widgets.tableWidget_2.setItem(0, 1, QTableWidgetItem("Serial Number"))
        widgets.tableWidget_2.setItem(0, 2, QTableWidgetItem("Result Class"))
        widgets.tableWidget_2.setItem(0, 3, QTableWidgetItem("Notes"))
        self.update_table_report(fetch_general_class_limited(search_string))
    
    def sync_db(self):
        try:
            tran = paramiko.Transport(('124.223.101.237', 22))
            tran.connect(username="root", password='zzh_xyl_123')
            # 获取SFTP实例
            sftp = paramiko.SFTPClient.from_transport(tran)
            # 设置上传的本地/远程文件路径
            localpath = "./hsaois.db"
            remotepath = "/www/wwwroot/hsaois_server/app/hsaois.db"
            sftp.remove(remotepath)
            sftp.put(localpath, remotepath)
            tran.close()
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname='124.223.101.237', port=22, username='root', password='zzh_xyl_123')
            stdin, stdout, stderr = client.exec_command('chown www /www/wwwroot/hsaois_server/app/hsaois.db')
            client.close()
            widgets.btn_data_upload.setIcon(QIcon(":/icons/images/icons/cloud.svg"))
        except Exception as e:
            print(e)
            self.es.message_box.emit("Error", "Failed to synchronize database:\n\n" + str(e))


# CLASS FOR EMITTING SIGNALS
class EmitSignal(QObject):
    text_print = Signal(str)
    message_box = Signal(str, str)
    video = Signal(QImage)
    clear = Signal()
    stop = Signal()
    update_graph = Signal(list, int, float)
    update_table = Signal(list, int)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    app.setWindowIcon(QIcon("logo.png"))
    app.processEvents()
    window = MainWindow()
    time.sleep(1)
    splash.close()
    sys.exit(app.exec())
