# ///////////////////////////////////////////////////////////////
#
# BY: Miracle Factory
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
        self.ui.textBrowser.setStyleSheet("background-color: rgb(242, 242, 242); border: none; border-left: 1px rgb(230, 230, 230); font-size: 12px;")
        self.ui.dash_frame_1.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 14px; padding: 5px;")
        self.ui.dash_frame_2.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 14px;padding: 5px;")
        self.ui.dash_frame_3.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 14px; padding: 5px;")
        self.ui.dash_frame_4.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 14px; padding: 5px;")
        self.ui.frame_2.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 12px; padding: 5px;")
        self.ui.line_graph.setStyleSheet("border-radius: 5px; background-color: rgb(240, 240, 245); font-size: 12px; padding: 8px;")
        self.ui.batch_number.setStyleSheet("color: #705597; font-weight: bold; font-size: 24px;")
        self.ui.detected.setStyleSheet("color: #705597; font-weight: bold; font-size: 24px;")
        self.ui.frac_defective.setStyleSheet("color: #705597; font-weight: bold; font-size: 24px;")
        self.ui.most_defected.setStyleSheet("color: #705597; font-weight: bold; font-size: 24px;")
        self.ui.label_5.setStyleSheet("color: #705597; font-weight: bold;")
        self.ui.label_7.setStyleSheet("color: #705597; font-weight: bold;")
