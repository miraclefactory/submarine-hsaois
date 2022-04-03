# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 721)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1080, 660))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget\n"
"{\n"
"	color: #333;\n"
"	font: 10pt \"Arial\";\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	border: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"\n"
"QToolTip\n"
"{\n"
"	color: #333;\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(112, 85, 151);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"\n"
"#bgApp\n"
"{	\n"
"	background-color: rgb(2"
                        "50, 250, 250);\n"
"    color: #44475a;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"\n"
"#leftMenuBg\n"
"{\n"
"	background-color: rgb(237, 237, 249);\n"
"}\n"
"\n"
"#topLogoInfo\n"
"{\n"
"	background-color: rgb(237, 237, 249);\n"
"}\n"
"\n"
"#topLogo\n"
"{\n"
"	background-color: rgb(237, 237, 249);\n"
"	/* background-image: url(:/images/images/images/PyDracula.png); */\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"#titleLeftApp { font: 63 12pt \"Arial Semibold\"; color: gray; }\n"
"\n"
"#titleLeftDescription { font: 8pt \"Arial\"; color: #bd93f9; }\n"
"\n"
"/* MENUS */\n"
"\n"
"#topMenu .QPushButton\n"
"{	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 18px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 2px;\n"
"    color: rgb(112, 85, 151);\n"
"}\n"
"\n"
"#topMenu "
                        ".QPushButton:hover\n"
"{\n"
"	background-color: rgb(230, 230, 249);\n"
"}\n"
"\n"
"#topMenu .QPushButton:pressed\n"
"{	\n"
"	background-color: rgb(217, 217, 255);\n"
"}\n"
"\n"
"#bottomMenu .QPushButton\n"
"{	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 18px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 2px;\n"
"    color: rgb(112, 85, 151);\n"
"}\n"
"\n"
"#bottomMenu .QPushButton:hover\n"
"{\n"
"	background-color: rgb(230, 230, 249);\n"
"}\n"
"\n"
"#bottomMenu .QPushButton:pressed\n"
"{	\n"
"	background-color: rgb(217, 217, 255);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"\n"
"#toggleButton\n"
"{\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 18px solid transparent;\n"
"	background-color: rgb(237, 237, 249);\n"
"	text-align: left;\n"
"	padding-left: 0px;\n"
"	color: rgb(112, 85, 151);\n"
"}\n"
"\n"
"#toggleButton:hover\n"
"{\n"
""
                        "	background-color: rgb(230, 230, 249);\n"
"}\n"
"\n"
"#toggleButton:pressed\n"
"{	\n"
"	background-color: rgb(217, 217, 255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"\n"
"#extraLeftBox\n"
"{	\n"
"	background-color: rgb(214, 200, 242);\n"
"    color: #705597;\n"
"}\n"
"\n"
"#extraTopBg\n"
"{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon\n"
"{\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraClose"
                        "ColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"/* #extraContent\n"
"{\n"
"	border-top: 3px solid #6272a4;\n"
"} */\n"
"\n"
"/* Extra Top Menus */\n"
"\n"
"#extraTopMenu .QPushButton\n"
"{\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#extraTopMenu .QPushButton:hover\n"
"{\n"
"	background-color: #5d6c99;\n"
"}\n"
"\n"
"#extraTopMenu .QPushButton:pressed\n"
"{	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"\n"
"#contentTopBg\n"
"{	\n"
"	background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"#contentBottom\n"
"{\n"
"	border-top: 1px solid #eee;\n"
"}\n"
""
                        "\n"
"#titleRightInfo\n"
"{\n"
"    color: gray;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(240, 240, 240); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(220, 220, 220); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #495474; }\n"
"#themeSettingsTopDetail { background-color: #6272a4; }\n"
"\n"
"/* Bottom Bar */\n"
"/* #bottomBar { background-color: #495474 } */\n"
"#bottomBar { background-color: #705597; }\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"\n"
"/* MENUS */\n"
"\n"
"#contentSettings .QPushButton\n"
"{\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	borde"
                        "r-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#contentSettings .QPushButton:hover\n"
"{\n"
"	background-color: #5d6c99;\n"
"}\n"
"\n"
"#contentSettings .QPushButton:pressed\n"
"{	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"\n"
"QTableWidget\n"
"{	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	/* gridline-color: #9faeda; */\n"
"	gridline-color: rgb(210, 188, 226);\n"
"    outline: none;\n"
"}\n"
"\n"
"QTableWidget::item\n"
"{\n"
"	border-color: rgb(210, 188, 226);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(210, 188, 226);\n"
"}\n"
"\n"
"QTableWidget::item:selected\n"
"{\n"
"	background-color: rgb(240, 240, 245);\n"
"    color: #705597;\n"
"	font-weight: bold;\n"
"}\n"
""
                        "\n"
"QHeaderView::section\n"
"{\n"
"	background-color: #6272a4;\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader\n"
"{	\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"	background-color: #6272a4;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #705597;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"\n"
"QLineEdit\n"
"{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(136, 112, 173);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #d8b7ff;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px "
                        "solid #ab90d1;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #d8b7ff;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"QPlainTextEdit  QScrollBar:vertical\n"
"{\n"
"    width: 8px;\n"
"}\n"
"\n"
"QPlainTextEdit  QScrollBar:horizontal\n"
"{\n"
"    height: 8px;\n"
"}\n"
"\n"
"QPlainTextEdit:hover\n"
"{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"QPlainTextEdit:focus\n"
"{\n"
"	border: 2px solid #bd93f9;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: none;\n"
"    background: rgb(136, 112, 173);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    backgr"
                        "ound: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border: none;\n"
"    background: rgb(136, 112, 173);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: none;\n"
"    background: rgb(136, 112, 173);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"	border: none;\n"
"    background-color: rgb(136, 112, 173);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
""
                        "	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: none;\n"
"    background: rgb(136, 112, 173);\n"
"    height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"	border: none;\n"
"    background: rgb(136, 112, 173);\n"
"    height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////"
                        "////////////////////////\n"
"CheckBox */\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover\n"
"{\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"}\n"
"\n"
""
                        "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"\n"
"QComboBox\n"
"{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"QComboBox:hover\n"
"{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: #6272a4;\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"\n"
"/* ////////////////////////"
                        "/////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"\n"
"QSlider::groove:horizontal\n"
"{\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"QSlider::groove:horizontal:hover\n"
"{\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"QSlider::handle:horizontal\n"
"{\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover\n"
"{\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed\n"
"{\n"
"    background-color: rgb(217, 217, 255);\n"
"}\n"
"\n"
"QSlider::groove:vertical\n"
"{\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"QSlider::groove:vertical:hover\n"
"{\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"QSlider::handle:vertical\n"
"{\n"
"    background-colo"
                        "r: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover\n"
"{\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"\n"
"QSlider::handle:vertical:pressed\n"
"{\n"
"    background-color: rgb(217, 217, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"\n"
"#pagesContainer QCommandLinkButton\n"
"{	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"    border: 2px solid #ff79c6;\n"
"    color: #ff79c6;\n"
"}\n"
"\n"
"#pagesContainer QCommandLinkButton:hover\n"
"{	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"#pagesContainer QCommandLinkButton:pressed\n"
"{	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: #586796;\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////"
                        "//\n"
"Button */\n"
"\n"
"#pagesContainer QPushButton\n"
"{\n"
"	border: 2px solid rgb(136, 112, 173);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(136, 112, 173);\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#pagesContainer QPushButton:hover\n"
"{\n"
"	background-color: rgb(179, 162, 204);\n"
"	border: 2px solid #705597;\n"
"}\n"
"\n"
"#pagesContainer QPushButton:pressed\n"
"{\n"
"	border: 2px solid #d8b7ff;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"TabWidget */\n"
"\n"
"/* QTabWidget::tab-bar {\n"
"	background-color: black;\n"
"} */\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    background-color: white;\n"
"    border-color: gray;\n"
"    font: 10px 'Arial';\n"
"    color: gray;\n"
"    height: 20px;\n"
"	padding-right: 15px;\n"
"	padding-left: 15px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first\n"
"{\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
""
                        "{\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    background-color: rgb(211, 200, 227);\n"
"    color: gray;\n"
"}\n"
"\n"
"QTabBar::close-button\n"
"{\n"
"    background-position: center;\n"
"    /* background-image: url(\":/Appearance/close_chat_item\"); */\n"
"}\n"
"\n"
"/* QTabWidget::pane\n"
"{ \n"
"    position: absolute;\n"
"} */\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-color: rgb(136, 112, 173);\n"
"    background-color: rgb(136, 112, 173);\n"
"    color: white;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ProgressBar */\n"
"\n"
"QProgressBar\n"
"{\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"	border-radius: 1px;\n"
"	width: 5px;\n"
"	margin: 1px;\n"
"}\n"
"\n"
"#progressBar_1::chunk\n"
"{\n"
"	background-color: #705597;\n"
"}\n"
"\n"
"#progressBar_2::chunk\n"
"{\n"
"	background-color: #927bb3;\n"
"}\n"
"\n"
"#progres"
                        "sBar_3::chunk\n"
"{\n"
"	background-color: #b194da;\n"
"}\n"
"\n"
"")
        self.splitter_4 = QSplitter(self.styleSheet)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(0, 0, 0, 0))
        self.splitter_4.setOrientation(Qt.Vertical)
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Arial Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_detect_2 = QPushButton(self.topLogoInfo)
        self.btn_detect_2.setObjectName(u"btn_detect_2")
        self.btn_detect_2.setGeometry(QRect(0, 0, 60, 51))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_detect_2.sizePolicy().hasHeightForWidth())
        self.btn_detect_2.setSizePolicy(sizePolicy1)
        self.btn_detect_2.setMinimumSize(QSize(0, 45))
        self.btn_detect_2.setFont(font)
        self.btn_detect_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_detect_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_detect_2.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon = QIcon()
        icon.addFile(u":/images/images/images/5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_detect_2.setIcon(icon)
        self.btn_detect_2.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleButton.setIcon(icon1)
        self.toggleButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/home-alt2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon2)
        self.btn_home.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_detect = QPushButton(self.topMenu)
        self.btn_detect.setObjectName(u"btn_detect")
        sizePolicy1.setHeightForWidth(self.btn_detect.sizePolicy().hasHeightForWidth())
        self.btn_detect.setSizePolicy(sizePolicy1)
        self.btn_detect.setMinimumSize(QSize(0, 45))
        self.btn_detect.setFont(font)
        self.btn_detect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_detect.setLayoutDirection(Qt.LeftToRight)
        self.btn_detect.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_detect.setIcon(icon3)
        self.btn_detect.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.btn_detect)

        self.btn_dash = QPushButton(self.topMenu)
        self.btn_dash.setObjectName(u"btn_dash")
        sizePolicy1.setHeightForWidth(self.btn_dash.sizePolicy().hasHeightForWidth())
        self.btn_dash.setSizePolicy(sizePolicy1)
        self.btn_dash.setMinimumSize(QSize(0, 45))
        self.btn_dash.setFont(font)
        self.btn_dash.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dash.setLayoutDirection(Qt.LeftToRight)
        self.btn_dash.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dash.setIcon(icon4)
        self.btn_dash.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.btn_dash)

        self.btn_report = QPushButton(self.topMenu)
        self.btn_report.setObjectName(u"btn_report")
        sizePolicy1.setHeightForWidth(self.btn_report.sizePolicy().hasHeightForWidth())
        self.btn_report.setSizePolicy(sizePolicy1)
        self.btn_report.setMinimumSize(QSize(0, 45))
        self.btn_report.setFont(font)
        self.btn_report.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_report.setLayoutDirection(Qt.LeftToRight)
        self.btn_report.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report.setIcon(icon5)
        self.btn_report.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.btn_report)

        self.btn_train = QPushButton(self.topMenu)
        self.btn_train.setObjectName(u"btn_train")
        sizePolicy1.setHeightForWidth(self.btn_train.sizePolicy().hasHeightForWidth())
        self.btn_train.setSizePolicy(sizePolicy1)
        self.btn_train.setMinimumSize(QSize(0, 45))
        self.btn_train.setFont(font)
        self.btn_train.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_train.setLayoutDirection(Qt.LeftToRight)
        self.btn_train.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/fit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_train.setIcon(icon6)
        self.btn_train.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.btn_train)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/ellypsis.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleLeftBox.setIcon(icon7)
        self.toggleLeftBox.setIconSize(QSize(20, 20))

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon8)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy1.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy1)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy1.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy1)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.contentTopBg.sizePolicy().hasHeightForWidth())
        self.contentTopBg.setSizePolicy(sizePolicy2)
        self.contentTopBg.setMinimumSize(QSize(0, 28))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy3)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(10)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy4)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        self.label_15 = QLabel(self.leftBox)
        self.label_15.setObjectName(u"label_15")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy5)
        self.label_15.setStyleSheet(u"color: rgb(96, 96, 96);")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_15.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_15)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_start_live = QPushButton(self.rightButtons)
        self.top_start_live.setObjectName(u"top_start_live")
        self.top_start_live.setMinimumSize(QSize(28, 28))
        self.top_start_live.setStyleSheet(u"border-radius: 5px;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.top_start_live.setIcon(icon9)

        self.horizontalLayout_2.addWidget(self.top_start_live)

        self.top_stop_live = QPushButton(self.rightButtons)
        self.top_stop_live.setObjectName(u"top_stop_live")
        self.top_stop_live.setMinimumSize(QSize(28, 28))
        self.top_stop_live.setStyleSheet(u"border-radius: 5px;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/rectangle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.top_stop_live.setIcon(icon10)

        self.horizontalLayout_2.addWidget(self.top_stop_live)

        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon11)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon12)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon13)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon8)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.horizontalLayout_30 = QHBoxLayout(self.home)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.home_logo = QPushButton(self.home)
        self.home_logo.setObjectName(u"home_logo")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.home_logo.sizePolicy().hasHeightForWidth())
        self.home_logo.setSizePolicy(sizePolicy6)
        self.home_logo.setStyleSheet(u"border: none;")
        icon14 = QIcon()
        icon14.addFile(u":/images/images/images/6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_logo.setIcon(icon14)
        self.home_logo.setIconSize(QSize(100, 100))

        self.horizontalLayout_25.addWidget(self.home_logo)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setSpacing(5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 10, -1, 10)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_4)

        self.home_logo_line = QLabel(self.home)
        self.home_logo_line.setObjectName(u"home_logo_line")
        self.home_logo_line.setStyleSheet(u"font-size: 40pt;\n"
"font-weight: 600;\n"
"color: rgb(150, 150, 150);")
        self.home_logo_line.setScaledContents(False)
        self.home_logo_line.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_29.addWidget(self.home_logo_line)

        self.home_logo_line2 = QLabel(self.home)
        self.home_logo_line2.setObjectName(u"home_logo_line2")
        self.home_logo_line2.setStyleSheet(u"font-size: 20pt;\n"
"font-weight: 500;\n"
"color: rgb(170,170,170);")
        self.home_logo_line2.setScaledContents(False)
        self.home_logo_line2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_29.addWidget(self.home_logo_line2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_3)


        self.horizontalLayout_25.addLayout(self.verticalLayout_29)


        self.horizontalLayout_27.addLayout(self.horizontalLayout_25)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_5)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(15)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_5)

        self.label_13 = QLabel(self.home)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(100, 100, 100);")

        self.verticalLayout_30.addWidget(self.label_13)

        self.label_11 = QLabel(self.home)
        self.label_11.setObjectName(u"label_11")
        sizePolicy5.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy5)
        self.label_11.setStyleSheet(u"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-left: 2px solid rgb(112, 85, 151);\n"
"background-color: rgb(237, 237, 249);\n"
"font-size: 12pt;\n"
"padding: 12px;")

        self.verticalLayout_30.addWidget(self.label_11)

        self.label_12 = QLabel(self.home)
        self.label_12.setObjectName(u"label_12")
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)
        self.label_12.setStyleSheet(u"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-left: 2px solid rgb(112, 85, 151);\n"
"background-color: rgb(237, 237, 249);\n"
"font-size: 12pt;\n"
"padding: 12px;")

        self.verticalLayout_30.addWidget(self.label_12)

        self.label_9 = QLabel(self.home)
        self.label_9.setObjectName(u"label_9")
        sizePolicy5.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy5)
        self.label_9.setStyleSheet(u"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-left: 2px solid rgb(112, 85, 151);\n"
"background-color: rgb(237, 237, 249);\n"
"font-size: 12pt;\n"
"padding: 12px;")

        self.verticalLayout_30.addWidget(self.label_9)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_6)


        self.horizontalLayout_27.addLayout(self.verticalLayout_30)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_6)


        self.verticalLayout_31.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.video_tu = QPushButton(self.home)
        self.video_tu.setObjectName(u"video_tu")
        sizePolicy6.setHeightForWidth(self.video_tu.sizePolicy().hasHeightForWidth())
        self.video_tu.setSizePolicy(sizePolicy6)
        self.video_tu.setMinimumSize(QSize(120, 32))
        self.video_tu.setStyleSheet(u"color: #555;\n"
"font-size: 12pt;\n"
"border: 1px solid rgb(220, 220, 220);\n"
"background-color: rgb(248, 248, 255);")
        self.video_tu.setIcon(icon9)

        self.horizontalLayout_28.addWidget(self.video_tu)


        self.verticalLayout_31.addLayout(self.horizontalLayout_28)


        self.horizontalLayout_30.addLayout(self.verticalLayout_31)

        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.horizontalLayout_6 = QHBoxLayout(self.widgets)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.splitter_3 = QSplitter(self.widgets)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.splitter_3.setHandleWidth(5)
        self.tabWidget = QTabWidget(self.splitter_3)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy7)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.live = QWidget()
        self.live.setObjectName(u"live")
        self.horizontalLayout_7 = QHBoxLayout(self.live)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.splitter = QSplitter(self.live)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(5)
        self.video_viewer = QLabel(self.splitter)
        self.video_viewer.setObjectName(u"video_viewer")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.video_viewer.sizePolicy().hasHeightForWidth())
        self.video_viewer.setSizePolicy(sizePolicy8)
        self.video_viewer.setMinimumSize(QSize(100, 100))
        self.video_viewer.setAutoFillBackground(False)
        self.video_viewer.setStyleSheet(u"border: 1px solid rgb(220, 220, 220);\n"
"border-radius: 5px;\n"
"background-color: rgb(233, 233, 233);\n"
"")
        self.video_viewer.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.video_viewer)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 5, 0, 0)
        self.btn_start_live = QPushButton(self.layoutWidget)
        self.btn_start_live.setObjectName(u"btn_start_live")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(2)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.btn_start_live.sizePolicy().hasHeightForWidth())
        self.btn_start_live.setSizePolicy(sizePolicy9)
        self.btn_start_live.setMinimumSize(QSize(110, 40))
        self.btn_start_live.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_live.setStyleSheet(u"background-color: rgb(136, 112, 173);\n"
"\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/play_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start_live.setIcon(icon15)
        self.btn_start_live.setFlat(False)

        self.horizontalLayout_11.addWidget(self.btn_start_live)

        self.btn_stop_live = QPushButton(self.layoutWidget)
        self.btn_stop_live.setObjectName(u"btn_stop_live")
        sizePolicy9.setHeightForWidth(self.btn_stop_live.sizePolicy().hasHeightForWidth())
        self.btn_stop_live.setSizePolicy(sizePolicy9)
        self.btn_stop_live.setMinimumSize(QSize(110, 40))
        self.btn_stop_live.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop_live.setStyleSheet(u"background-color: rgb(136, 112, 173);\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/rectangle_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stop_live.setIcon(icon16)
        self.btn_stop_live.setFlat(False)

        self.horizontalLayout_11.addWidget(self.btn_stop_live)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        sizePolicy10 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy10)
        self.line.setMinimumSize(QSize(1, 40))
        self.line.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line)

        self.btn_scan = QPushButton(self.layoutWidget)
        self.btn_scan.setObjectName(u"btn_scan")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(1)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.btn_scan.sizePolicy().hasHeightForWidth())
        self.btn_scan.setSizePolicy(sizePolicy11)
        self.btn_scan.setMinimumSize(QSize(110, 40))
        self.btn_scan.setStyleSheet(u"background-color: rgb(136, 112, 173);\n"
"")
        icon17 = QIcon()
        icon17.addFile(u":/icons/images/icons/aperture_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_scan.setIcon(icon17)

        self.horizontalLayout_11.addWidget(self.btn_scan)

        self.btn_update = QPushButton(self.layoutWidget)
        self.btn_update.setObjectName(u"btn_update")
        sizePolicy11.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy11)
        self.btn_update.setMinimumSize(QSize(110, 40))
        self.btn_update.setStyleSheet(u"background-color: rgb(136, 112, 173);\n"
"")
        icon18 = QIcon()
        icon18.addFile(u":/icons/images/icons/cil-data-transfer-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update.setIcon(icon18)

        self.horizontalLayout_11.addWidget(self.btn_update)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.splitter.addWidget(self.layoutWidget)

        self.horizontalLayout_7.addWidget(self.splitter)

        self.tabWidget.addTab(self.live, "")
        self.file = QWidget()
        self.file.setObjectName(u"file")
        self.horizontalLayout_9 = QHBoxLayout(self.file)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.splitter_2 = QSplitter(self.file)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter_2.setHandleWidth(5)
        self.upload = QWidget(self.splitter_2)
        self.upload.setObjectName(u"upload")
        sizePolicy8.setHeightForWidth(self.upload.sizePolicy().hasHeightForWidth())
        self.upload.setSizePolicy(sizePolicy8)
        self.upload.setMinimumSize(QSize(0, 0))
        self.upload.setAcceptDrops(True)
        self.upload.setStyleSheet(u"border: 2px dashed rgb(220, 220, 220);\n"
"border-radius: 5px;")
        self.horizontalLayout_29 = QHBoxLayout(self.upload)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.btn_file = QPushButton(self.upload)
        self.btn_file.setObjectName(u"btn_file")
        sizePolicy6.setHeightForWidth(self.btn_file.sizePolicy().hasHeightForWidth())
        self.btn_file.setSizePolicy(sizePolicy6)
        self.btn_file.setMinimumSize(QSize(110, 35))
        self.btn_file.setAcceptDrops(False)
        self.btn_file.setStyleSheet(u"background-color: rgb(136, 112, 173);\n"
"border: none;")
        icon19 = QIcon()
        icon19.addFile(u":/icons/images/icons/folder-add_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_file.setIcon(icon19)

        self.horizontalLayout_29.addWidget(self.btn_file)

        self.splitter_2.addWidget(self.upload)
        self.layoutWidget1 = QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 5, 0, 0)
        self.btn_start_file = QPushButton(self.layoutWidget1)
        self.btn_start_file.setObjectName(u"btn_start_file")
        sizePolicy9.setHeightForWidth(self.btn_start_file.sizePolicy().hasHeightForWidth())
        self.btn_start_file.setSizePolicy(sizePolicy9)
        self.btn_start_file.setMinimumSize(QSize(110, 40))
        self.btn_start_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_file.setStyleSheet(u"background-color: rgb(136, 112, 173);")
        self.btn_start_file.setIcon(icon15)
        self.btn_start_file.setFlat(False)

        self.horizontalLayout_8.addWidget(self.btn_start_file)

        self.btn_stop_file = QPushButton(self.layoutWidget1)
        self.btn_stop_file.setObjectName(u"btn_stop_file")
        sizePolicy9.setHeightForWidth(self.btn_stop_file.sizePolicy().hasHeightForWidth())
        self.btn_stop_file.setSizePolicy(sizePolicy9)
        self.btn_stop_file.setMinimumSize(QSize(110, 40))
        self.btn_stop_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop_file.setStyleSheet(u"background-color: rgb(136, 112, 173);")
        self.btn_stop_file.setIcon(icon16)
        self.btn_stop_file.setFlat(False)

        self.horizontalLayout_8.addWidget(self.btn_stop_file)

        self.line_2 = QFrame(self.layoutWidget1)
        self.line_2.setObjectName(u"line_2")
        sizePolicy10.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy10)
        self.line_2.setMinimumSize(QSize(1, 40))
        self.line_2.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_2)

        self.btn_result = QPushButton(self.layoutWidget1)
        self.btn_result.setObjectName(u"btn_result")
        sizePolicy11.setHeightForWidth(self.btn_result.sizePolicy().hasHeightForWidth())
        self.btn_result.setSizePolicy(sizePolicy11)
        self.btn_result.setMinimumSize(QSize(110, 40))
        self.btn_result.setStyleSheet(u"background-color: rgb(136, 112, 173);")
        icon20 = QIcon()
        icon20.addFile(u":/icons/images/icons/image_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_result.setIcon(icon20)

        self.horizontalLayout_8.addWidget(self.btn_result)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.splitter_2.addWidget(self.layoutWidget1)

        self.horizontalLayout_9.addWidget(self.splitter_2)

        self.tabWidget.addTab(self.file, "")
        self.splitter_3.addWidget(self.tabWidget)
        self.layoutWidget2 = QWidget(self.splitter_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy12)
        self.label_14.setMinimumSize(QSize(180, 25))
        self.label_14.setMaximumSize(QSize(400, 16777215))
        self.label_14.setStyleSheet(u"background-color: rgb(237, 232, 239);\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"color: rgb(96, 96, 96);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_14)

        self.textBrowser = QTextBrowser(self.layoutWidget2)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy13 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy13)
        self.textBrowser.setMinimumSize(QSize(180, 0))
        self.textBrowser.setMaximumSize(QSize(400, 16777215))
        self.textBrowser.setStyleSheet(u"background-color: rgb(242, 242, 242);\n"
"border: none;\n"
"border-left: 1px rgb(230, 230, 230);\n"
"font-size: 12pt;")

        self.verticalLayout_22.addWidget(self.textBrowser)

        self.splitter_3.addWidget(self.layoutWidget2)

        self.horizontalLayout_6.addWidget(self.splitter_3)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_21 = QVBoxLayout(self.new_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.row_1 = QFrame(self.new_page)
        self.row_1.setObjectName(u"row_1")
        sizePolicy14 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(2)
        sizePolicy14.setHeightForWidth(self.row_1.sizePolicy().hasHeightForWidth())
        self.row_1.setSizePolicy(sizePolicy14)
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        sizePolicy2.setHeightForWidth(self.frame_div_content_1.sizePolicy().hasHeightForWidth())
        self.frame_div_content_1.setSizePolicy(sizePolicy2)
        self.frame_div_content_1.setMinimumSize(QSize(0, 0))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_div_content_1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.dash_frame_1 = QFrame(self.frame_div_content_1)
        self.dash_frame_1.setObjectName(u"dash_frame_1")
        sizePolicy5.setHeightForWidth(self.dash_frame_1.sizePolicy().hasHeightForWidth())
        self.dash_frame_1.setSizePolicy(sizePolicy5)
        self.dash_frame_1.setStyleSheet(u"background-color: rgb(229, 229, 237);\n"
"border: 1px rgb(179, 181, 183) solid;\n"
"border-radius: 5px;\n"
"font-size: 14pt;\n"
"font-weight: bold;\n"
"padding: 8px;\n"
"")
        self.dash_frame_1.setFrameShape(QFrame.StyledPanel)
        self.dash_frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.dash_frame_1)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_4 = QLabel(self.dash_frame_1)
        self.label_4.setObjectName(u"label_4")
        sizePolicy15 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy15)
        self.label_4.setMinimumSize(QSize(0, 26))
        self.label_4.setStyleSheet(u"font-size: 12pt;\n"
"font-weight: normal;")

        self.verticalLayout_20.addWidget(self.label_4)

        self.batch_number = QLabel(self.dash_frame_1)
        self.batch_number.setObjectName(u"batch_number")
        sizePolicy2.setHeightForWidth(self.batch_number.sizePolicy().hasHeightForWidth())
        self.batch_number.setSizePolicy(sizePolicy2)
        self.batch_number.setStyleSheet(u"font-size: 22pt;")
        self.batch_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_20.addWidget(self.batch_number)


        self.horizontalLayout_16.addLayout(self.verticalLayout_20)


        self.horizontalLayout_10.addWidget(self.dash_frame_1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.dash_frame_2 = QFrame(self.frame_div_content_1)
        self.dash_frame_2.setObjectName(u"dash_frame_2")
        sizePolicy5.setHeightForWidth(self.dash_frame_2.sizePolicy().hasHeightForWidth())
        self.dash_frame_2.setSizePolicy(sizePolicy5)
        self.dash_frame_2.setStyleSheet(u"background-color: rgb(229, 229, 237);\n"
"border: 1px rgb(179, 181, 183) solid;\n"
"border-radius: 5px;\n"
"font-size: 14pt;\n"
"font-weight: bold;\n"
"padding: 8px;\n"
"")
        self.dash_frame_2.setFrameShape(QFrame.StyledPanel)
        self.dash_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.dash_frame_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_6 = QLabel(self.dash_frame_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy15.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy15)
        self.label_6.setMinimumSize(QSize(0, 26))
        self.label_6.setStyleSheet(u"font-size: 12pt;\n"
"font-weight: normal;")

        self.verticalLayout_23.addWidget(self.label_6)

        self.detected = QLabel(self.dash_frame_2)
        self.detected.setObjectName(u"detected")
        sizePolicy2.setHeightForWidth(self.detected.sizePolicy().hasHeightForWidth())
        self.detected.setSizePolicy(sizePolicy2)
        self.detected.setStyleSheet(u"font-size: 22pt;")
        self.detected.setFrameShape(QFrame.NoFrame)
        self.detected.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_23.addWidget(self.detected)


        self.horizontalLayout_17.addLayout(self.verticalLayout_23)


        self.horizontalLayout_10.addWidget(self.dash_frame_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.dash_frame_3 = QFrame(self.frame_div_content_1)
        self.dash_frame_3.setObjectName(u"dash_frame_3")
        sizePolicy5.setHeightForWidth(self.dash_frame_3.sizePolicy().hasHeightForWidth())
        self.dash_frame_3.setSizePolicy(sizePolicy5)
        self.dash_frame_3.setStyleSheet(u"background-color: rgb(229, 229, 237);\n"
"border: 1px rgb(179, 181, 183) solid;\n"
"border-radius: 5px;\n"
"font-size: 14pt;\n"
"font-weight: bold;\n"
"padding: 8px;\n"
"")
        self.dash_frame_3.setFrameShape(QFrame.StyledPanel)
        self.dash_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.dash_frame_3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_8 = QLabel(self.dash_frame_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy15.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy15)
        self.label_8.setMinimumSize(QSize(0, 26))
        self.label_8.setStyleSheet(u"font-size: 12pt;\n"
"font-weight: normal;")

        self.verticalLayout_25.addWidget(self.label_8)

        self.frac_defective = QLabel(self.dash_frame_3)
        self.frac_defective.setObjectName(u"frac_defective")
        sizePolicy2.setHeightForWidth(self.frac_defective.sizePolicy().hasHeightForWidth())
        self.frac_defective.setSizePolicy(sizePolicy2)
        self.frac_defective.setStyleSheet(u"font-size: 22pt;")
        self.frac_defective.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.frac_defective)


        self.horizontalLayout_18.addLayout(self.verticalLayout_25)


        self.horizontalLayout_10.addWidget(self.dash_frame_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.dash_frame_4 = QFrame(self.frame_div_content_1)
        self.dash_frame_4.setObjectName(u"dash_frame_4")
        sizePolicy5.setHeightForWidth(self.dash_frame_4.sizePolicy().hasHeightForWidth())
        self.dash_frame_4.setSizePolicy(sizePolicy5)
        self.dash_frame_4.setStyleSheet(u"background-color: rgb(229, 229, 237);\n"
"border: 1px rgb(179, 181, 183) solid;\n"
"border-radius: 5px;\n"
"font-size: 14pt;\n"
"font-weight: bold;\n"
"padding: 8px;\n"
"")
        self.dash_frame_4.setFrameShape(QFrame.StyledPanel)
        self.dash_frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.dash_frame_4)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_10 = QLabel(self.dash_frame_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy15.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy15)
        self.label_10.setMinimumSize(QSize(0, 26))
        self.label_10.setStyleSheet(u"font-size: 12pt;\n"
"font-weight: normal;")

        self.verticalLayout_26.addWidget(self.label_10)

        self.most_defected = QLabel(self.dash_frame_4)
        self.most_defected.setObjectName(u"most_defected")
        sizePolicy2.setHeightForWidth(self.most_defected.sizePolicy().hasHeightForWidth())
        self.most_defected.setSizePolicy(sizePolicy2)
        self.most_defected.setStyleSheet(u"font-size: 22pt;")
        self.most_defected.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.most_defected)


        self.horizontalLayout_19.addLayout(self.verticalLayout_26)


        self.horizontalLayout_10.addWidget(self.dash_frame_4)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout_21.addWidget(self.row_1)

        self.frame = QFrame(self.new_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.line_graph = PlotWidget(self.frame)
        self.line_graph.setObjectName(u"line_graph")
        sizePolicy5.setHeightForWidth(self.line_graph.sizePolicy().hasHeightForWidth())
        self.line_graph.setSizePolicy(sizePolicy5)
        self.line_graph.setStyleSheet(u"background-color: rgb(229, 229, 237);\n"
"border: 1px rgb(179, 181, 183) solid;\n"
"border-radius: 5px;\n"
"font-size: 14pt;\n"
"font-weight: bold;\n"
"padding: 8px;")

        self.horizontalLayout_13.addWidget(self.line_graph)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy5.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy5)
        self.frame_2.setMinimumSize(QSize(0, 200))
        self.frame_2.setStyleSheet(u"background-color: rgb(229, 229, 237);\n"
"border: 1px rgb(179, 181, 183) solid;\n"
"border-radius: 5px;\n"
"font-size: 14pt;\n"
"font-weight: bold;\n"
"padding: 8px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(0, 10))

        self.horizontalLayout_12.addWidget(self.label_5)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.label_7)


        self.verticalLayout_28.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_17.addWidget(self.label)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_17.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_17.addWidget(self.label_3)


        self.horizontalLayout_15.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.progressBar_1 = QProgressBar(self.frame_2)
        self.progressBar_1.setObjectName(u"progressBar_1")
        self.progressBar_1.setMaximum(20)
        self.progressBar_1.setValue(15)
        self.progressBar_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_18.addWidget(self.progressBar_1)

        self.progressBar_2 = QProgressBar(self.frame_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMaximum(20)
        self.progressBar_2.setValue(10)
        self.progressBar_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_18.addWidget(self.progressBar_2)

        self.progressBar_3 = QProgressBar(self.frame_2)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setMaximum(20)
        self.progressBar_3.setValue(5)
        self.progressBar_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_18.addWidget(self.progressBar_3)


        self.horizontalLayout_15.addLayout(self.verticalLayout_18)


        self.verticalLayout_28.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_24.addLayout(self.verticalLayout_28)


        self.horizontalLayout_13.addWidget(self.frame_2)


        self.verticalLayout_21.addWidget(self.frame)

        self.row_4 = QFrame(self.new_page)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setMinimumSize(QSize(0, 150))
        self.row_4.setFrameShape(QFrame.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.row_4)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_4)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 20):
            self.tableWidget.setRowCount(20)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy16 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy16)
        palette = QPalette()
        brush = QBrush(QColor(51, 51, 51, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 255))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(20)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_14.addWidget(self.tableWidget)


        self.verticalLayout_21.addWidget(self.row_4)

        self.stackedWidget.addWidget(self.new_page)
        self.report = QWidget()
        self.report.setObjectName(u"report")
        self.horizontalLayout_23 = QHBoxLayout(self.report)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(25)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.search_box = QLineEdit(self.report)
        self.search_box.setObjectName(u"search_box")
        sizePolicy17 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.search_box.sizePolicy().hasHeightForWidth())
        self.search_box.setSizePolicy(sizePolicy17)
        self.search_box.setMinimumSize(QSize(0, 40))
        self.search_box.setStyleSheet(u"color: rgb(90,90,90);\n"
"font-size: 12pt;\n"
"font-style: italic;\n"
"")

        self.horizontalLayout_22.addWidget(self.search_box)

        self.btn_search = QPushButton(self.report)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy9.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy9)
        self.btn_search.setMinimumSize(QSize(40, 40))
        self.btn_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search.setStyleSheet(u"background-color: rgb(136, 112, 173); \n"
"color: white;\n"
"border-radius: 8px;")
        icon21 = QIcon()
        icon21.addFile(u":/icons/images/icons/search_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon21)
        self.btn_search.setFlat(False)

        self.horizontalLayout_22.addWidget(self.btn_search)

        self.btn_save = QPushButton(self.report)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy9.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy9)
        self.btn_save.setMinimumSize(QSize(120, 40))
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setStyleSheet(u"background-color: rgb(136, 112, 173); \n"
"color: white;\n"
"border-radius: 8px;")
        icon22 = QIcon()
        icon22.addFile(u":/icons/images/icons/download_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon22)
        self.btn_save.setFlat(False)

        self.horizontalLayout_22.addWidget(self.btn_save)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_7)

        self.btn_question = QPushButton(self.report)
        self.btn_question.setObjectName(u"btn_question")
        sizePolicy9.setHeightForWidth(self.btn_question.sizePolicy().hasHeightForWidth())
        self.btn_question.setSizePolicy(sizePolicy9)
        self.btn_question.setMinimumSize(QSize(40, 40))
        self.btn_question.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_question.setStyleSheet(u"background-color: rgb(136, 112, 173); \n"
"color: white;\n"
"font-size: 16pt;\n"
"border-radius: 20px;")
        self.btn_question.setFlat(False)

        self.horizontalLayout_22.addWidget(self.btn_question)


        self.verticalLayout_27.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.batch_data_graph = PlotWidget(self.report)
        self.batch_data_graph.setObjectName(u"batch_data_graph")
        sizePolicy18 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy18.setHorizontalStretch(2)
        sizePolicy18.setVerticalStretch(1)
        sizePolicy18.setHeightForWidth(self.batch_data_graph.sizePolicy().hasHeightForWidth())
        self.batch_data_graph.setSizePolicy(sizePolicy18)
        self.batch_data_graph.setStyleSheet(u"background-color: rgb(240, 240, 245);\n"
"border-radius: 5px;\n"
"font-size: 14pt;\n"
"font-weight: normal;\n"
"padding: 8px;")

        self.horizontalLayout_20.addWidget(self.batch_data_graph)

        self.textBrowser_report = QTextBrowser(self.report)
        self.textBrowser_report.setObjectName(u"textBrowser_report")
        sizePolicy19 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy19.setHorizontalStretch(1)
        sizePolicy19.setVerticalStretch(1)
        sizePolicy19.setHeightForWidth(self.textBrowser_report.sizePolicy().hasHeightForWidth())
        self.textBrowser_report.setSizePolicy(sizePolicy19)
        self.textBrowser_report.setStyleSheet(u"background-color: rgb(240, 240, 245);\n"
"border-radius: 5px;\n"
"font-size: 14pt;\n"
"font-weight: normal;\n"
"padding: 8px;")

        self.horizontalLayout_20.addWidget(self.textBrowser_report)


        self.verticalLayout_27.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.def_total_table = QFrame(self.report)
        self.def_total_table.setObjectName(u"def_total_table")
        sizePolicy.setHeightForWidth(self.def_total_table.sizePolicy().hasHeightForWidth())
        self.def_total_table.setSizePolicy(sizePolicy)
        self.def_total_table.setStyleSheet(u"background-color: rgb(240, 240, 245);\n"
"border-radius: 5px;\n"
"font-size: 14pt;\n"
"font-weight: normal;\n"
"padding: 8px;")
        self.def_total_table.setFrameShape(QFrame.StyledPanel)
        self.def_total_table.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.def_total_table)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_2 = QTableWidget(self.def_total_table)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        if (self.tableWidget_2.rowCount() < 20):
            self.tableWidget_2.setRowCount(20)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font4);
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem45)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy20 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy20.setHorizontalStretch(0)
        sizePolicy20.setVerticalStretch(0)
        sizePolicy20.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy20)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush6 = QBrush(QColor(240, 240, 245, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget_2.setPalette(palette1)
        self.tableWidget_2.setStyleSheet(u"font-size: 10pt;")
        self.tableWidget_2.setFrameShape(QFrame.NoFrame)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setRowCount(20)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_26.addWidget(self.tableWidget_2)


        self.horizontalLayout_21.addWidget(self.def_total_table)

        self.def_total_text = QTextBrowser(self.report)
        self.def_total_text.setObjectName(u"def_total_text")
        sizePolicy21 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy21.setHorizontalStretch(0)
        sizePolicy21.setVerticalStretch(0)
        sizePolicy21.setHeightForWidth(self.def_total_text.sizePolicy().hasHeightForWidth())
        self.def_total_text.setSizePolicy(sizePolicy21)
        self.def_total_text.setStyleSheet(u"background-color: rgb(240, 240, 245);\n"
"border-radius: 5px;\n"
"font-size: 14pt;\n"
"font-weight: normal;\n"
"padding: 8px;")

        self.horizontalLayout_21.addWidget(self.def_total_text)

        self.final_words = QTextBrowser(self.report)
        self.final_words.setObjectName(u"final_words")
        sizePolicy21.setHeightForWidth(self.final_words.sizePolicy().hasHeightForWidth())
        self.final_words.setSizePolicy(sizePolicy21)
        self.final_words.setStyleSheet(u"background-color: rgb(240, 240, 245);\n"
"border-radius: 5px;\n"
"font-size: 14pt;\n"
"font-weight: normal;\n"
"padding: 8px;")

        self.horizontalLayout_21.addWidget(self.final_words)


        self.verticalLayout_27.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_23.addLayout(self.verticalLayout_27)

        self.stackedWidget.addWidget(self.report)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        sizePolicy5.setHeightForWidth(self.bottomBar.sizePolicy().hasHeightForWidth())
        self.bottomBar.setSizePolicy(sizePolicy5)
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_python = QPushButton(self.bottomBar)
        self.btn_python.setObjectName(u"btn_python")
        sizePolicy22 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy22.setHorizontalStretch(0)
        sizePolicy22.setVerticalStretch(0)
        sizePolicy22.setHeightForWidth(self.btn_python.sizePolicy().hasHeightForWidth())
        self.btn_python.setSizePolicy(sizePolicy22)
        self.btn_python.setMinimumSize(QSize(33, 22))
        self.btn_python.setMaximumSize(QSize(16777196, 16777215))
        self.btn_python.setStyleSheet(u"background-color:  rgb(78, 60, 105);\n"
"border: none;")
        icon23 = QIcon()
        icon23.addFile(u":/icons/images/icons/python.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_python.setIcon(icon23)
        self.btn_python.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_python)

        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMinimumSize(QSize(0, 16))
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setStyleSheet(u"")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        sizePolicy23 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy23.setHorizontalStretch(1)
        sizePolicy23.setVerticalStretch(0)
        sizePolicy23.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy23)
        self.version.setMinimumSize(QSize(0, 16))
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 16))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Submarine", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Theme based on Quiet Light", None))
        self.btn_detect_2.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"       Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"        Home", None))
        self.btn_detect.setText(QCoreApplication.translate("MainWindow", u"        Detect", None))
        self.btn_dash.setText(QCoreApplication.translate("MainWindow", u"        Dashboard", None))
        self.btn_report.setText(QCoreApplication.translate("MainWindow", u"        Report", None))
        self.btn_train.setText(QCoreApplication.translate("MainWindow", u"        Train", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"      More", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"More", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><spa"
                        "n style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Submarine</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:"
                        "12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Submarine - Hyper Speed Automatic Optical Inspection System", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.top_start_live.setText("")
        self.top_stop_live.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.home.setStyleSheet("")
        self.home_logo.setText("")
        self.home_logo_line.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>HSAOIS<span style=\" font-size:14pt; vertical-align:sub;\">by Submarine</span></p></body></html>", None))
        self.home_logo_line2.setText(QCoreApplication.translate("MainWindow", u"Invoke The Next Era In Optical Inspection", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Start</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Documentation</span></p><p><span style=\" font-size:13pt;\">New to HSAOIS? Check out our documentation.</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Access to your database</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Learn to train a custom model", None))
        self.video_tu.setText(QCoreApplication.translate("MainWindow", u" Video Tutorial", None))
        self.video_viewer.setText("")
        self.btn_start_live.setText(QCoreApplication.translate("MainWindow", u" Start", None))
        self.btn_stop_live.setText(QCoreApplication.translate("MainWindow", u" Stop", None))
        self.btn_scan.setText(QCoreApplication.translate("MainWindow", u" Scan", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u" Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.live), QCoreApplication.translate("MainWindow", u"Live Detect", None))
        self.btn_file.setText(QCoreApplication.translate("MainWindow", u" Select File", None))
        self.btn_start_file.setText(QCoreApplication.translate("MainWindow", u" Start", None))
        self.btn_stop_file.setText(QCoreApplication.translate("MainWindow", u" Stop", None))
        self.btn_result.setText(QCoreApplication.translate("MainWindow", u" Open Result", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.file), QCoreApplication.translate("MainWindow", u"File Detect", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Detect Status Output", None))
        self.textBrowser.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Batch Number", None))
        self.batch_number.setText(QCoreApplication.translate("MainWindow", u"001", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Detected", None))
        self.detected.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fraction Defective", None))
        self.frac_defective.setText(QCoreApplication.translate("MainWindow", u"0.0%", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Most Defected", None))
        self.most_defected.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Def. Types", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Def. Number Count", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Motherboard", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CPU_FAN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"FAN_Port", None))
        self.progressBar_1.setFormat(QCoreApplication.translate("MainWindow", u"%v/20", None))
        self.progressBar_2.setFormat(QCoreApplication.translate("MainWindow", u"%v/20", None))
        self.progressBar_3.setFormat(QCoreApplication.translate("MainWindow", u"%v/20", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Log Entry", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Result Class", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Notes", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.search_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search For Batch Reports", None))
        self.btn_search.setText("")
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u" Save", None))
        self.btn_question.setText(QCoreApplication.translate("MainWindow", u"?", None))
        ___qtablewidgetitem24 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem25 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem26 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem27 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"class", None));
        ___qtablewidgetitem28 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem36 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem37 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem38 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem41 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem42 = self.tableWidget_2.verticalHeaderItem(15)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem43 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Motherboard", None));
        ___qtablewidgetitem44 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"CPU_FAN", None));
        ___qtablewidgetitem45 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"FAN_Port", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.btn_python.setText("")
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"PySide 6.2.3", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"Demo Version V1.0.0 Asterisk", None))
    # retranslateUi
