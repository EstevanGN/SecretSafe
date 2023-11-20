# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
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

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from cryptosystems import shift, afin, vigenere #, Menezes
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "SECRET SAFE"
        description = "SECRET SAFE"
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
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_classical.clicked.connect(self.buttonClick)
        widgets.btn_block.clicked.connect(self.buttonClick)
        widgets.btn_public_key.clicked.connect(self.buttonClick)
        widgets.btn_analysis.clicked.connect(self.buttonClick)
        
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        #widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        #widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        #widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.welcome_page)
        widgets.btn_classical.setStyleSheet(UIFunctions.selectMenu(widgets.btn_classical.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_classical":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ui.classical_list.currentIndexChanged.connect(self.classical_encryption_choice_action)
        # SHOW WIDGETS PAGE
        if btnName == "btn_block":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ui.pushButton.clicked.connect(self.open_file)

        # SHOW NEW PAGE
        if btnName == "btn_public_key":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            # AQUI
            self.ui.public_key_list.currentIndexChanged.connect(self.public_key_encryption_choice_action)

        if btnName == "btn_analysis":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

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
            
    def shift_encrypt_text(self):
        input_text = self.ui.classical_encrypt_input.toPlainText()
        shift_encrypt_return = shift.cifrar_desplazamiento(input_text)
        output_text = shift_encrypt_return[0]
        generated_key = shift_encrypt_return[1]
        self.ui.classical_generated_key_output.setPlainText(str(generated_key))
        self.ui.classical_encrypt_output.setPlainText(str(output_text))
    
    def shift_decrypt_text(self):
        input_text = self.ui.classical_decrypt_input.toPlainText()
        key = int(self.ui.classical_key_input.toPlainText())
        output_text = shift.descifrar_desplazamiento(input_text, key)
        self.ui.classical_decrypt_output.setPlainText(output_text)
        
    def affine_encrypt_text(self):
        input_text = self.ui.classical_encrypt_input.toPlainText()
        affine_encrypt_return = afin.cifrar_afin(input_text)
        output_text = affine_encrypt_return[0]
        generated_key_1 = affine_encrypt_return[1]
        generated_key_2 = affine_encrypt_return[2]
        self.ui.classical_generated_key_output.setPlainText("(" + str(generated_key_1) + ", " + str(generated_key_2) + ")")
        self.ui.classical_encrypt_output.setPlainText(str(output_text))
        
    def affine_decrypt_text(self):
        input_text = self.ui.classical_decrypt_input.toPlainText()
        t = eval(self.ui.classical_key_input.toPlainText())
        key_1, key_2 = t
        output_text = afin.descifrar_afin(input_text, key_1, key_2)
        self.ui.classical_decrypt_output.setPlainText(output_text)
        
    def classical_encryption_choice_action(self):
        index = self.ui.classical_list.currentIndex()
        if index == 0:
            self.ui.classical_btn_encrypt.clicked.connect(self.shift_encrypt_text)
            self.ui.classical_btn_decrypt.clicked.connect(self.shift_decrypt_text)
        elif index == 3:
            self.ui.classical_btn_encrypt.clicked.connect(self.affine_encrypt_text)
            self.ui.classical_btn_decrypt.clicked.connect(self.affine_decrypt_text)
            
    def public_key_encryption_choice_action(self):
        print("Public key")
        
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Todos los archivos (*)")
        if file_name:
            os.startfile(file_name)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
