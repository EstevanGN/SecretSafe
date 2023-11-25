# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 800)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/logo.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
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
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
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
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
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
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/menu.png);")

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
        self.btn_classical = QPushButton(self.topMenu)
        self.btn_classical.setObjectName(u"btn_classical")
        sizePolicy.setHeightForWidth(self.btn_classical.sizePolicy().hasHeightForWidth())
        self.btn_classical.setSizePolicy(sizePolicy)
        self.btn_classical.setMinimumSize(QSize(0, 70))
        self.btn_classical.setFont(font)
        self.btn_classical.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_classical.setLayoutDirection(Qt.LeftToRight)
        self.btn_classical.setStyleSheet(u"background-image: url(:/icons/images/icons/classical.png);")
        self.btn_classical.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.btn_classical)

        self.btn_block = QPushButton(self.topMenu)
        self.btn_block.setObjectName(u"btn_block")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_block.sizePolicy().hasHeightForWidth())
        self.btn_block.setSizePolicy(sizePolicy1)
        self.btn_block.setMinimumSize(QSize(0, 70))
        self.btn_block.setFont(font)
        self.btn_block.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_block.setLayoutDirection(Qt.LeftToRight)
        self.btn_block.setStyleSheet(u"background-image: url(:/icons/images/icons/block_2.png);")

        self.verticalLayout_8.addWidget(self.btn_block)

        self.btn_public_key = QPushButton(self.topMenu)
        self.btn_public_key.setObjectName(u"btn_public_key")
        sizePolicy.setHeightForWidth(self.btn_public_key.sizePolicy().hasHeightForWidth())
        self.btn_public_key.setSizePolicy(sizePolicy)
        self.btn_public_key.setMinimumSize(QSize(0, 70))
        self.btn_public_key.setFont(font)
        self.btn_public_key.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_public_key.setLayoutDirection(Qt.LeftToRight)
        self.btn_public_key.setStyleSheet(u"background-image: url(:/icons/images/icons/public_key_2.png);")

        self.verticalLayout_8.addWidget(self.btn_public_key)

        self.btn_analysis = QPushButton(self.topMenu)
        self.btn_analysis.setObjectName(u"btn_analysis")
        sizePolicy.setHeightForWidth(self.btn_analysis.sizePolicy().hasHeightForWidth())
        self.btn_analysis.setSizePolicy(sizePolicy)
        self.btn_analysis.setMinimumSize(QSize(0, 70))
        self.btn_analysis.setFont(font)
        self.btn_analysis.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_analysis.setLayoutDirection(Qt.LeftToRight)
        self.btn_analysis.setStyleSheet(u"background-image: url(:/icons/images/icons/analysis.png)")

        self.verticalLayout_8.addWidget(self.btn_analysis)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

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
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
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
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


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
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
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
        self.verticalLayout_26 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"# background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"# background-position: center;\n"
"# background-repeat: no-repeat;")
        self.horizontalLayout_7 = QHBoxLayout(self.home)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.classical_list = QComboBox(self.home)
        self.classical_list.addItem("")
        self.classical_list.addItem("")
        self.classical_list.addItem("")
        self.classical_list.addItem("")
        self.classical_list.addItem("")
        self.classical_list.setObjectName(u"classical_list")
        self.classical_list.setMinimumSize(QSize(0, 0))
        self.classical_list.setMaximumSize(QSize(167, 32))
        self.classical_list.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")

        self.horizontalLayout_7.addWidget(self.classical_list, 0, Qt.AlignVCenter)

        self.classical_input_widget = QWidget(self.home)
        self.classical_input_widget.setObjectName(u"classical_input_widget")
        self.verticalLayout_15 = QVBoxLayout(self.classical_input_widget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.classical_encrypt_process = QLineEdit(self.classical_input_widget)
        self.classical_encrypt_process.setObjectName(u"classical_encrypt_process")
        self.classical_encrypt_process.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.classical_encrypt_process.setAlignment(Qt.AlignCenter)
        self.classical_encrypt_process.setReadOnly(True)

        self.verticalLayout_15.addWidget(self.classical_encrypt_process)

        self.classical_encrypt_input = QTextEdit(self.classical_input_widget)
        self.classical_encrypt_input.setObjectName(u"classical_encrypt_input")
        self.classical_encrypt_input.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")

        self.verticalLayout_15.addWidget(self.classical_encrypt_input)

        self.classical_generated_key_widget = QWidget(self.classical_input_widget)
        self.classical_generated_key_widget.setObjectName(u"classical_generated_key_widget")
        sizePolicy.setHeightForWidth(self.classical_generated_key_widget.sizePolicy().hasHeightForWidth())
        self.classical_generated_key_widget.setSizePolicy(sizePolicy)
        self.classical_generated_key_widget.setMinimumSize(QSize(0, 40))
        self.classical_generated_key_widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_11 = QHBoxLayout(self.classical_generated_key_widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.classical_generated_key_icon = QPushButton(self.classical_generated_key_widget)
        self.classical_generated_key_icon.setObjectName(u"classical_generated_key_icon")
        self.classical_generated_key_icon.setEnabled(True)
        self.classical_generated_key_icon.setMinimumSize(QSize(0, 30))
        self.classical_generated_key_icon.setMaximumSize(QSize(16777215, 30))
        self.classical_generated_key_icon.setStyleSheet(u"border: 2px solid violet;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-caret-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.classical_generated_key_icon.setIcon(icon3)

        self.horizontalLayout_11.addWidget(self.classical_generated_key_icon)

        self.classica_generated_key_line = QLineEdit(self.classical_generated_key_widget)
        self.classica_generated_key_line.setObjectName(u"classica_generated_key_line")
        self.classica_generated_key_line.setEnabled(False)
        sizePolicy.setHeightForWidth(self.classica_generated_key_line.sizePolicy().hasHeightForWidth())
        self.classica_generated_key_line.setSizePolicy(sizePolicy)
        self.classica_generated_key_line.setMinimumSize(QSize(120, 30))
        self.classica_generated_key_line.setMaximumSize(QSize(120, 30))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setKerning(True)
        self.classica_generated_key_line.setFont(font4)
        self.classica_generated_key_line.setAutoFillBackground(False)
        self.classica_generated_key_line.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: none;\n"
"border-radius: 10px;")
        self.classica_generated_key_line.setAlignment(Qt.AlignCenter)
        self.classica_generated_key_line.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.classica_generated_key_line)

        self.classical_generated_key_output = QTextEdit(self.classical_generated_key_widget)
        self.classical_generated_key_output.setObjectName(u"classical_generated_key_output")
        self.classical_generated_key_output.setMinimumSize(QSize(0, 30))
        self.classical_generated_key_output.setMaximumSize(QSize(16777215, 30))
        self.classical_generated_key_output.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")
        self.classical_generated_key_output.setReadOnly(False)

        self.horizontalLayout_11.addWidget(self.classical_generated_key_output)


        self.verticalLayout_15.addWidget(self.classical_generated_key_widget)

        self.classical_btn_encrypt = QPushButton(self.classical_input_widget)
        self.classical_btn_encrypt.setObjectName(u"classical_btn_encrypt")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.classical_btn_encrypt.sizePolicy().hasHeightForWidth())
        self.classical_btn_encrypt.setSizePolicy(sizePolicy4)
        self.classical_btn_encrypt.setMinimumSize(QSize(100, 0))
        self.classical_btn_encrypt.setMaximumSize(QSize(500, 40))
        self.classical_btn_encrypt.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-lock-locked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.classical_btn_encrypt.setIcon(icon4)

        self.verticalLayout_15.addWidget(self.classical_btn_encrypt, 0, Qt.AlignHCenter)

        self.classical_encrypt_output = QTextEdit(self.classical_input_widget)
        self.classical_encrypt_output.setObjectName(u"classical_encrypt_output")
        self.classical_encrypt_output.setMinimumSize(QSize(0, 0))
        self.classical_encrypt_output.setMaximumSize(QSize(16777215, 100))
        self.classical_encrypt_output.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.classical_encrypt_output.setReadOnly(True)

        self.verticalLayout_15.addWidget(self.classical_encrypt_output)


        self.horizontalLayout_7.addWidget(self.classical_input_widget)

        self.classical_vertical_line = QFrame(self.home)
        self.classical_vertical_line.setObjectName(u"classical_vertical_line")
        self.classical_vertical_line.setStyleSheet(u"border-width: 5px;\n"
" border-style: solid; \n"
"border-color: violet;")
        self.classical_vertical_line.setFrameShape(QFrame.VLine)
        self.classical_vertical_line.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.classical_vertical_line)

        self.classical_output_widget = QWidget(self.home)
        self.classical_output_widget.setObjectName(u"classical_output_widget")
        self.verticalLayout_18 = QVBoxLayout(self.classical_output_widget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.classical_decrypt_process = QLineEdit(self.classical_output_widget)
        self.classical_decrypt_process.setObjectName(u"classical_decrypt_process")
        self.classical_decrypt_process.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.classical_decrypt_process.setAlignment(Qt.AlignCenter)
        self.classical_decrypt_process.setReadOnly(True)

        self.verticalLayout_18.addWidget(self.classical_decrypt_process)

        self.classical_decrypt_input = QTextEdit(self.classical_output_widget)
        self.classical_decrypt_input.setObjectName(u"classical_decrypt_input")
        self.classical_decrypt_input.setMinimumSize(QSize(0, 0))
        self.classical_decrypt_input.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")
        self.classical_decrypt_input.setReadOnly(False)

        self.verticalLayout_18.addWidget(self.classical_decrypt_input)

        self.classical_key_widget = QWidget(self.classical_output_widget)
        self.classical_key_widget.setObjectName(u"classical_key_widget")
        sizePolicy.setHeightForWidth(self.classical_key_widget.sizePolicy().hasHeightForWidth())
        self.classical_key_widget.setSizePolicy(sizePolicy)
        self.classical_key_widget.setMinimumSize(QSize(0, 40))
        self.classical_key_widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_10 = QHBoxLayout(self.classical_key_widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.classical_key_icon = QPushButton(self.classical_key_widget)
        self.classical_key_icon.setObjectName(u"classical_key_icon")
        self.classical_key_icon.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.classical_key_icon.sizePolicy().hasHeightForWidth())
        self.classical_key_icon.setSizePolicy(sizePolicy4)
        self.classical_key_icon.setMinimumSize(QSize(0, 30))
        self.classical_key_icon.setMaximumSize(QSize(16777215, 30))
        self.classical_key_icon.setFocusPolicy(Qt.WheelFocus)
        self.classical_key_icon.setStyleSheet(u"border: none;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/public_key_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.classical_key_icon.setIcon(icon5)

        self.horizontalLayout_10.addWidget(self.classical_key_icon)

        self.classical_key_line = QLineEdit(self.classical_key_widget)
        self.classical_key_line.setObjectName(u"classical_key_line")
        sizePolicy.setHeightForWidth(self.classical_key_line.sizePolicy().hasHeightForWidth())
        self.classical_key_line.setSizePolicy(sizePolicy)
        self.classical_key_line.setMinimumSize(QSize(70, 30))
        self.classical_key_line.setMaximumSize(QSize(70, 30))
        self.classical_key_line.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: none;\n"
"border-radius: 10px;")
        self.classical_key_line.setAlignment(Qt.AlignCenter)
        self.classical_key_line.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.classical_key_line)

        self.classical_key_input = QTextEdit(self.classical_key_widget)
        self.classical_key_input.setObjectName(u"classical_key_input")
        self.classical_key_input.setMinimumSize(QSize(0, 30))
        self.classical_key_input.setMaximumSize(QSize(16777215, 30))
        self.classical_key_input.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")

        self.horizontalLayout_10.addWidget(self.classical_key_input)


        self.verticalLayout_18.addWidget(self.classical_key_widget)

        self.classical_btn_decrypt = QPushButton(self.classical_output_widget)
        self.classical_btn_decrypt.setObjectName(u"classical_btn_decrypt")
        sizePolicy4.setHeightForWidth(self.classical_btn_decrypt.sizePolicy().hasHeightForWidth())
        self.classical_btn_decrypt.setSizePolicy(sizePolicy4)
        self.classical_btn_decrypt.setMinimumSize(QSize(100, 0))
        self.classical_btn_decrypt.setMaximumSize(QSize(500, 40))
        self.classical_btn_decrypt.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-lock-unlocked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.classical_btn_decrypt.setIcon(icon6)

        self.verticalLayout_18.addWidget(self.classical_btn_decrypt, 0, Qt.AlignHCenter)

        self.classical_decrypt_output = QTextEdit(self.classical_output_widget)
        self.classical_decrypt_output.setObjectName(u"classical_decrypt_output")
        self.classical_decrypt_output.setMaximumSize(QSize(16777215, 100))
        self.classical_decrypt_output.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.classical_decrypt_output.setReadOnly(True)

        self.verticalLayout_18.addWidget(self.classical_decrypt_output)


        self.horizontalLayout_7.addWidget(self.classical_output_widget)

        self.stackedWidget.addWidget(self.home)
        self.welcome_page = QWidget()
        self.welcome_page.setObjectName(u"welcome_page")
        sizePolicy.setHeightForWidth(self.welcome_page.sizePolicy().hasHeightForWidth())
        self.welcome_page.setSizePolicy(sizePolicy)
        self.welcome_page.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_6 = QHBoxLayout(self.welcome_page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget = QWidget(self.welcome_page)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_23 = QVBoxLayout(self.widget)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.welcome_page_tittle = QLineEdit(self.widget)
        self.welcome_page_tittle.setObjectName(u"welcome_page_tittle")
        sizePolicy.setHeightForWidth(self.welcome_page_tittle.sizePolicy().hasHeightForWidth())
        self.welcome_page_tittle.setSizePolicy(sizePolicy)
        self.welcome_page_tittle.setMinimumSize(QSize(0, 60))
        self.welcome_page_tittle.setMaximumSize(QSize(16777215, 60))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(35)
        font5.setBold(False)
        font5.setItalic(False)
        self.welcome_page_tittle.setFont(font5)
        self.welcome_page_tittle.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"font-size: 35pt;\n"
"color: rgb(212, 94, 234);")
        self.welcome_page_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.welcome_page_tittle)

        self.welcome_page_widget = QWidget(self.widget)
        self.welcome_page_widget.setObjectName(u"welcome_page_widget")
        sizePolicy.setHeightForWidth(self.welcome_page_widget.sizePolicy().hasHeightForWidth())
        self.welcome_page_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_9 = QHBoxLayout(self.welcome_page_widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.welcome_page_description = QTextEdit(self.welcome_page_widget)
        self.welcome_page_description.setObjectName(u"welcome_page_description")
        self.welcome_page_description.setMinimumSize(QSize(500, 0))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(30)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setKerning(True)
        self.welcome_page_description.setFont(font6)
        self.welcome_page_description.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"border-radius: 10px;\n"
"font-size: 30pt;")

        self.horizontalLayout_9.addWidget(self.welcome_page_description)

        self.welcome_page_image = QPushButton(self.welcome_page_widget)
        self.welcome_page_image.setObjectName(u"welcome_page_image")
        self.welcome_page_image.setEnabled(True)
        sizePolicy.setHeightForWidth(self.welcome_page_image.sizePolicy().hasHeightForWidth())
        self.welcome_page_image.setSizePolicy(sizePolicy)
        self.welcome_page_image.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"border-radius: 50px;")
        icon7 = QIcon()
        icon7.addFile(u":/images/images/images/kawai.png", QSize(), QIcon.Normal, QIcon.Off)
        self.welcome_page_image.setIcon(icon7)
        self.welcome_page_image.setIconSize(QSize(500, 500))

        self.horizontalLayout_9.addWidget(self.welcome_page_image)


        self.verticalLayout_23.addWidget(self.welcome_page_widget)


        self.horizontalLayout_6.addWidget(self.widget)

        self.stackedWidget.addWidget(self.welcome_page)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.horizontalLayout_15 = QVBoxLayout(self.widgets)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.block_horizontal_layout = QHBoxLayout()
        self.block_horizontal_layout.setObjectName(u"block_horizontal_layout")
        self.block_combo_widget = QWidget(self.widgets)
        self.block_combo_widget.setObjectName(u"block_combo_widget")
        self.verticalLayout_17 = QVBoxLayout(self.block_combo_widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.block_list = QComboBox(self.block_combo_widget)
        self.block_list.addItem("")
        self.block_list.addItem("")
        self.block_list.addItem("")
        self.block_list.addItem("")
        self.block_list.setObjectName(u"block_list")
        self.block_list.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")

        self.verticalLayout_17.addWidget(self.block_list, 0, Qt.AlignTop)

        self.block_mode_widget = QWidget(self.block_combo_widget)
        self.block_mode_widget.setObjectName(u"block_mode_widget")
        self.verticalLayout_22 = QVBoxLayout(self.block_mode_widget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.block_mode_btn = QPushButton(self.block_mode_widget)
        self.block_mode_btn.setObjectName(u"block_mode_btn")
        self.block_mode_btn.setEnabled(False)
        self.block_mode_btn.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: none;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_mode_btn.setIcon(icon8)

        self.verticalLayout_22.addWidget(self.block_mode_btn)

        self.block_mode_list = QComboBox(self.block_mode_widget)
        self.block_mode_list.addItem("")
        self.block_mode_list.addItem("")
        self.block_mode_list.addItem("")
        self.block_mode_list.addItem("")
        self.block_mode_list.setObjectName(u"block_mode_list")
        self.block_mode_list.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")

        self.verticalLayout_22.addWidget(self.block_mode_list)


        self.verticalLayout_17.addWidget(self.block_mode_widget, 0, Qt.AlignVCenter)


        self.block_horizontal_layout.addWidget(self.block_combo_widget)

        self.block_input_widget = QWidget(self.widgets)
        self.block_input_widget.setObjectName(u"block_input_widget")
        self.verticalLayout_16 = QVBoxLayout(self.block_input_widget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.block_encrypt_process = QLineEdit(self.block_input_widget)
        self.block_encrypt_process.setObjectName(u"block_encrypt_process")
        self.block_encrypt_process.setEnabled(False)
        self.block_encrypt_process.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.block_encrypt_process.setAlignment(Qt.AlignCenter)
        self.block_encrypt_process.setReadOnly(True)

        self.verticalLayout_16.addWidget(self.block_encrypt_process)

        self.block_encrypt_filesearch_widget = QWidget(self.block_input_widget)
        self.block_encrypt_filesearch_widget.setObjectName(u"block_encrypt_filesearch_widget")
        self.horizontalLayout_18 = QHBoxLayout(self.block_encrypt_filesearch_widget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.block_encrypt_filepath = QLineEdit(self.block_encrypt_filesearch_widget)
        self.block_encrypt_filepath.setObjectName(u"block_encrypt_filepath")
        self.block_encrypt_filepath.setEnabled(True)
        self.block_encrypt_filepath.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.block_encrypt_filepath.setReadOnly(False)

        self.horizontalLayout_18.addWidget(self.block_encrypt_filepath)

        self.block_encrypt_filepath_btn = QPushButton(self.block_encrypt_filesearch_widget)
        self.block_encrypt_filepath_btn.setObjectName(u"block_encrypt_filepath_btn")
        self.block_encrypt_filepath_btn.setMinimumSize(QSize(50, 0))
        self.block_encrypt_filepath_btn.setMaximumSize(QSize(50, 16777215))
        self.block_encrypt_filepath_btn.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_encrypt_filepath_btn.setIcon(icon9)

        self.horizontalLayout_18.addWidget(self.block_encrypt_filepath_btn)


        self.verticalLayout_16.addWidget(self.block_encrypt_filesearch_widget)

        self.block_encrypt_filename_widget = QWidget(self.block_input_widget)
        self.block_encrypt_filename_widget.setObjectName(u"block_encrypt_filename_widget")
        self.block_encrypt_filename_widget.setMinimumSize(QSize(0, 33))
        self.block_encrypt_filename_widget.setMaximumSize(QSize(16777215, 33))
        self.horizontalLayout_17 = QHBoxLayout(self.block_encrypt_filename_widget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.block_encrypt_filename_tittle = QLineEdit(self.block_encrypt_filename_widget)
        self.block_encrypt_filename_tittle.setObjectName(u"block_encrypt_filename_tittle")
        self.block_encrypt_filename_tittle.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.block_encrypt_filename_tittle.sizePolicy().hasHeightForWidth())
        self.block_encrypt_filename_tittle.setSizePolicy(sizePolicy5)
        self.block_encrypt_filename_tittle.setMinimumSize(QSize(90, 25))
        self.block_encrypt_filename_tittle.setMaximumSize(QSize(90, 25))
        self.block_encrypt_filename_tittle.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"")
        self.block_encrypt_filename_tittle.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.block_encrypt_filename_tittle)

        self.block_encrypt_filename = QTextEdit(self.block_encrypt_filename_widget)
        self.block_encrypt_filename.setObjectName(u"block_encrypt_filename")
        self.block_encrypt_filename.setMinimumSize(QSize(0, 25))
        self.block_encrypt_filename.setMaximumSize(QSize(16777215, 25))
        self.block_encrypt_filename.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_17.addWidget(self.block_encrypt_filename)


        self.verticalLayout_16.addWidget(self.block_encrypt_filename_widget)

        self.block_generate_key_widget = QWidget(self.block_input_widget)
        self.block_generate_key_widget.setObjectName(u"block_generate_key_widget")
        self.block_generate_key_widget.setMinimumSize(QSize(0, 60))
        self.block_generate_key_widget.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_14 = QHBoxLayout(self.block_generate_key_widget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.block_generate_key_btn = QPushButton(self.block_generate_key_widget)
        self.block_generate_key_btn.setObjectName(u"block_generate_key_btn")
        self.block_generate_key_btn.setMinimumSize(QSize(0, 25))
        self.block_generate_key_btn.setMaximumSize(QSize(16777215, 25))
        self.block_generate_key_btn.setStyleSheet(u"border: 2px solid violet;")
        self.block_generate_key_btn.setIcon(icon3)

        self.horizontalLayout_14.addWidget(self.block_generate_key_btn)

        self.block_geenerate_key_message = QLineEdit(self.block_generate_key_widget)
        self.block_geenerate_key_message.setObjectName(u"block_geenerate_key_message")
        self.block_geenerate_key_message.setEnabled(False)
        self.block_geenerate_key_message.setMinimumSize(QSize(100, 25))
        self.block_geenerate_key_message.setMaximumSize(QSize(100, 25))
        self.block_geenerate_key_message.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: nonet;\n"
"border-radius: 10px;")
        self.block_geenerate_key_message.setAlignment(Qt.AlignCenter)
        self.block_geenerate_key_message.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.block_geenerate_key_message)

        self.block_generate_key_output = QTextEdit(self.block_generate_key_widget)
        self.block_generate_key_output.setObjectName(u"block_generate_key_output")
        self.block_generate_key_output.setMinimumSize(QSize(0, 50))
        self.block_generate_key_output.setMaximumSize(QSize(16777215, 50))
        self.block_generate_key_output.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")

        self.horizontalLayout_14.addWidget(self.block_generate_key_output)


        self.verticalLayout_16.addWidget(self.block_generate_key_widget)

        self.block_encrypt_btn = QPushButton(self.block_input_widget)
        self.block_encrypt_btn.setObjectName(u"block_encrypt_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.block_encrypt_btn.sizePolicy().hasHeightForWidth())
        self.block_encrypt_btn.setSizePolicy(sizePolicy6)
        self.block_encrypt_btn.setMinimumSize(QSize(100, 0))
        self.block_encrypt_btn.setMaximumSize(QSize(500, 40))
        self.block_encrypt_btn.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.block_encrypt_btn.setIcon(icon4)

        self.verticalLayout_16.addWidget(self.block_encrypt_btn, 0, Qt.AlignHCenter)

        self.block_encrypt_output = QLabel(self.block_input_widget)
        self.block_encrypt_output.setObjectName(u"block_encrypt_output")
        sizePolicy.setHeightForWidth(self.block_encrypt_output.sizePolicy().hasHeightForWidth())
        self.block_encrypt_output.setSizePolicy(sizePolicy)
        self.block_encrypt_output.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"")
        self.block_encrypt_output.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.block_encrypt_output)


        self.block_horizontal_layout.addWidget(self.block_input_widget)

        self.block_vertical_line = QFrame(self.widgets)
        self.block_vertical_line.setObjectName(u"block_vertical_line")
        self.block_vertical_line.setStyleSheet(u"border-width: 5px;\n"
" border-style: solid; \n"
"border-color: violet;")
        self.block_vertical_line.setFrameShape(QFrame.VLine)
        self.block_vertical_line.setFrameShadow(QFrame.Raised)

        self.block_horizontal_layout.addWidget(self.block_vertical_line)

        self.block_output_widget = QWidget(self.widgets)
        self.block_output_widget.setObjectName(u"block_output_widget")
        self.verticalLayout = QVBoxLayout(self.block_output_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.block_decrypt_process = QLineEdit(self.block_output_widget)
        self.block_decrypt_process.setObjectName(u"block_decrypt_process")
        self.block_decrypt_process.setEnabled(False)
        self.block_decrypt_process.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.block_decrypt_process.setAlignment(Qt.AlignCenter)
        self.block_decrypt_process.setReadOnly(True)

        self.verticalLayout.addWidget(self.block_decrypt_process)

        self.block_decrypt_search_widget = QWidget(self.block_output_widget)
        self.block_decrypt_search_widget.setObjectName(u"block_decrypt_search_widget")
        self.horizontalLayout_19 = QHBoxLayout(self.block_decrypt_search_widget)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.block_decrypt_filepath = QLineEdit(self.block_decrypt_search_widget)
        self.block_decrypt_filepath.setObjectName(u"block_decrypt_filepath")
        self.block_decrypt_filepath.setEnabled(True)
        self.block_decrypt_filepath.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.block_decrypt_filepath.setReadOnly(False)

        self.horizontalLayout_19.addWidget(self.block_decrypt_filepath)

        self.block_decrypt_filepath_btn = QPushButton(self.block_decrypt_search_widget)
        self.block_decrypt_filepath_btn.setObjectName(u"block_decrypt_filepath_btn")
        self.block_decrypt_filepath_btn.setMinimumSize(QSize(50, 0))
        self.block_decrypt_filepath_btn.setMaximumSize(QSize(50, 16777215))
        self.block_decrypt_filepath_btn.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;")
        self.block_decrypt_filepath_btn.setIcon(icon9)

        self.horizontalLayout_19.addWidget(self.block_decrypt_filepath_btn)


        self.verticalLayout.addWidget(self.block_decrypt_search_widget)

        self.block_decrypt_filename_widget = QWidget(self.block_output_widget)
        self.block_decrypt_filename_widget.setObjectName(u"block_decrypt_filename_widget")
        self.block_decrypt_filename_widget.setMinimumSize(QSize(0, 33))
        self.block_decrypt_filename_widget.setMaximumSize(QSize(16777215, 33))
        self.horizontalLayout_20 = QHBoxLayout(self.block_decrypt_filename_widget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.block_decrrypt_filename_tittle = QLineEdit(self.block_decrypt_filename_widget)
        self.block_decrrypt_filename_tittle.setObjectName(u"block_decrrypt_filename_tittle")
        self.block_decrrypt_filename_tittle.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.block_decrrypt_filename_tittle.sizePolicy().hasHeightForWidth())
        self.block_decrrypt_filename_tittle.setSizePolicy(sizePolicy5)
        self.block_decrrypt_filename_tittle.setMinimumSize(QSize(90, 25))
        self.block_decrrypt_filename_tittle.setMaximumSize(QSize(90, 25))
        self.block_decrrypt_filename_tittle.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"")
        self.block_decrrypt_filename_tittle.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.block_decrrypt_filename_tittle)

        self.block_decrypt_filename = QTextEdit(self.block_decrypt_filename_widget)
        self.block_decrypt_filename.setObjectName(u"block_decrypt_filename")
        self.block_decrypt_filename.setMinimumSize(QSize(0, 25))
        self.block_decrypt_filename.setMaximumSize(QSize(16777215, 25))
        self.block_decrypt_filename.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_20.addWidget(self.block_decrypt_filename)


        self.verticalLayout.addWidget(self.block_decrypt_filename_widget)

        self.block_key_widget = QWidget(self.block_output_widget)
        self.block_key_widget.setObjectName(u"block_key_widget")
        self.block_key_widget.setMinimumSize(QSize(0, 60))
        self.block_key_widget.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_16 = QHBoxLayout(self.block_key_widget)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.block_key_icon = QPushButton(self.block_key_widget)
        self.block_key_icon.setObjectName(u"block_key_icon")
        self.block_key_icon.setEnabled(False)
        self.block_key_icon.setMinimumSize(QSize(0, 25))
        self.block_key_icon.setMaximumSize(QSize(16777215, 25))
        self.block_key_icon.setStyleSheet(u"border: none;")
        self.block_key_icon.setIcon(icon5)

        self.horizontalLayout_16.addWidget(self.block_key_icon)

        self.block_key_message = QLineEdit(self.block_key_widget)
        self.block_key_message.setObjectName(u"block_key_message")
        self.block_key_message.setEnabled(False)
        self.block_key_message.setMinimumSize(QSize(60, 25))
        self.block_key_message.setMaximumSize(QSize(60, 25))
        self.block_key_message.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: none;\n"
"border-radius: 10px;")
        self.block_key_message.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.block_key_message)

        self.block_key_output = QTextEdit(self.block_key_widget)
        self.block_key_output.setObjectName(u"block_key_output")
        self.block_key_output.setMinimumSize(QSize(0, 50))
        self.block_key_output.setMaximumSize(QSize(16777215, 50))
        self.block_key_output.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")

        self.horizontalLayout_16.addWidget(self.block_key_output)


        self.verticalLayout.addWidget(self.block_key_widget)

        self.block_decrypt_btn = QPushButton(self.block_output_widget)
        self.block_decrypt_btn.setObjectName(u"block_decrypt_btn")
        sizePolicy6.setHeightForWidth(self.block_decrypt_btn.sizePolicy().hasHeightForWidth())
        self.block_decrypt_btn.setSizePolicy(sizePolicy6)
        self.block_decrypt_btn.setMinimumSize(QSize(100, 0))
        self.block_decrypt_btn.setMaximumSize(QSize(500, 40))
        self.block_decrypt_btn.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.block_decrypt_btn.setIcon(icon4)

        self.verticalLayout.addWidget(self.block_decrypt_btn, 0, Qt.AlignHCenter)

        self.block_decrypt_output = QLabel(self.block_output_widget)
        self.block_decrypt_output.setObjectName(u"block_decrypt_output")
        sizePolicy.setHeightForWidth(self.block_decrypt_output.sizePolicy().hasHeightForWidth())
        self.block_decrypt_output.setSizePolicy(sizePolicy)
        self.block_decrypt_output.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"")
        self.block_decrypt_output.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.block_decrypt_output)


        self.block_horizontal_layout.addWidget(self.block_output_widget)


        self.horizontalLayout_15.addLayout(self.block_horizontal_layout)

        self.stackedWidget.addWidget(self.widgets)
        self.cryptoanalysis = QWidget()
        self.cryptoanalysis.setObjectName(u"cryptoanalysis")
        sizePolicy.setHeightForWidth(self.cryptoanalysis.sizePolicy().hasHeightForWidth())
        self.cryptoanalysis.setSizePolicy(sizePolicy)
        self.horizontalLayout_22 = QHBoxLayout(self.cryptoanalysis)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.cryptoanalysis_layout = QHBoxLayout()
        self.cryptoanalysis_layout.setObjectName(u"cryptoanalysis_layout")
        self.crypo_input_widget = QWidget(self.cryptoanalysis)
        self.crypo_input_widget.setObjectName(u"crypo_input_widget")
        sizePolicy.setHeightForWidth(self.crypo_input_widget.sizePolicy().hasHeightForWidth())
        self.crypo_input_widget.setSizePolicy(sizePolicy)
        self.verticalLayout_24 = QVBoxLayout(self.crypo_input_widget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.crypto_tittle = QLineEdit(self.crypo_input_widget)
        self.crypto_tittle.setObjectName(u"crypto_tittle")
        self.crypto_tittle.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.crypto_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.crypto_tittle)

        self.crypto_analysis_input = QTextEdit(self.crypo_input_widget)
        self.crypto_analysis_input.setObjectName(u"crypto_analysis_input")
        self.crypto_analysis_input.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")

        self.verticalLayout_24.addWidget(self.crypto_analysis_input)

        self.crypto_analysis_btn = QPushButton(self.crypo_input_widget)
        self.crypto_analysis_btn.setObjectName(u"crypto_analysis_btn")
        sizePolicy5.setHeightForWidth(self.crypto_analysis_btn.sizePolicy().hasHeightForWidth())
        self.crypto_analysis_btn.setSizePolicy(sizePolicy5)
        self.crypto_analysis_btn.setMinimumSize(QSize(100, 40))
        self.crypto_analysis_btn.setMaximumSize(QSize(100, 40))
        self.crypto_analysis_btn.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.crypto_analysis_btn.setIcon(icon10)

        self.verticalLayout_24.addWidget(self.crypto_analysis_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.cryptoanalysis_layout.addWidget(self.crypo_input_widget)

        self.crypto_output_widget = QWidget(self.cryptoanalysis)
        self.crypto_output_widget.setObjectName(u"crypto_output_widget")
        sizePolicy.setHeightForWidth(self.crypto_output_widget.sizePolicy().hasHeightForWidth())
        self.crypto_output_widget.setSizePolicy(sizePolicy)
        self.verticalLayout_25 = QVBoxLayout(self.crypto_output_widget)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.crypto_analysis_output = QTextEdit(self.crypto_output_widget)
        self.crypto_analysis_output.setObjectName(u"crypto_analysis_output")
        self.crypto_analysis_output.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")
        self.crypto_analysis_output.setReadOnly(True)

        self.verticalLayout_25.addWidget(self.crypto_analysis_output)


        self.cryptoanalysis_layout.addWidget(self.crypto_output_widget)


        self.horizontalLayout_22.addLayout(self.cryptoanalysis_layout)

        self.stackedWidget.addWidget(self.cryptoanalysis)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.horizontalLayout_8 = QHBoxLayout(self.new_page)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.public_key_combo = QWidget(self.new_page)
        self.public_key_combo.setObjectName(u"public_key_combo")
        sizePolicy.setHeightForWidth(self.public_key_combo.sizePolicy().hasHeightForWidth())
        self.public_key_combo.setSizePolicy(sizePolicy)
        self.public_key_combo.setMaximumSize(QSize(170, 16777215))
        self.public_key_combo.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_21 = QVBoxLayout(self.public_key_combo)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.public_key_list = QComboBox(self.public_key_combo)
        self.public_key_list.addItem("")
        self.public_key_list.addItem("")
        self.public_key_list.addItem("")
        self.public_key_list.addItem("")
        self.public_key_list.setObjectName(u"public_key_list")
        sizePolicy4.setHeightForWidth(self.public_key_list.sizePolicy().hasHeightForWidth())
        self.public_key_list.setSizePolicy(sizePolicy4)
        self.public_key_list.setMaximumSize(QSize(167, 32))
        self.public_key_list.setLayoutDirection(Qt.LeftToRight)
        self.public_key_list.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")
        self.public_key_list.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_21.addWidget(self.public_key_list, 0, Qt.AlignVCenter)

        self.public_key_generate_settings = QPushButton(self.public_key_combo)
        self.public_key_generate_settings.setObjectName(u"public_key_generate_settings")
        sizePolicy4.setHeightForWidth(self.public_key_generate_settings.sizePolicy().hasHeightForWidth())
        self.public_key_generate_settings.setSizePolicy(sizePolicy4)
        self.public_key_generate_settings.setMinimumSize(QSize(160, 30))
        self.public_key_generate_settings.setMaximumSize(QSize(160, 30))
        self.public_key_generate_settings.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-dialpad.png", QSize(), QIcon.Normal, QIcon.Off)
        self.public_key_generate_settings.setIcon(icon11)

        self.verticalLayout_21.addWidget(self.public_key_generate_settings, 0, Qt.AlignBottom)

        self.public_key_settings_output = QTextEdit(self.public_key_combo)
        self.public_key_settings_output.setObjectName(u"public_key_settings_output")
        self.public_key_settings_output.setMinimumSize(QSize(160, 100))
        self.public_key_settings_output.setMaximumSize(QSize(160, 100))
        self.public_key_settings_output.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.public_key_settings_output.setReadOnly(True)

        self.verticalLayout_21.addWidget(self.public_key_settings_output)


        self.horizontalLayout_8.addWidget(self.public_key_combo)

        self.public_input_widget = QWidget(self.new_page)
        self.public_input_widget.setObjectName(u"public_input_widget")
        self.verticalLayout_19 = QVBoxLayout(self.public_input_widget)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.public_encrypt_process = QLineEdit(self.public_input_widget)
        self.public_encrypt_process.setObjectName(u"public_encrypt_process")
        self.public_encrypt_process.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.public_encrypt_process.setAlignment(Qt.AlignCenter)
        self.public_encrypt_process.setReadOnly(True)

        self.verticalLayout_19.addWidget(self.public_encrypt_process)

        self.public_encrypt_input = QTextEdit(self.public_input_widget)
        self.public_encrypt_input.setObjectName(u"public_encrypt_input")
        self.public_encrypt_input.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")

        self.verticalLayout_19.addWidget(self.public_encrypt_input)

        self.public_public_key_widget = QWidget(self.public_input_widget)
        self.public_public_key_widget.setObjectName(u"public_public_key_widget")
        self.public_public_key_widget.setMinimumSize(QSize(0, 40))
        self.public_public_key_widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_12 = QHBoxLayout(self.public_public_key_widget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.public_key_icon = QPushButton(self.public_public_key_widget)
        self.public_key_icon.setObjectName(u"public_key_icon")
        self.public_key_icon.setEnabled(False)
        self.public_key_icon.setMinimumSize(QSize(0, 30))
        self.public_key_icon.setMaximumSize(QSize(16777215, 30))
        self.public_key_icon.setStyleSheet(u"border: none;")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-transfer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.public_key_icon.setIcon(icon12)

        self.horizontalLayout_12.addWidget(self.public_key_icon)

        self.public_key_line = QLineEdit(self.public_public_key_widget)
        self.public_key_line.setObjectName(u"public_key_line")
        sizePolicy.setHeightForWidth(self.public_key_line.sizePolicy().hasHeightForWidth())
        self.public_key_line.setSizePolicy(sizePolicy)
        self.public_key_line.setMinimumSize(QSize(90, 30))
        self.public_key_line.setMaximumSize(QSize(90, 30))
        self.public_key_line.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: nonee;\n"
"border-radius: 10px;")
        self.public_key_line.setAlignment(Qt.AlignCenter)
        self.public_key_line.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.public_key_line)

        self.public_key_input = QTextEdit(self.public_public_key_widget)
        self.public_key_input.setObjectName(u"public_key_input")
        self.public_key_input.setMinimumSize(QSize(0, 30))
        self.public_key_input.setMaximumSize(QSize(16777215, 30))
        self.public_key_input.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")

        self.horizontalLayout_12.addWidget(self.public_key_input)


        self.verticalLayout_19.addWidget(self.public_public_key_widget)

        self.public_btn_encrypt = QPushButton(self.public_input_widget)
        self.public_btn_encrypt.setObjectName(u"public_btn_encrypt")
        sizePolicy4.setHeightForWidth(self.public_btn_encrypt.sizePolicy().hasHeightForWidth())
        self.public_btn_encrypt.setSizePolicy(sizePolicy4)
        self.public_btn_encrypt.setMinimumSize(QSize(100, 0))
        self.public_btn_encrypt.setMaximumSize(QSize(500, 40))
        self.public_btn_encrypt.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.public_btn_encrypt.setIcon(icon4)

        self.verticalLayout_19.addWidget(self.public_btn_encrypt, 0, Qt.AlignHCenter)

        self.public_encrypt_output = QTextEdit(self.public_input_widget)
        self.public_encrypt_output.setObjectName(u"public_encrypt_output")
        self.public_encrypt_output.setMaximumSize(QSize(16777215, 100))
        self.public_encrypt_output.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.public_encrypt_output.setReadOnly(True)

        self.verticalLayout_19.addWidget(self.public_encrypt_output)


        self.horizontalLayout_8.addWidget(self.public_input_widget)

        self.public_vertical_line = QFrame(self.new_page)
        self.public_vertical_line.setObjectName(u"public_vertical_line")
        self.public_vertical_line.setStyleSheet(u"border-width: 5px;\n"
" border-style: solid; \n"
"border-color: violet;")
        self.public_vertical_line.setFrameShape(QFrame.VLine)
        self.public_vertical_line.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.public_vertical_line)

        self.public_output_widget = QWidget(self.new_page)
        self.public_output_widget.setObjectName(u"public_output_widget")
        self.verticalLayout_20 = QVBoxLayout(self.public_output_widget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.public_decrypt_process = QLineEdit(self.public_output_widget)
        self.public_decrypt_process.setObjectName(u"public_decrypt_process")
        self.public_decrypt_process.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.public_decrypt_process.setAlignment(Qt.AlignCenter)
        self.public_decrypt_process.setReadOnly(True)

        self.verticalLayout_20.addWidget(self.public_decrypt_process)

        self.public_decrypt_input = QTextEdit(self.public_output_widget)
        self.public_decrypt_input.setObjectName(u"public_decrypt_input")
        self.public_decrypt_input.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")
        self.public_decrypt_input.setReadOnly(False)

        self.verticalLayout_20.addWidget(self.public_decrypt_input)

        self.public_private_key_widget = QWidget(self.public_output_widget)
        self.public_private_key_widget.setObjectName(u"public_private_key_widget")
        self.public_private_key_widget.setMinimumSize(QSize(0, 40))
        self.public_private_key_widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_13 = QHBoxLayout(self.public_private_key_widget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.private_key_icon = QPushButton(self.public_private_key_widget)
        self.private_key_icon.setObjectName(u"private_key_icon")
        self.private_key_icon.setEnabled(False)
        self.private_key_icon.setMinimumSize(QSize(0, 30))
        self.private_key_icon.setMaximumSize(QSize(16777215, 30))
        self.private_key_icon.setStyleSheet(u"border: none;")
        self.private_key_icon.setIcon(icon5)

        self.horizontalLayout_13.addWidget(self.private_key_icon)

        self.private_key_line = QLineEdit(self.public_private_key_widget)
        self.private_key_line.setObjectName(u"private_key_line")
        sizePolicy.setHeightForWidth(self.private_key_line.sizePolicy().hasHeightForWidth())
        self.private_key_line.setSizePolicy(sizePolicy)
        self.private_key_line.setMinimumSize(QSize(90, 30))
        self.private_key_line.setMaximumSize(QSize(90, 30))
        self.private_key_line.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: none;\n"
"border-radius: 10px;")
        self.private_key_line.setAlignment(Qt.AlignCenter)
        self.private_key_line.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.private_key_line)

        self.private_key_input = QTextEdit(self.public_private_key_widget)
        self.private_key_input.setObjectName(u"private_key_input")
        self.private_key_input.setMinimumSize(QSize(0, 30))
        self.private_key_input.setMaximumSize(QSize(16777215, 30))
        self.private_key_input.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid violet;\n"
"border-radius: 10px;")

        self.horizontalLayout_13.addWidget(self.private_key_input)


        self.verticalLayout_20.addWidget(self.public_private_key_widget)

        self.public_btn_decrypt = QPushButton(self.public_output_widget)
        self.public_btn_decrypt.setObjectName(u"public_btn_decrypt")
        sizePolicy4.setHeightForWidth(self.public_btn_decrypt.sizePolicy().hasHeightForWidth())
        self.public_btn_decrypt.setSizePolicy(sizePolicy4)
        self.public_btn_decrypt.setMinimumSize(QSize(100, 0))
        self.public_btn_decrypt.setMaximumSize(QSize(500, 40))
        self.public_btn_decrypt.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.public_btn_decrypt.setIcon(icon6)

        self.verticalLayout_20.addWidget(self.public_btn_decrypt, 0, Qt.AlignHCenter)

        self.public_decrypt_output = QTextEdit(self.public_output_widget)
        self.public_decrypt_output.setObjectName(u"public_decrypt_output")
        self.public_decrypt_output.setMaximumSize(QSize(16777215, 100))
        self.public_decrypt_output.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.public_decrypt_output.setReadOnly(True)

        self.verticalLayout_20.addWidget(self.public_decrypt_output)


        self.horizontalLayout_8.addWidget(self.public_output_widget)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_26.addWidget(self.stackedWidget)


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
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setBold(False)
        font7.setItalic(False)
        self.creditsLabel.setFont(font7)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"SecretSafe", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern Cryptography APP", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_classical.setText(QCoreApplication.translate("MainWindow", u"Classical Encryption", None))
        self.btn_block.setText(QCoreApplication.translate("MainWindow", u"Image Encryption", None))
        self.btn_public_key.setText(QCoreApplication.translate("MainWindow", u"Public Key Encryption", None))
        self.btn_analysis.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
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
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; "
                        "margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"SECRET SAFE", None))
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
        self.classical_list.setItemText(0, QCoreApplication.translate("MainWindow", u"Shift", None))
        self.classical_list.setItemText(1, QCoreApplication.translate("MainWindow", u"Sustitution", None))
        self.classical_list.setItemText(2, QCoreApplication.translate("MainWindow", u"Vigenere", None))
        self.classical_list.setItemText(3, QCoreApplication.translate("MainWindow", u"Affine", None))
        self.classical_list.setItemText(4, QCoreApplication.translate("MainWindow", u"Hill", None))

        self.classical_encrypt_process.setText(QCoreApplication.translate("MainWindow", u"ENCRYPT PROCESS", None))
        self.classical_generated_key_icon.setText("")
        self.classica_generated_key_line.setText(QCoreApplication.translate("MainWindow", u"Generated Key", None))
        self.classical_btn_encrypt.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.classical_decrypt_process.setText(QCoreApplication.translate("MainWindow", u"DECRYPT PROCESS", None))
        self.classical_decrypt_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.classical_key_icon.setText("")
        self.classical_key_line.setText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.classical_btn_decrypt.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.welcome_page_tittle.setText(QCoreApplication.translate("MainWindow", u"WHAT DOES SECRETSAFE DO FOR YOU?", None))
        self.welcome_page_description.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">This is an application that addresses the need for privacy and security in a virtual world. Focusing on internet text messaging, Secret Safe allows the encryption of two key forms of information: text and images. Classic, block, and public key encryptions are employed to cater to different user preferences. Lastly, it provides a cryptanalysis tool to playfully demonstrate the vulnerabilities of classic ciphers.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px;"
                        " margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">We hope that Secret Safe proves valuable in your everyday life.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Best regards,</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Development Team:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">- Santiago Tovar Mosquera</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">- Juliana Nieto C\u00e1rdenas</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">- Anderson Andr\u00e9s Llanos Quintero</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">- Daniel Estevan Garcia Ni\u00f1o</span></p></body></html>", None))
        self.welcome_page_image.setText("")
        self.block_list.setItemText(0, QCoreApplication.translate("MainWindow", u"AES", None))
        self.block_list.setItemText(1, QCoreApplication.translate("MainWindow", u"S-DES", None))
        self.block_list.setItemText(2, QCoreApplication.translate("MainWindow", u"T-DES", None))
        self.block_list.setItemText(3, QCoreApplication.translate("MainWindow", u"HILL", None))

        self.block_mode_btn.setText(QCoreApplication.translate("MainWindow", u"MODE", None))
        self.block_mode_list.setItemText(0, QCoreApplication.translate("MainWindow", u"CBC", None))
        self.block_mode_list.setItemText(1, QCoreApplication.translate("MainWindow", u"CTR", None))
        self.block_mode_list.setItemText(2, QCoreApplication.translate("MainWindow", u"ECB", None))
        self.block_mode_list.setItemText(3, QCoreApplication.translate("MainWindow", u"OFB", None))

        self.block_encrypt_process.setText(QCoreApplication.translate("MainWindow", u"ENCRYPT PROCESS", None))
        self.block_encrypt_filepath_btn.setText("")
        self.block_encrypt_filename_tittle.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.block_generate_key_btn.setText("")
        self.block_geenerate_key_message.setText(QCoreApplication.translate("MainWindow", u"Generate Key", None))
        self.block_encrypt_btn.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.block_encrypt_output.setText("")
        self.block_decrypt_process.setText(QCoreApplication.translate("MainWindow", u"DECRYPT PROCESS", None))
        self.block_decrypt_filepath_btn.setText("")
        self.block_decrrypt_filename_tittle.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.block_key_icon.setText("")
        self.block_key_message.setText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.block_decrypt_btn.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.block_decrypt_output.setText("")
        self.crypto_tittle.setText(QCoreApplication.translate("MainWindow", u"CRYPTOANALYSIS", None))
        self.crypto_analysis_btn.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.public_key_list.setItemText(0, QCoreApplication.translate("MainWindow", u"RSA", None))
        self.public_key_list.setItemText(1, QCoreApplication.translate("MainWindow", u"Rabin", None))
        self.public_key_list.setItemText(2, QCoreApplication.translate("MainWindow", u"ElGamal", None))
        self.public_key_list.setItemText(3, QCoreApplication.translate("MainWindow", u"Menezes-Vanstone", None))

        self.public_key_generate_settings.setText(QCoreApplication.translate("MainWindow", u"Generate Setting", None))
        self.public_encrypt_process.setText(QCoreApplication.translate("MainWindow", u"ENCRYPT PROCESS", None))
        self.public_key_icon.setText("")
        self.public_key_line.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.public_btn_encrypt.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.public_decrypt_process.setText(QCoreApplication.translate("MainWindow", u"DECRYPT PROCESS", None))
        self.private_key_icon.setText("")
        self.private_key_line.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.public_btn_decrypt.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Keep your secret safe", None))
    # retranslateUi

