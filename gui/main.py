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
import ast
import numpy as np
import struct

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from cryptosystems import rabin,RSA,shift, afin, vigenere, sust_permu, hill, Menezes, aes_image_encryption, SDES, triple_des
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
        # Classical Global Variables
        self.current_generate_key_function = None
        self.current_encrypt_function = None
        self.current_decrypt_function = None
        # Block Global Variables
        self.current_block_generate_key_function = None
        self.current_block_encrypt_function = None
        self.current_block_decrypt_function = None
        global widgets
        widgets = self.ui
        # Classical Global Variables
        self.current_public_generate_key_function = None
        self.current_public_encrypt_function = None
        self.current_public_decrypt_function = None
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
            self.ui.classical_list.setCurrentIndex(1)
            self.ui.classical_list.setCurrentIndex(0)
        # SHOW WIDGETS PAGE
        if btnName == "btn_block":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ui.block_encrypt_filepath_btn.clicked.connect(self.open_file)
            self.ui.block_decrypt_filepath_btn.clicked.connect(self.open_file_decrypt)
            #self.ui.block_generate_key_btn.clicked.connect(self.aes_generate_key)
            #self.ui.block_encrypt_btn.clicked.connect(self.aes_encrypt_image)
            #self.ui.block_decrypt_btn.clicked.connect(self.aes_decrypt_image)
            self.ui.block_list.currentIndexChanged.connect(self.block_encryption_choice_action)
            self.ui.block_mode_list.currentIndexChanged.connect(self.block_encryption_choice_action)
            self.ui.block_list.setCurrentIndex(1)
            self.ui.block_list.setCurrentIndex(0)
            self.ui.block_mode_list.setCurrentIndex(1)
            self.ui.block_mode_list.setCurrentIndex(0)

        # SHOW NEW PAGE
        if btnName == "btn_public_key":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            # AQUI
            self.ui.public_key_list.currentIndexChanged.connect(self.public_key_encryption_choice_action)
            self.ui.public_key_list.setCurrentIndex(1)
            self.ui.public_key_list.setCurrentIndex(0)

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
    
    ##########################################################################################################################################################################
    
    def shift_generate_key(self):
        generated_key = shift.generar_clave_desplazamiento()
        self.ui.classical_generated_key_output.setPlainText(str(generated_key))
        
    def sustitution_permutation_generate_key(self):
        if self.ui.classical_encrypt_input.toPlainText():
            generated_key = sust_permu.generar_claves(self.ui.classical_encrypt_input.toPlainText())
            blocks = generated_key[0]
            final_permutation = generated_key[1]
            block_length = generated_key[2]
            self.ui.classical_generated_key_output.setPlainText("Blocks : " + str(blocks) + " - Permutation : " + str(final_permutation) + " - Block Lenght : " + str(block_length))
    
    def vigenere_generate_key(self):
        if self.ui.classical_encrypt_input.toPlainText():
            generated_key = vigenere.generar_clave_vigenere(self.ui.classical_encrypt_input.toPlainText())
            self.ui.classical_generated_key_output.setPlainText(str(generated_key))
            
    def affine_generate_key(self):
        generated_keys = afin.generar_claves_afin()
        a = generated_keys[0]
        b = generated_keys[1]
        self.ui.classical_generated_key_output.setPlainText("(" + str(a) + ", " + str(b) + ")")
        
    def hill_generate_key(self):
        generated_key = hill.generar_matriz_clave()
        self.ui.classical_generated_key_output.setPlainText(str(generated_key))
            
    def shift_encrypt_text(self):
        input_text = self.ui.classical_encrypt_input.toPlainText()
        if self.ui.classical_generated_key_output.toPlainText():
            generated_key = int(self.ui.classical_generated_key_output.toPlainText())
            output_text = shift.cifrar_desplazamiento(input_text, generated_key)
            self.ui.classical_encrypt_output.setPlainText(str(output_text))
    
    def shift_decrypt_text(self):
        input_text = self.ui.classical_decrypt_input.toPlainText()
        key = int(self.ui.classical_key_input.toPlainText())
        output_text = shift.descifrar_desplazamiento(input_text, key)
        self.ui.classical_decrypt_output.setPlainText(output_text)
        
    def sustitution_permutation_encrypt_text(self):
        input_text = self.ui.classical_encrypt_input.toPlainText()
        if self.ui.classical_generated_key_output.toPlainText():
            key_values = self.ui.classical_generated_key_output.toPlainText().split(" - ")
            key_blocks = ast.literal_eval(key_values[0].split(" : ")[1])
            final_permutation = ast.literal_eval(key_values[1].split(" : ")[1])
            block_length = int(key_values[2].split(" : ")[1])
            output_text = sust_permu.cifrar_sustPermu(input_text, block_length, key_blocks, final_permutation)
            self.ui.classical_generated_key_output.setPlainText("Blocks : " + str(key_blocks) + " - Permutation : " + str(final_permutation) + " - Block Length : " + str(block_length))
            self.ui.classical_encrypt_output.setPlainText(str(output_text))
        
    def sustitution_permutation_decrypt_text(self):
        input_text = self.ui.classical_decrypt_input.toPlainText()
        key_inputs = self.ui.classical_key_input.toPlainText().split(" - ")
        key_blocks = ast.literal_eval(key_inputs[0].split(" : ")[1])
        final_permutation = ast.literal_eval(key_inputs[1].split(" : ")[1])
        output_text = sust_permu.descifrar_sustPermu(input_text, key_blocks, final_permutation)
        self.ui.classical_decrypt_output.setPlainText(output_text)
        
    def vigenere_encrypt_text(self):
        input_text = self.ui.classical_encrypt_input.toPlainText()
        if self.ui.classical_generated_key_output.toPlainText():
            key = self.ui.classical_generated_key_output.toPlainText()
            output_text = vigenere.cifrar_vigenere(input_text, key)
            self.ui.classical_generated_key_output.setPlainText(str(key))
            self.ui.classical_encrypt_output.setPlainText(str(output_text))
        
    def vigener_decrypt_text(self):
        input_text = self.ui.classical_decrypt_input.toPlainText()
        key = self.ui.classical_key_input.toPlainText()
        output_text = vigenere.descifrar_vigenere(input_text, key)
        self.ui.classical_decrypt_output.setPlainText(output_text)
        
    def affine_encrypt_text(self):
        input_text = self.ui.classical_encrypt_input.toPlainText()
        if self.ui.classical_generated_key_output.toPlainText():
            keys = eval(self.ui.classical_generated_key_output.toPlainText())
            a, b = keys
            output_text = afin.cifrar_afin(input_text, a, b)
            self.ui.classical_generated_key_output.setPlainText("(" + str(a) + ", " + str(b) + ")")
            self.ui.classical_encrypt_output.setPlainText(str(output_text))
        
    def affine_decrypt_text(self):
        input_text = self.ui.classical_decrypt_input.toPlainText()
        t = eval(self.ui.classical_key_input.toPlainText())
        key_1, key_2 = t
        output_text = afin.descifrar_afin(input_text, key_1, key_2)
        self.ui.classical_decrypt_output.setPlainText(output_text)
        
    def hill_encrypt_text(self):
        input_text = self.ui.classical_encrypt_input.toPlainText()
        if self.ui.classical_generated_key_output.toPlainText():
            matrix_key = np.matrix(self.ui.classical_generated_key_output.toPlainText())
            output_text = hill.cifrar_hill(input_text, matrix_key)
            self.ui.classical_generated_key_output.setPlainText(str(matrix_key))
            self.ui.classical_encrypt_output.setPlainText(str(output_text))
        
    def hill_decrypt_text(self):
        input_text = self.ui.classical_decrypt_input.toPlainText()
        key = np.matrix(self.ui.classical_key_input.toPlainText())
        output_text = hill.descifrar_hill(input_text, key)
        self.ui.classical_decrypt_output.setPlainText(output_text)
        
    def classical_encryption_choice_action(self):
        index = self.ui.classical_list.currentIndex()
        if self.current_encrypt_function is not None:
            self.ui.classical_btn_encrypt.clicked.disconnect(self.current_encrypt_function)
        if self.current_decrypt_function is not None:
            self.ui.classical_btn_decrypt.clicked.disconnect(self.current_decrypt_function)
        if self.current_generate_key_function is not None:
            self.ui.classical_generated_key_icon.clicked.disconnect(self.current_generate_key_function)
        if index == 0:
            self.ui.classical_generated_key_output.setPlainText("")
            self.ui.classical_key_input.setPlainText("")
            self.current_generate_key_function = self.shift_generate_key
            self.current_encrypt_function = self.shift_encrypt_text
            self.current_decrypt_function = self.shift_decrypt_text
        elif index == 1:
            self.ui.classical_generated_key_output.setPlainText("")
            self.ui.classical_key_input.setPlainText("")
            self.current_generate_key_function = self.sustitution_permutation_generate_key
            self.current_encrypt_function = self.sustitution_permutation_encrypt_text
            self.current_decrypt_function = self.sustitution_permutation_decrypt_text
        elif index == 2:
            self.ui.classical_generated_key_output.setPlainText("")
            self.ui.classical_key_input.setPlainText("")
            self.current_generate_key_function = self.vigenere_generate_key
            self.current_encrypt_function = self.vigenere_encrypt_text
            self.current_decrypt_function = self.vigener_decrypt_text
        elif index == 3:
            self.ui.classical_generated_key_output.setPlainText("")
            self.ui.classical_key_input.setPlainText("")
            self.current_generate_key_function = self.affine_generate_key
            self.current_encrypt_function = self.affine_encrypt_text
            self.current_decrypt_function = self.affine_decrypt_text
        elif index == 4:
            self.ui.classical_generated_key_output.setPlainText("")
            self.ui.classical_key_input.setPlainText("")
            self.current_generate_key_function = self.hill_generate_key
            self.current_encrypt_function = self.hill_encrypt_text
            self.current_decrypt_function = self.hill_decrypt_text
        # Set the specific slot for the given index
        self.ui.classical_generated_key_icon.clicked.connect(self.current_generate_key_function)
        self.ui.classical_btn_encrypt.clicked.connect(self.current_encrypt_function)
        self.ui.classical_btn_decrypt.clicked.connect(self.current_decrypt_function)
    
    ##########################################################################################################################################################################
    
    
    def RSA_generate_key(self):
        self.ui.public_encrypt_output.setPlainText("")
        self.ui.public_decrypt_output.setPlainText("")
        self.ui.public_key_settings_output.setPlainText("")
        generated_key = RSA.generar_claves()
        self.ui.public_key_input.setPlainText(str(generated_key[0]))
        self.ui.private_key_input.setPlainText(str(generated_key[1]))
        self.ui.public_key_settings_output.setPlainText(str(generated_key[2]))

    def RSA_encrypt_text(self):
        input_text = self.ui.public_encrypt_input.toPlainText()
        if self.ui.public_encrypt_input.toPlainText():
            generated_key = eval(self.ui.public_key_input.toPlainText())
            output_text = RSA.cifrar(input_text, generated_key)
            self.ui.public_encrypt_output.setPlainText(str(output_text))

    def RSA_decrypt_text(self):
        input_text = self.ui.public_decrypt_input.toPlainText()
        if self.ui.public_decrypt_input.toPlainText():
            generated_key = eval(self.ui.private_key_input.toPlainText())
            output_text = RSA.descifrar(ast.literal_eval(input_text), generated_key)
            self.ui.public_decrypt_output.setPlainText(str(output_text))    
    
    def rabin_generate_key(self):
        self.ui.public_encrypt_output.setPlainText("")
        self.ui.public_decrypt_output.setPlainText("")
        self.ui.public_key_settings_output.setPlainText("")
        generated_key = rabin.generar_claves()
        self.ui.public_key_input.setPlainText(str(generated_key[0]))
        self.ui.private_key_input.setPlainText(str(generated_key[1]))

    def rabin_encrypt_text(self):
        input_text = self.ui.public_encrypt_input.toPlainText()
        if self.ui.public_encrypt_input.toPlainText():
            generated_key = eval(self.ui.public_key_input.toPlainText())
            output_text = rabin.cifrar(input_text, generated_key)
            self.ui.public_encrypt_output.setPlainText(str(output_text))


    def rabin_decrypt_text(self):
        input_text = self.ui.public_decrypt_input.toPlainText()
        if self.ui.public_decrypt_input.toPlainText():
            generated_key = eval(self.ui.private_key_input.toPlainText())
            output_text = rabin.descifrar(int(input_text), generated_key, eval(self.ui.public_key_input.toPlainText())[1])
            self.ui.public_decrypt_output.setPlainText(str(output_text))            


    
    def public_key_encryption_choice_action(self):
        index = self.ui.public_key_list.currentIndex()
        if self.current_public_encrypt_function is not None:
            self.ui.public_btn_encrypt.clicked.disconnect(self.current_public_encrypt_function)
        if self.current_public_decrypt_function is not None:
            self.ui.public_btn_decrypt.clicked.disconnect(self.current_public_decrypt_function)
        if self.current_public_generate_key_function is not None:
            self.ui.public_key_generate_settings.clicked.disconnect(self.current_public_generate_key_function)
        if index == 0:
            self.ui.public_key_input.setPlainText("")
            self.ui.private_key_input.setPlainText("")
            self.ui.public_key_settings_output.setPlainText("")
            self.current_public_generate_key_function = self.RSA_generate_key
            self.current_public_encrypt_function = self.RSA_encrypt_text
            self.current_public_decrypt_function = self.RSA_decrypt_text
        elif index == 1:
            self.ui.public_key_input.setPlainText("")
            self.ui.private_key_input.setPlainText("")
            self.ui.public_key_settings_output.setPlainText("")
            self.current_public_generate_key_function = self.rabin_generate_key
            self.current_public_encrypt_function = self.rabin_encrypt_text
            self.current_public_decrypt_function = self.rabin_decrypt_text        
        self.ui.public_key_generate_settings.clicked.connect(self.current_public_generate_key_function)
        self.ui.public_btn_encrypt.clicked.connect(self.current_public_encrypt_function)
        self.ui.public_btn_decrypt.clicked.connect(self.current_public_decrypt_function)
        
    ##########################################################################################################################################################################
    
    def aes_generate_key(self):
        generated_key = aes_image_encryption.aes_generate_key()
        self.ui.block_generate_key_output.setPlainText(str(generated_key))
        
    def sdes_generate_key(self):
        generated_key = SDES.sdes_generate_key()
        self.ui.block_generate_key_output.setPlainText(str(generated_key))
        
    def tdes_generate_key(self):
        generated_key = triple_des.tdes_generate_key()
        self.ui.block_generate_key_output.setPlainText(str(generated_key))
        
    def aes_encrypt_image(self):
        image_path = self.ui.block_encrypt_filepath.text()
        if self.ui.block_generate_key_output.toPlainText():
            aes_key = ast.literal_eval(self.ui.block_generate_key_output.toPlainText())
            key = struct.pack('16B', *aes_key)
            encrypt_image_return = aes_image_encryption.cifrar_imagen(image_path, key)
            encrypted_image_path = encrypt_image_return[0]
            mode = str(encrypt_image_return[1])
            pixmap = QPixmap(encrypted_image_path)
            self.ui.block_encrypt_output.setPixmap(pixmap)
            self.ui.block_generate_key_output.setPlainText("Key : " + self.ui.block_generate_key_output.toPlainText() + " - Mode : " + mode)
            
    def aes_decrypt_image(self):
        image_path = self.ui.block_decrypt_filepath.text()
        all_key = self.ui.block_key_output.toPlainText().split(" - ")
        aes_key = ast.literal_eval(all_key[0].split(" : ")[1])
        aes_mode = ast.literal_eval(all_key[1].split(" : ")[1])
        key = struct.pack('16B', *aes_key)
        mode = struct.pack('16B', *aes_mode)
        decrypted_image_path = aes_image_encryption.descifrar_imagen(image_path, key, mode)
        pixmap = QPixmap(decrypted_image_path)
        self.ui.block_decrypt_output.setPixmap(pixmap)
        
    def aes_encrypt_image_ecb(self):
        image_path = self.ui.block_encrypt_filepath.text()
        if self.ui.block_generate_key_output.toPlainText():
            aes_key = ast.literal_eval(self.ui.block_generate_key_output.toPlainText())
            key = struct.pack('16B', *aes_key)
            encrypted_image_path = aes_image_encryption.cifrar_imagen_ecb(image_path, key)
            pixmap = QPixmap(encrypted_image_path)
            self.ui.block_encrypt_output.setPixmap(pixmap)
            self.ui.block_generate_key_output.setPlainText("Key : " + self.ui.block_generate_key_output.toPlainText())
        
    def aes_encrypt_image_ctr(self):
        image_path = self.ui.block_encrypt_filepath.text()
        if self.ui.block_generate_key_output.toPlainText():
            aes_key = ast.literal_eval(self.ui.block_generate_key_output.toPlainText())
            key = struct.pack('16B', *aes_key)
            encrypted_image_path = aes_image_encryption.cifrar_imagen_ctr(image_path, key)
            pixmap = QPixmap(encrypted_image_path)
            self.ui.block_encrypt_output.setPixmap(pixmap)
            self.ui.block_generate_key_output.setPlainText("Key : " + self.ui.block_generate_key_output.toPlainText())
        
    def aes_decrypt_image_ecb(self):
        image_path = self.ui.block_decrypt_filepath.text()
        aes_key = ast.literal_eval(self.ui.block_key_output.toPlainText().split(" : ")[1])
        key = struct.pack('16B', *aes_key)
        decrypted_image_path = aes_image_encryption.descifrar_imagen_ecb(image_path, key)
        pixmap = QPixmap(decrypted_image_path)
        self.ui.block_decrypt_output.setPixmap(pixmap)
        
    def aes_decrypt_image_ctr(self):
        image_path = self.ui.block_decrypt_filepath.text()
        aes_key = ast.literal_eval(self.ui.block_key_output.toPlainText().split(" : ")[1])
        key = struct.pack('16B', *aes_key)
        decrypted_image_path = aes_image_encryption.descifrar_imagen_ctr(image_path, key)
        pixmap = QPixmap(decrypted_image_path)
        self.ui.block_decrypt_output.setPixmap(pixmap)
    
    def sdes_encrypt_image(self):
        image_path = self.ui.block_encrypt_filepath.text()
        if self.ui.block_generate_key_output.toPlainText():
            aes_key = ast.literal_eval(self.ui.block_generate_key_output.toPlainText())
            key = struct.pack('8B', *aes_key)
            encrypt_image_return = SDES.cifrar_imagen(image_path, key)
            encrypted_image_path = encrypt_image_return[0]
            mode = str(encrypt_image_return[1])
            pixmap = QPixmap(encrypted_image_path)
            self.ui.block_encrypt_output.setPixmap(pixmap)
            self.ui.block_generate_key_output.setPlainText("Key : " + self.ui.block_generate_key_output.toPlainText() + " - Mode : " + mode)
        
    def sdes_encrypt_image_ecb(self):
        image_path = self.ui.block_encrypt_filepath.text()
        if self.ui.block_generate_key_output.toPlainText():
            aes_key = ast.literal_eval(self.ui.block_generate_key_output.toPlainText())
            key = struct.pack('8B', *aes_key)
            encrypted_image_path = SDES.cifrar_imagen_ecb(image_path, key)
            pixmap = QPixmap(encrypted_image_path)
            self.ui.block_encrypt_output.setPixmap(pixmap)
            self.ui.block_generate_key_output.setPlainText("Key : " + self.ui.block_generate_key_output.toPlainText())
        
    def sdes_encrypt_image_ctr(self):
        image_path = self.ui.block_encrypt_filepath.text()
        if self.ui.block_generate_key_output.toPlainText():
            aes_key = ast.literal_eval(self.ui.block_generate_key_output.toPlainText())
            key = struct.pack('8B', *aes_key)
            encrypted_image_path = SDES.cifrar_imagen_ctr(image_path, key)
            pixmap = QPixmap(encrypted_image_path)
            self.ui.block_encrypt_output.setPixmap(pixmap)
            self.ui.block_generate_key_output.setPlainText("Key : " + self.ui.block_generate_key_output.toPlainText())
    
    def sdes_decrypt_image(self):
        image_path = self.ui.block_decrypt_filepath.text()
        all_key = self.ui.block_key_output.toPlainText().split(" - ")
        aes_key = ast.literal_eval(all_key[0].split(" : ")[1])
        aes_mode = ast.literal_eval(all_key[1].split(" : ")[1])
        key = struct.pack('8B', *aes_key)
        mode = struct.pack('8B', *aes_mode)
        decrypted_image_path = SDES.descifrar_imagen(image_path, key, mode)
        pixmap = QPixmap(decrypted_image_path)
        self.ui.block_decrypt_output.setPixmap(pixmap)
        
    def sdes_decrypt_image_ecb(self):
        image_path = self.ui.block_decrypt_filepath.text()
        aes_key = ast.literal_eval(self.ui.block_key_output.toPlainText().split(" : ")[1])
        key = struct.pack('8B', *aes_key)
        decrypted_image_path = SDES.descifrar_imagen_ecb(image_path, key)
        pixmap = QPixmap(decrypted_image_path)
        self.ui.block_decrypt_output.setPixmap(pixmap)
        
    def sdes_decrypt_image_ctr(self):
        image_path = self.ui.block_decrypt_filepath.text()
        aes_key = ast.literal_eval(self.ui.block_key_output.toPlainText().split(" : ")[1])
        key = struct.pack('8B', *aes_key)
        decrypted_image_path = SDES.descifrar_imagen_ctr(image_path, key)
        pixmap = QPixmap(decrypted_image_path)
        self.ui.block_decrypt_output.setPixmap(pixmap)
        
    def tdes_encrypt_image(self):
        image_path = self.ui.block_encrypt_filepath.text()
        if self.ui.block_generate_key_output.toPlainText():
            aes_key = ast.literal_eval(self.ui.block_generate_key_output.toPlainText())
            key = struct.pack('24B', *aes_key)
            encrypt_image_return = triple_des.cifrar_imagen(image_path, key)
            encrypted_image_path = encrypt_image_return[0]
            mode = str(encrypt_image_return[1])
            pixmap = QPixmap(encrypted_image_path)
            self.ui.block_encrypt_output.setPixmap(pixmap)
            self.ui.block_generate_key_output.setPlainText("Key : " + self.ui.block_generate_key_output.toPlainText() + " - Mode : " + mode)
        
    def tdes_encrypt_image_ecb(self):
        image_path = self.ui.block_encrypt_filepath.text()
        if self.ui.block_generate_key_output.toPlainText():
            aes_key = ast.literal_eval(self.ui.block_generate_key_output.toPlainText())
            key = struct.pack('24B', *aes_key)
            encrypted_image_path = triple_des.cifrar_imagen_ecb(image_path, key)
            pixmap = QPixmap(encrypted_image_path)
            self.ui.block_encrypt_output.setPixmap(pixmap)
            self.ui.block_generate_key_output.setPlainText("Key : " + self.ui.block_generate_key_output.toPlainText())
        
    def tdes_encrypt_image_ctr(self):
        image_path = self.ui.block_encrypt_filepath.text()
        if self.ui.block_generate_key_output.toPlainText():
            aes_key = ast.literal_eval(self.ui.block_generate_key_output.toPlainText())
            key = struct.pack('24B', *aes_key)
            encrypted_image_path = triple_des.cifrar_imagen_ctr(image_path, key)
            pixmap = QPixmap(encrypted_image_path)
            self.ui.block_encrypt_output.setPixmap(pixmap)
            self.ui.block_generate_key_output.setPlainText("Key : " + self.ui.block_generate_key_output.toPlainText())
        
    def tdes_decrypt_image(self):
        image_path = self.ui.block_decrypt_filepath.text()
        all_key = self.ui.block_key_output.toPlainText().split(" - ")
        aes_key = ast.literal_eval(all_key[0].split(" : ")[1])
        aes_mode = ast.literal_eval(all_key[1].split(" : ")[1])
        key = struct.pack('24B', *aes_key)
        mode = struct.pack('8B', *aes_mode)
        decrypted_image_path = triple_des.descifrar_imagen(image_path, key, mode)
        pixmap = QPixmap(decrypted_image_path)
        self.ui.block_decrypt_output.setPixmap(pixmap)
        
    def tdes_decrypt_image_ecb(self):
        image_path = self.ui.block_decrypt_filepath.text()
        aes_key = ast.literal_eval(self.ui.block_key_output.toPlainText().split(" : ")[1])
        key = struct.pack('24B', *aes_key)
        decrypted_image_path = triple_des.descifrar_imagen_ecb(image_path, key)
        pixmap = QPixmap(decrypted_image_path)
        self.ui.block_decrypt_output.setPixmap(pixmap)
        
    def tdes_decrypt_image_ctr(self):
        image_path = self.ui.block_decrypt_filepath.text()
        aes_key = ast.literal_eval(self.ui.block_key_output.toPlainText().split(" : ")[1])
        key = struct.pack('24B', *aes_key)
        decrypted_image_path = triple_des.descifrar_imagen_ctr(image_path, key)
        pixmap = QPixmap(decrypted_image_path)
        self.ui.block_decrypt_output.setPixmap(pixmap)
        
    def block_encryption_choice_action(self):
        index = self.ui.block_list.currentIndex()
        mode_index = self.ui.block_mode_list.currentIndex()
        if self.current_block_encrypt_function is not None:
            self.ui.block_encrypt_btn.clicked.disconnect(self.current_block_encrypt_function)
        if self.current_block_decrypt_function is not None:
            self.ui.block_decrypt_btn.clicked.disconnect(self.current_block_decrypt_function)
        if self.current_block_generate_key_function is not None:
            self.ui.block_generate_key_btn.clicked.disconnect(self.current_block_generate_key_function)
        if index == 0:
            if mode_index == 0 or mode_index == 3:
                self.ui.block_encrypt_output.clear()
                self.ui.block_decrypt_output.clear()
                self.ui.block_generate_key_output.setPlainText("")
                self.ui.block_key_output.setPlainText("")
                self.current_block_generate_key_function = self.aes_generate_key
                self.current_block_encrypt_function = self.aes_encrypt_image
                self.current_block_decrypt_function = self.aes_decrypt_image
            elif mode_index == 1:
                self.ui.block_encrypt_output.clear()
                self.ui.block_decrypt_output.clear()
                self.ui.block_generate_key_output.setPlainText("")
                self.ui.block_key_output.setPlainText("")
                self.current_block_generate_key_function = self.aes_generate_key
                self.current_block_encrypt_function = self.aes_encrypt_image_ctr
                self.current_block_decrypt_function = self.aes_decrypt_image_ctr
            elif mode_index == 2:
                self.ui.block_encrypt_output.clear()
                self.ui.block_decrypt_output.clear()
                self.ui.block_generate_key_output.setPlainText("")
                self.ui.block_key_output.setPlainText("")
                self.current_block_generate_key_function = self.aes_generate_key
                self.current_block_encrypt_function = self.aes_encrypt_image_ecb
                self.current_block_decrypt_function = self.aes_decrypt_image_ecb
        elif index == 1:
            if mode_index == 0 or mode_index == 3:
                self.ui.block_encrypt_output.clear()
                self.ui.block_decrypt_output.clear()
                self.ui.block_generate_key_output.setPlainText("")
                self.ui.block_key_output.setPlainText("")
                self.current_block_generate_key_function = self.sdes_generate_key
                self.current_block_encrypt_function = self.sdes_encrypt_image
                self.current_block_decrypt_function = self.sdes_decrypt_image
            elif mode_index == 1:
                self.ui.block_encrypt_output.clear()
                self.ui.block_decrypt_output.clear()
                self.ui.block_generate_key_output.setPlainText("")
                self.ui.block_key_output.setPlainText("")
                self.current_block_generate_key_function = self.sdes_generate_key
                self.current_block_encrypt_function = self.sdes_encrypt_image_ctr
                self.current_block_decrypt_function = self.sdes_decrypt_image_ctr
            elif mode_index == 2:
                self.ui.block_encrypt_output.clear()
                self.ui.block_decrypt_output.clear()
                self.ui.block_generate_key_output.setPlainText("")
                self.ui.block_key_output.setPlainText("")
                self.current_block_generate_key_function = self.sdes_generate_key
                self.current_block_encrypt_function = self.sdes_encrypt_image_ecb
                self.current_block_decrypt_function = self.sdes_decrypt_image_ecb
        elif index == 2:
            if mode_index == 0 or mode_index == 3:
                self.ui.block_encrypt_output.clear()
                self.ui.block_decrypt_output.clear()
                self.ui.block_generate_key_output.setPlainText("")
                self.ui.block_key_output.setPlainText("")
                self.current_block_generate_key_function = self.tdes_generate_key
                self.current_block_encrypt_function = self.tdes_encrypt_image
                self.current_block_decrypt_function = self.tdes_decrypt_image
            elif mode_index == 1:
                self.ui.block_encrypt_output.clear()
                self.ui.block_decrypt_output.clear()
                self.ui.block_generate_key_output.setPlainText("")
                self.ui.block_key_output.setPlainText("")
                self.current_block_generate_key_function = self.tdes_generate_key
                self.current_block_encrypt_function = self.tdes_encrypt_image_ctr
                self.current_block_decrypt_function = self.tdes_decrypt_image_ctr
            elif mode_index == 2:
                self.ui.block_encrypt_output.clear()
                self.ui.block_decrypt_output.clear()
                self.ui.block_generate_key_output.setPlainText("")
                self.ui.block_key_output.setPlainText("")
                self.current_block_generate_key_function = self.tdes_generate_key
                self.current_block_encrypt_function = self.tdes_encrypt_image_ecb
                self.current_block_decrypt_function = self.tdes_decrypt_image_ecb
        
        self.ui.block_generate_key_btn.clicked.connect(self.current_block_generate_key_function)
        self.ui.block_encrypt_btn.clicked.connect(self.current_block_encrypt_function)
        self.ui.block_decrypt_btn.clicked.connect(self.current_block_decrypt_function)

    
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Todos los archivos (*)")
        if file_path:
            self.ui.block_encrypt_filepath.setText(str(file_path))
            #os.startfile(file_path)
            
    def open_file_decrypt(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Todos los archivos (*)")
        if file_path:
            self.ui.block_decrypt_filepath.setText(str(file_path))
            #os.startfile(file_path)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
