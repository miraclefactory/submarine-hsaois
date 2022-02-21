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

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *

# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 18px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgb(112, 85, 151), stop:0.5 rgb(237, 237, 249));
        background-color: rgb(237, 237, 249);
        """

        # SET MANUAL STYLES
        # self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        # self.ui.pushButton.setStyleSheet("background-color: rgb(196, 183, 215);")
        # self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        # self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        # self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        # self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        # self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        # self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        # self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")
        self.ui.textBrowser.setStyleSheet(" border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 12pt;")
        self.ui.dash_frame_1.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 14pt; padding: 5px;")
        self.ui.dash_frame_2.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 14pt;padding: 5px;")
        self.ui.dash_frame_3.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 14pt; padding: 5px;")
        self.ui.dash_frame_4.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 14pt; padding: 5px;")
        self.ui.frame_2.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 12pt; padding: 5px;")
        self.ui.line_graph.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 12pt; padding: 8px;")
        self.ui.batch_number.setStyleSheet("color: #705597; font-weight: bold; font-size: 24pt;")
        self.ui.detected.setStyleSheet("color: #705597; font-weight: bold; font-size: 24pt;")
        self.ui.frac_defective.setStyleSheet("color: #705597; font-weight: bold; font-size: 24pt;")
        self.ui.most_defected.setStyleSheet("color: #705597; font-weight: bold; font-size: 24pt;")
        self.ui.label_5.setStyleSheet("color: #705597; font-weight: bold;")
        self.ui.label_7.setStyleSheet("color: #705597; font-weight: bold;")
        self.ui.btn_start_live.setStyleSheet("background-color: rgb(136, 112, 173); color: white;")
        self.ui.btn_stop_live.setStyleSheet("background-color: rgb(136, 112, 173); color: white;")
        self.ui.btn_scan.setStyleSheet("background-color: rgb(136, 112, 173); color: white;")
        self.ui.btn_start_file.setStyleSheet("background-color: rgb(136, 112, 173); color: white;")
        self.ui.btn_stop_file.setStyleSheet("background-color: rgb(136, 112, 173); color: white;")
        self.ui.btn_result.setStyleSheet("background-color: rgb(136, 112, 173); color: white;")
        self.ui.btn_file.setStyleSheet("background-color: rgb(136, 112, 173); color: white;")