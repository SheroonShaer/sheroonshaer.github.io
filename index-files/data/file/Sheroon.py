# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import  random
import os
import tempfile
import wget
import zipfile

tempdir=tempfile.gettempdir()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 603)
        font = QtGui.QFont()
        font.setFamily("Estedad Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Estedad Regular")
        font.setPointSize(10)
        font.setKerning(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("/*\n"
" * MacOS Style Sheet for QT Applications\n"
" * Author: Jaime A. Quiroga P.\n"
" * Company: GTRONICK\n"
" * Last updated: 25/12/2020, 23:10.\n"
" * Available at: https://github.com/GTRONICK/QSS/blob/master/MacOS.qss\n"
" */\n"
"QMainWindow {\n"
"    background-color:#ececec;\n"
"}\n"
"QPushButton, QToolButton, QCommandLinkButton{\n"
"    padding: 0 5px 0 5px;\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-right-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-width: 2px;\n"
"    border-radius: 8px;\n"
"    color: #616161;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #fbfdfd, stop:0.5 #ffffff, stop:1 #fbfdfd);\n"
"}\n"
"QPushButton::default, QToolButton::default, QCommandLinkButton::default{\n"
"    border: 2px solid transparent;\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);\n"
"}\n"
"QPushButton:hover, QToolButton:hover, QCommandLinkButton:hover{\n"
"    color: #3d3d3d;\n"
"}\n"
"QPushButton:pressed, QToolButton:pressed, QCommandLinkButton:pressed{\n"
"    color: #aeaeae;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);\n"
"}\n"
"QPushButton:disabled, QToolButton:disabled, QCommandLinkButton:disabled{\n"
"    color: #616161;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #dce7eb, stop:0.5 #e0e8eb, stop:1 #dee7ec);\n"
"}\n"
"QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QTimeEdit, QDateEdit, QDateTimeEdit {\n"
"    border-width: 2px;\n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    background-color: #f4f4f4;\n"
"    color: #3d3d3d;\n"
"}\n"
"QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QTimeEdit:focus, QDateEdit:focus, QDateTimeEdit:focus {\n"
"    border-width: 2px;\n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #85b7e3, stop:1 #9ec1db);\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);\n"
"    background-color: #f4f4f4;\n"
"    color: #3d3d3d;\n"
"}\n"
"QLineEdit:disabled, QTextEdit:disabled, QPlainTextEdit:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled, QTimeEdit:disabled, QDateEdit:disabled, QDateTimeEdit:disabled {\n"
"    color: #b9b9b9;\n"
"}\n"
"QSpinBox::up-button, QDoubleSpinBox::up-button, QTimeEdit::up-button, QDateEdit::up-button, QDateTimeEdit::up-button {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    color: #272727;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"QSpinBox::down-button, QDoubleSpinBox::down-button, QTimeEdit::down-button, QDateEdit::down-button, QDateTimeEdit::down-button {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    width: 15px;\n"
"    color: #272727;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-bottom-right-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed, QTimeEdit::up-button:pressed, QDateEdit::up-button:pressed, QDateTimeEdit::up-button:pressed {\n"
"    color: #aeaeae;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);\n"
"}\n"
"QSpinBox::down-button:pressed, QDoubleSpinBox::down-button:pressed, QTimeEdit::down-button:pressed, QDateEdit::down-button:pressed, QDateTimeEdit::down-button:pressed {\n"
"    color: #aeaeae;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);\n"
"}\n"
"QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover, QTimeEdit::up-button:hover, QDateEdit::up-button:hover, QDateTimeEdit::up-button:hover {\n"
"    color: #FFFFFF;\n"
"    border-top-right-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);\n"
"    \n"
"}\n"
"QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover, QTimeEdit::down-button:hover, QDateEdit::down-button:hover, QDateTimeEdit::down-button:hover {\n"
"    color: #FFFFFF;\n"
"    border-bottom-right-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);\n"
"}\n"
"QSpinBox::up-arrow, QDoubleSpinBox::up-arrow, QTimeEdit::up-arrow, QDateEdit::up-arrow, QDateTimeEdit::up-arrow {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-up-symbolic.symbolic.png);\n"
"}\n"
"QSpinBox::down-arrow, QDoubleSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow, QDateTimeEdit::down-arrow {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png);\n"
"}\n"
"QProgressBar {\n"
"    max-height: 8px;\n"
"    text-align: center;\n"
"    font: italic bold 11px;\n"
"    color: #3d3d3d;\n"
"    border: 1px solid transparent;\n"
"    border-radius:4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"    border-radius: 4px;\n"
"}\n"
"QProgressBar:disabled {\n"
"    color: #616161;\n"
"}\n"
"QProgressBar::chunk:disabled {\n"
"    background-color: #aeaeae;\n"
"}\n"
"QSlider::groove {\n"
"    border: 1px solid #bbbbbb;\n"
"    background-color: #52595d;\n"
"    border-radius: 4px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 6px;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 6px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page, QSlider::sub-page {\n"
"    border: 1px transparent;\n"
"    background-color: #52595d;\n"
"    border-radius: 4px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);\n"
"}\n"
"QSlider::add-page:horizontal:disabled, QSlider::sub-page:horizontal:disabled, QSlider::add-page:vertical:disabled, QSlider::sub-page:vertical:disabled {\n"
"    background: #b9b9b9;\n"
"}\n"
"QComboBox, QFontComboBox {\n"
"    border-width: 2px;\n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    background-color: #f4f4f4;\n"
"    color: #272727;\n"
"    padding-left: 5px;\n"
"}\n"
"QComboBox:editable, QComboBox:!editable, QComboBox::drop-down:editable, QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: #ffffff;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    color: #272727;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png); /*Adawaita icon thene*/\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid darkgray;\n"
"    border-radius: 8px;\n"
"    selection-background-color: #dadada;\n"
"    selection-color: #272727;\n"
"    color: #272727;\n"
"    background: white;\n"
"}\n"
"QLabel, QCheckBox, QRadioButton {\n"
"    color: #272727;\n"
"}\n"
"QCheckBox {\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled, QRadioButton:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/object-select-symbolic.symbolic.png);\n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    color: #ffffff;\n"
"    border-radius: 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #48a5fd, stop:0.5 #329cfb, stop:1 #48a5fd);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    \n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    border-radius: 3px;\n"
"    background-color: #fbfdfa;\n"
"}\n"
"QLCDNumber {\n"
"    color: #616161;;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #ececec;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #616161;\n"
"    spacing: 3px;\n"
"    padding: 1px 4px;\n"
"    background-color: #ececec;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #dadada;\n"
"    color: #3d3d3d;\n"
"}\n"
"QMenu {\n"
"    background-color: #ececec;\n"
"}\n"
"QMenu::item:selected {\n"
"    background-color: #dadada;\n"
"    color: #3d3d3d;\n"
"}\n"
"QMenu::item {\n"
"    color: #616161;;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"    border-color: #050a0e;\n"
"    background-color: #e0e0e0;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"    padding-top: 0.5em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid #c0c0c0;\n"
"    padding: 3px;\n"
"    color: #272727;\n"
"    background-color: #fefefc;\n"
"    margin-left:0px;\n"
"}\n"
"QTabBar::tab:!last {\n"
"    border-right: 1px solid;\n"
"    border-right-color: #c0c0c0;\n"
"    border-bottom-color: #c0c0c0;\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"}\n"
"QTabBar::tab:last {\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);\n"
"}\n"
"QRadioButton::indicator {\n"
"    height: 14px;\n"
"    width: 14px;\n"
"    border-style:solid;\n"
"    border-radius:7px;\n"
"    border-width: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #48a5fd;\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #ffffff, stop:0.5 #ffffff, stop:0.6 #48a5fd, stop:1 #48a5fd);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    border-color: #a9b7c6;\n"
"    background-color: #fbfdfa;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"\n"
"QDial {\n"
"    background: #16a085;\n"
"}\n"
"\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #222b2e;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color:#222b2e;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color:#222b2e;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#222b2e;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    max-height: 10px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"    max-width: 10px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background: #52595d;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover, QScrollBar::handle:vertical:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"}\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    border: 2px transparent grey;\n"
"    border-radius: 4px;\n"
"    subcontrol-origin: margin;\n"
"    background: #b9b9b9;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed, QScrollBar::sub-line:vertical:pressed {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-up-symbolic.symbolic.png);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png);\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-previous-symbolic.symbolic.png);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-next-symbolic.symbolic.png);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.input = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.input.setFont(font)
        self.input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input.setObjectName("input")
        self.gridLayout = QtWidgets.QGridLayout(self.input)
        self.gridLayout.setObjectName("gridLayout")
        self.lblradif = QtWidgets.QLabel(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.lblradif.setFont(font)
        self.lblradif.setObjectName("lblradif")
        self.gridLayout.addWidget(self.lblradif, 2, 6, 1, 1)
        self.lblghafieh = QtWidgets.QLabel(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.lblghafieh.setFont(font)
        self.lblghafieh.setObjectName("lblghafieh")
        self.gridLayout.addWidget(self.lblghafieh, 1, 2, 1, 1)
        self.Cmbghaleb = QtWidgets.QComboBox(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.Cmbghaleb.setFont(font)
        self.Cmbghaleb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Cmbghaleb.setObjectName("Cmbghaleb")
        self.Cmbghaleb.addItem("")
        self.Cmbghaleb.addItem("")
        self.Cmbghaleb.addItem("")
        self.Cmbghaleb.addItem("")
        self.Cmbghaleb.addItem("")
        self.gridLayout.addWidget(self.Cmbghaleb, 0, 0, 1, 1)
        self.lblweight = QtWidgets.QLabel(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.lblweight.setFont(font)
        self.lblweight.setObjectName("lblweight")
        self.gridLayout.addWidget(self.lblweight, 1, 6, 1, 1)
        self.lieghafieh = QtWidgets.QLineEdit(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.lieghafieh.setFont(font)
        self.lieghafieh.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lieghafieh.setObjectName("lieghafieh")
        self.gridLayout.addWidget(self.lieghafieh, 1, 0, 1, 1)
        self.lblsabk = QtWidgets.QLabel(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.lblsabk.setFont(font)
        self.lblsabk.setObjectName("lblsabk")
        self.gridLayout.addWidget(self.lblsabk, 0, 6, 1, 1)
        self.line = QtWidgets.QFrame(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 3, 3, 1)
        self.lblghaleb = QtWidgets.QLabel(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.lblghaleb.setFont(font)
        self.lblghaleb.setObjectName("lblghaleb")
        self.gridLayout.addWidget(self.lblghaleb, 0, 2, 1, 1)
        self.compose = QtWidgets.QPushButton(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.compose.setFont(font)
        self.compose.setObjectName("compose")
        self.gridLayout.addWidget(self.compose, 2, 0, 1, 3)
        self.lieradif = QtWidgets.QLineEdit(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.lieradif.setFont(font)
        self.lieradif.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lieradif.setObjectName("lieradif")
        self.gridLayout.addWidget(self.lieradif, 2, 5, 1, 1)
        self.lieweight = QtWidgets.QLineEdit(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.lieweight.setFont(font)
        self.lieweight.setObjectName("lieweight")
        self.gridLayout.addWidget(self.lieweight, 1, 5, 1, 1)
        self.liesabk = QtWidgets.QLineEdit(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.liesabk.setFont(font)
        self.liesabk.setObjectName("liesabk")
        self.gridLayout.addWidget(self.liesabk, 0, 5, 1, 1)
        self.lbltabyat = QtWidgets.QLabel(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        self.lbltabyat.setFont(font)
        self.lbltabyat.setObjectName("lbltabyat")
        self.gridLayout.addWidget(self.lbltabyat, 3, 6, 1, 1)
        self.lieabyat = QtWidgets.QLineEdit(self.input)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        self.lieabyat.setFont(font)
        self.lieabyat.setObjectName("lieabyat")
        self.gridLayout.addWidget(self.lieabyat, 3, 5, 1, 1)
        self.gridLayout_2.addWidget(self.input, 0, 0, 1, 1)
        self.output = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.output.setFont(font)
        self.output.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.output.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.output)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.poem = QtWidgets.QTextEdit(self.output)
        font = QtGui.QFont()
        font.setFamily("Estedad Medium")
        font.setPointSize(10)
        font.setKerning(False)
        self.poem.setFont(font)
        self.poem.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.poem.setObjectName("poem")
        self.gridLayout_3.addWidget(self.poem, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.output, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.compose.clicked.connect(self.run)
        #i = print(sher("ferdosi","2",'',"__U_U____U_U__",10,"masnavi"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "شعرون"))
        self.input.setTitle(_translate("MainWindow", "ارکان شعر"))
        self.lblradif.setText(_translate("MainWindow", "ردیف:"))
        self.lblghafieh.setText(_translate("MainWindow", "قافیه:"))
        self.Cmbghaleb.setItemText(0, _translate("MainWindow", "مثنوی"))
        self.Cmbghaleb.setItemText(1, _translate("MainWindow", "غزل"))
        self.Cmbghaleb.setItemText(2, _translate("MainWindow", "دوبیتی"))
        self.Cmbghaleb.setItemText(3, _translate("MainWindow", "قطعه"))
        self.Cmbghaleb.setItemText(4, _translate("MainWindow", "ساخت قافيه"))
        self.lblweight.setText(_translate("MainWindow", "وزن(U_):"))
        self.lblsabk.setText(_translate("MainWindow", "سبک:"))
        self.lblghaleb.setText(_translate("MainWindow", "قالب:"))
        self.compose.setText(_translate("MainWindow", "بسرای"))
        self.lbltabyat.setText(_translate("MainWindow", "تعداد ابیات:"))
        self.output.setTitle(_translate("MainWindow", "خروجی"))
    def run(self):
        sabk=self.liesabk.text()
        weight=self.lieweight.text()
        ghafieh=self.lieghafieh.text()
        radif=self.lieradif.text()
        abyat=self.lieabyat.text()
        ghaleb=self.Cmbghaleb.currentText()

        try:
            abyat=int(abyat)
        except:
            abyat=10
        if ghaleb=="مثنوی":
            ghaleb="masnavi"
            try:
                x=int(ghafieh)
            except:
                ghafieh=str('2')
        elif ghaleb=="غزل":
            ghaleb="ghazal"
        elif ghaleb=="دوبیتی":
            ghaleb="dobeyti"
        elif ghaleb=="قطعه":
            ghaleb="ghate"
        elif ghaleb=="ساخت قافيه":
            ghaleb="all_gh"
        self.poem.clear()
        self.poem.append(str(sher(sabk,ghafieh,radif,weight,abyat,ghaleb)))
        # with open(tempdir+'/sheroon.txt',"w",encoding="UTF-8") as f:
        #     f.write(str(sher(sabk,ghafieh,radif,weight,abyat,ghaleb)))
        #     f.close()
        # with open(tempdir+'/sheroon.txt',"r",encoding="UTF-8") as f:
        #     c=f.read()
        #     self.poem.append(str(c))
def sher(sabk, ghaf, radif, vaz, abyat, ghaleb):
    er1 = 'متاسّفانه حجم ابیاتی که برای مثنوی می‌خواهید بسیار زیاد است.\nما در پایگاه داده‌ی خود این تعداد را نداریم!!!'
    er2 = 'ردیف مورد نظر شما در پایگاه داده‌ی ما موجود نیست!!!'
    er3 = 'وزن انتخاب شده با تنظیمات هماهنگ نیست!!!'
    er4 = 'سبک نوشته‌شده وجود ندارد!!! برای بروز رسانی در محل سبک کلمه‌ی update را بنویسید و «بسرای» را فشار دهید!'
    er5 = 'برای قالب مورد نظر نوشتن قافیه نیاز است!!!'
    # settings = open('settings.txt', 'r', encoding='UTF8').read().split('\n')


    if vaz == '':
        vazn_10= ['__UU_____UU___', '_U___U___U_', 'U__U__U__U_', 'U___U___U___U__', 'UU__UU__UU__UU_',
                    'U_U_UU__U_U_UU_', '__U_U_UU__U_U_', '_U___U___U___U_', 'U___U___U___U___',
                    '__U_U____U_U__', '__UU__UU__UU__']
        vaz = random.choice(vazn_10)

    if ghaf == '':
        return er5


    def update():
        url = "https://github.com/SheroonShaer/data/raw/main/data.zip"
        try:os.remove(tempfile.gettempdir()+'/'+"data.zip")
        except:print("cont")
        wget.download(url,tempfile.gettempdir())
        with zipfile.ZipFile(tempfile.gettempdir()+'/'+"data.zip","r") as zip_ref:
            zip_ref.extractall("./")


    if sabk == 'update':
        update()
        return 'برنامه را دوباره اجرا کنید!'
    try:
        settings = ['', sabk, '', ghaf, '', radif, '', vaz, '', abyat, '', ghaleb]
        divan = open(f'data/{settings[1]}.txt', 'r', encoding='UTF8').read().replace('\n', ' ').split(' ')
        taghti_d = open(f'data/ta_{settings[1]}.txt', 'r', encoding='UTF8').read().replace('\n', ' ').split(' ')
        all = []
    except:
        return er4


    def ARRtoSTR (i):
        try:
            t = ''
            for j in i:
               t += j
        except:
            t = i
        return t 

    def vazn (world):
        l = world.split('*')
        txt = ''
        for i in range(len(l)):
            if len(l[i]) == 1:
                txt += 'U'
            elif len(l[i]) == 2:
                txt += '_'
            elif len(l[i]) == 3 and l[i][1] in ['ا','ی','و'] and l[i][2] == 'ن':
                txt += '_'
            else:
                txt += '_U'
        return txt


    for i in range(len(divan)):
        all.append({'w':(divan[i]), 't':taghti_d[i], 'v':vazn(taghti_d[i])})


    def dell_last_U (w):
        if w['w'][-1] == 'ه' and w['v'][-1] == 'U':
            tmp = w['v'][:-1] + '_'
        elif w['v'][-1] == 'U':
            tmp = w['v'][:-1]
        else:
            tmp = w['v']
        return {'w':w['w'], 'v':tmp}


    if settings[5] == '':
        radif = ''
        radif_v = ''
    else:
        # if not radif in divan ====>>> خطای ردیف تعریف نشده
        if not settings[5] in divan:
            return er2 
        radif = all[divan.index(settings[5])]['w']
        radif_v = dell_last_U(all[divan.index(settings[5])])['v']
    check = all.copy()
    all_arr = []
    gh = settings[3]
    while check != []:
        word = check.pop(0)
        if word['w'][-len(gh):] == gh:
            if radif != '':
                all_arr.append(dell_last_U(word))
            else:
                all_arr.append(word)
    true_arr = []
    for i in all_arr:
        v = i['v'] + radif_v
        if settings[7][-(len(v)):] == v:
            true_arr.append({'w':(i['w']+' '+radif), 'v':v})
    random.shuffle(true_arr)
    if ghaleb != 'masnavi':
        ghs = true_arr

    def mesra (gh, gh2):
        vaz = settings[7]
        mes = ''
        m_v = ''
        if gh2 == []:
            return ''
        tmp = random.choice(gh2)
        if gh :
            mes += tmp['w']
            m_v += dell_last_U(tmp)['v']
        t_arr = []
        while m_v!=vaz:
            t_arr = []
            for i in range(len(all)-1):
                if all[i] == mes.split(' ')[-1] and m_v+all[i+1]['v'] == vazn[-(len(m_v+all[i+1]['v'])):]:
                    t_arr.append(all[i+1])
            if t_arr == []:
                for i in range(len(all)):
                    if (len(m_v+all[i]['v']))<=len(vaz):
                        if all[i]['v']+m_v == vaz[-(len(all[i]['v']+m_v)):]:
                            t_arr.append(all[i])
            if t_arr == []:
                return ''
            w = random.choice(t_arr)
            # if t_arr == [] ====>>> خطای تنظیمات نامناسب
            m_v = w['v']+m_v
            mes = w['w']+' '+mes
        return mes


    def ghazal ():
        sher = []
        abya = int(settings[9])
        sher.append(mesra(True, ghs) + '\n')
        sher.append(mesra(True, ghs) + '\n')
        for i in range(abya - 1):
            sher.append(mesra(False, ghs) + '\n')
            sher.append(mesra(True, ghs) + '\n')
        return sher


    def ghate ():
        sher = []
        abya = int(settings[9])
        for i in range(abya):
            sher.append(mesra(False, ghs) + '\n')
            sher.append(mesra(True, ghs) + '\n')
        return sher


    def all_gh ():
        sher = []
        abya = int(settings[9])
        for i in range(abya):
            sher.append(mesra(True, ghs) + '\n')
            sher.append(mesra(True, ghs) + '\n')
        return sher


    def dobeyti ():
        sher = []
        sher.append(mesra(True, ghs) + '\n')
        sher.append(mesra(True, ghs) + '\n')
        sher.append(mesra(False, ghs) + '\n')
        sher.append(mesra(True, ghs) + '\n')
        return sher


    def masnavi ():
        sher = []
        abya = int(settings[9])
        vaz = settings[7]
        ghl = -(int(settings[3]))
        g = []
        w = []
        t = []
        for i in all:
            if not i['w'][ghl:] in g:
                g.append(i['w'][ghl:])
                w.append([{'w':i['w'], 'v':i['v']}])
            else:
                w[g.index(i['w'][ghl:])].append({'w':i['w'], 'v':i['v']})
        for i in w:
            if len(i) > 1:
                t.append([])
                for j in i:
                    if vaz[-(len(dell_last_U(j)['v'])):] == dell_last_U(j)['v'] and not j in t[-1]:
                        t[-1].append(j)
                random.shuffle(t[-1])
                if len(t[-1]) < 2:
                    t = t[:-1]
        random.shuffle(t)
        t = t * (int((settings[9] - 0.1) / len(t)) + 1)
        random.shuffle(t)
        for i in range(abya):
            if i >= len(t):
                return er1
            g = t[i]
            # if i >= len(t) ====>>> خطای کمبود قافیه
            random.shuffle(g)
            sher.append(mesra(True, [g[0]]) + '\n')
            sher.append(mesra(True, [g[1]]) + '\n')
        return sher


    if settings[11] == 'ghazal':
        i = ghazal()
        if i[1] == '\n':
            return er3
        return ARRtoSTR(i)
    if settings[11] == 'ghate':
        i = ghate()
        if i[1] == '\n':
            return er3
        return ARRtoSTR(i)
    if settings[11] == 'dobeyti':
        i = dobeyti()
        if i[1] == '\n':
            return er3
        return ARRtoSTR(i)
    if settings[11] == 'masnavi':
        return ARRtoSTR(masnavi())
    if settings[11] == 'all_gh':
        i = all_gh()
        if i[1] == '\n':
            return er3
        return ARRtoSTR(i)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
