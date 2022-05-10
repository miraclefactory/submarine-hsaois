# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_browser.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 665)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 647))
        MainWindow.setMaximumSize(QSize(780, 665))
        MainWindow.setStyleSheet(u"   QTabBar::tab\n"
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
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab:first\n"
"{\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"	border-top-right-radius: 0px;\n"
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
"}\n"
"\n"
"QTabWidget::pane\n"
"{ \n"
"    background-color: rgba(250, 250, 250, 1);\n"
"	top: -26px;\n"
"	padding-top: 0px;\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"	padding-bottom: 0px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-color:"
                        " rgb(136, 112, 173);\n"
"    background-color: rgb(136, 112, 173);\n"
"    color: white;\n"
"}\n"
"  ")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.pushButton_1 = QPushButton(self.tab)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy1)
        self.pushButton_1.setMinimumSize(QSize(0, 120))
        self.pushButton_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(235, 235, 235,135);\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(220,220,220);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_1.setIcon(icon)
        self.pushButton_1.setIconSize(QSize(48, 48))

        self.horizontalLayout_2.addWidget(self.pushButton_1)

        self.label_img = QLabel(self.tab)
        self.label_img.setObjectName(u"label_img")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.label_img.sizePolicy().hasHeightForWidth())
        self.label_img.setSizePolicy(sizePolicy2)
        self.label_img.setMinimumSize(QSize(0, 0))
        self.label_img.setMaximumSize(QSize(500000, 500000))
        self.label_img.setStyleSheet(u"background-color: rgb(150, 150, 150);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_img)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(0, 120))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(235, 235, 235,135);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(220,220,220);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(48, 48))

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(149, 150, 150);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_1.setText("")
        self.label_img.setText("")
        self.pushButton_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Current Image", None))
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u" Visualization ", None))
    # retranslateUi

