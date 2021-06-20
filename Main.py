import shutil
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QPushButton, QTextEdit

import os.path
from cv2 import cv2

import Utils


class Window(QMainWindow):
    utils = Utils.Utils()

    counter = 0
    counter_load = 0
    convert_clicked = 0
    translated_clicked = 0

    dynamic_path = ""

    updated_path = ""
    edit_line_text = ""

    image = None
    lb = None
    path_line_edit = None
    convert_to_text_btn, increase_brightness, fill_gaps, remove_noise, unglue = None, None, None, None, None
    converted_text_txt_view, translated_text_view, converted_text, translated_text = None, None, None, None

    translate_btn, spell_btn, spell_translated_btn = None, None, None
    v_layout = QVBoxLayout()

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Reading Made Easy")
        # setting icon
        #icon = QIcon("D:\\4thComputer\\2ndTerm\\Image\\Project\\icon1.png")
        #self.setWindowIcon(icon)

        self.image = None
        # setting geometry
        self.setGeometry(100, 100, 1850, 900)

        # calling method
        self.ui_components()

        # showing all the widgets
        self.show()

    # method for components
    """ By Mohamed Khaled Rashad"""
    def ui_components(self):
        # label of the line edit
        path_label = QLabel("Image Path", self)
        path_label.setGeometry(40, 0, 120, 60)
        path_label.setWordWrap(True)

        self.v_layout.addWidget(path_label)

        # line edit where the user enters the path of the image
        self.path_line_edit = QLineEdit("", self)
        self.path_line_edit.setGeometry(40, 40, 420, 30)  # x ,y , width, height

        self.v_layout.addWidget(self.path_line_edit)

        # Load button
        load_btn = QPushButton("Load", self)
        load_btn.setGeometry(480, 40, 60, 30)
        load_btn.clicked.connect(lambda: self.on_load_clicked())

        # preview of the loaded image
        self.lb = QLabel("Loaded Image", self)
        self.lb.setVisible(False)

        # preview of the loaded image
        self.label = QLabel("Modified Image", self)
        self.label.setVisible(False)

        #  convert to text button
        self.convert_to_text_btn = QPushButton("Convert to text", self)
        self.convert_to_text_btn.setVisible(False)

        #  increase brightness button
        self.increase_brightness = QPushButton("Increase Brightness", self)
        self.increase_brightness.setVisible(False)

        #  fill gaps button
        self.fill_gaps = QPushButton("Fill Gaps", self)
        self.fill_gaps.setVisible(False)

        #  Unglue button
        self.unglue = QPushButton("Unglue", self)
        self.unglue.setVisible(False)

        #  remove noise button
        self.remove_noise = QPushButton("Remove Noise", self)
        self.remove_noise.setVisible(False)

        #  text view of the converted text
        self.converted_text_txt_view = QTextEdit("", self)
        self.converted_text_txt_view.setVisible(False)
        self.converted_text_txt_view.setReadOnly(True)

        #  translate button
        self.translate_btn = QPushButton("Translate", self)
        self.translate_btn.setVisible(False)

        # text view of the translated text
        self.translated_text_view = QTextEdit("", self)
        self.translated_text_view.setVisible(False)
        self.translated_text_view.setReadOnly(True)

        # spell the converted text button
        self.spell_btn = QPushButton("Spell", self)
        self.spell_btn.setVisible(False)

        # spell the translated text button
        self.spell_translated_btn = QPushButton("Spell", self)
        self.spell_translated_btn.setVisible(False)

    """ By Mohamed Khaled Rashad"""
    # call back method of load button
    def on_load_clicked(self):
        self.counter = 0
        self.counter_load += 1
        self.utils.counter_zero()
        shutil.rmtree('A\\')
        path = os.path.join('', 'A')
        os.mkdir(path)

        self.label.setVisible(False)
        self.converted_text_txt_view.setVisible(False)
        self.translated_text_view.setVisible(False)

        # input validation
        self.edit_line_text = self.path_line_edit.text()
        if len(self.edit_line_text) == 0:
            message = "Please enter image path"
            self.utils.show_message(message)

        elif not os.path.isfile(self.edit_line_text):
            message = "Please enter a valid path"
            self.utils.show_message(message)

        elif os.path.isfile(self.edit_line_text):
            print("Valid path")

            self.display_image(self.edit_line_text)

        else:
            message = " "
            self.utils.show_message(message)

    """ By Mohamed Khaled Rashad"""
    # display the preview of the input image
    def display_image(self, path):
        self.lb.setVisible(True)
        self.lb.setGeometry(40, 100, 500, 500)

        pixmap = QPixmap(path)

        self.lb.setPixmap(pixmap.scaled(self.lb.size()))
        if self.counter_load <= 1:
            self.prepare_convert_btn()
            self.prepare_processing_btns()

    # display the image after some process
    def display_modified_image(self, image_path):
        self.label.setVisible(True)
        self.label.setGeometry(600, 100, 500, 500)
        pixMap = QPixmap(image_path)
        self.label.setPixmap(pixMap.scaled(self.label.size()))

    # showing the convert to text button
    def prepare_convert_btn(self):
        self.convert_to_text_btn.setGeometry(1200, 40, 100, 30)
        self.convert_to_text_btn.setVisible(True)
        self.convert_to_text_btn.clicked.connect(lambda: self.on_convert_btn_clicked())

    # showing the increase brightness, fill gaps, remove noise, and unglue buttons
    def prepare_processing_btns(self):
        self.increase_brightness.setGeometry(600, 40, 120, 30)
        self.increase_brightness.setVisible(True)
        self.increase_brightness.clicked.connect(lambda: self.on_increase_brightness_btn_clicked())

        self.fill_gaps.setGeometry(750, 40, 120, 30)
        self.fill_gaps.setVisible(True)
        self.fill_gaps.clicked.connect(lambda: self.on_fill_gaps_btn_clicked())

        self.unglue.setGeometry(900, 40, 120, 30)
        self.unglue.setVisible(True)
        self.unglue.clicked.connect(lambda: self.on_unglue_btn_clicked())

        self.remove_noise.setGeometry(1050, 40, 120, 30)
        self.remove_noise.setVisible(True)
        self.remove_noise.clicked.connect(lambda: self.on_remove_noise_btn_clicked())

    """ By Mohamed Khaled Rashad"""
    # call back function of convert button
    def on_convert_btn_clicked(self):
        if self.counter > 0:
            path = self.updated_path
        else:
            path = self.edit_line_text
        image = cv2.imread(path)
        self.converted_text = self.utils.convert(image)
        self.converted_text_txt_view.setGeometry(1200, 100, 500, 100)
        self.converted_text_txt_view.setVisible(True)
        self.converted_text_txt_view.setText(self.converted_text)
        self.converted_text_txt_view.setAlignment(Qt.AlignTop)
        self.converted_text_txt_view.setStyleSheet("padding: 5px")
        self.converted_text_txt_view.setFont(QFont("New Times", 12))
        if self.convert_clicked == 0:
            self.prepare_translate_and_spell()

        self.convert_clicked += 1

    """ By Mohamed Khaled Rashad"""
    # call back function of increase brightness button
    def on_increase_brightness_btn_clicked(self):
        if self.counter > 0:
            path = self.updated_path
            new_path = self.utils.increase_brightness(path)
        else:
            path = self.edit_line_text
            new_path = self.utils.increase_brightness(path)

        self.display_modified_image(new_path)
        self.updated_path = new_path

        self.counter += 1

    """ By Mohamed Khaled Rashad"""
    # call back function of fill gaps button
    def on_fill_gaps_btn_clicked(self):
        if self.counter > 0:
            path = self.updated_path
            new_path = self.utils.close_gaps(path, iterations=self.counter)
        else:
            path = self.edit_line_text
            new_path = self.utils.close_gaps(path, iterations=self.counter)

        self.display_modified_image(new_path)
        self.updated_path = new_path

        self.counter += 1

    """ By Mohamed Khaled Rashad"""
    # call back function of unglue button
    def on_unglue_btn_clicked(self):
        if self.counter > 0:
            path = self.updated_path
            new_path = self.utils.open_gaps(path, iterations=self.counter)
        else:
            path = self.edit_line_text
            new_path = self.utils.open_gaps(path, iterations=self.counter)

        self.display_modified_image(new_path)
        self.updated_path = new_path

        self.counter += 1

    """ By Mohamed Khaled Rashad"""
    # call back function of remove noise button
    def on_remove_noise_btn_clicked(self):
        if self.counter > 0:
            path = self.updated_path
            new_path = self.utils.remove_noise(path)
        else:
            path = self.edit_line_text
            new_path = self.utils.remove_noise(path)
        self.display_modified_image(new_path)
        self.updated_path = new_path
        self.counter += 1

    """ By Mohamed Khaled Rashad"""
    # show translate and spell (converted text) button
    def prepare_translate_and_spell(self):
        self.translate_btn.setGeometry(1200, 220, 100, 30)
        self.translate_btn.setVisible(True)
        self.translate_btn.clicked.connect(lambda: self.on_translate_clicked())

        self.spell_btn.setGeometry(1330, 220, 100, 30)
        self.spell_btn.setVisible(True)

        dest_language = 'en'
        self.spell_btn.clicked.connect(lambda: self.on_spell_clicked(dest_language))

    """ By Mohamed Khaled Rashad"""
    # call back function of translate button
    def on_translate_clicked(self):
        dest_language = 'ar'
        self.translated_text = self.utils.translate(self.converted_text[:-1], dest_language)
        self.translated_text_view.setGeometry(1200, 280, 500, 100)

        self.translated_text_view.setVisible(True)
        self.translated_text_view.setText(self.translated_text)
        self.translated_text_view.setAlignment(Qt.AlignTop)
        self.translated_text_view.setStyleSheet("padding: 5px")
        self.translated_text_view.setFont(QFont("New Times", 12))
        if self.translated_clicked == 0:
            self.prepare_spell_translated()

        self.translated_clicked += 1

    """ By Mohamed Khaled Rashad"""
    # call back function of spell (converted text) button
    def on_spell_clicked(self, dest_language):
        self.utils.spell(self.converted_text, dest_language)

    """ By Mohamed Khaled Rashad"""
    # show spell (translated text) button
    def prepare_spell_translated(self):

        self.spell_translated_btn.setGeometry(1200, 400, 100, 30)
        self.spell_translated_btn.setVisible(True)
        dest_language = 'ar'
        self.spell_translated_btn.clicked.connect(
            lambda: self.on_spell_translated_clicked(dest_language))

    """ By Mohamed Khaled Rashad"""
    # call back function of spell (translated text) button
    def on_spell_translated_clicked(self, dest_language):
        self.utils.spell(self.translated_text, dest_language)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
