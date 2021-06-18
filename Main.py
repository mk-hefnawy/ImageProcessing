import shutil
import sys

from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QPushButton, QTextEdit

import os.path

from PyQt5.uic.properties import QtGui
from cv2 import cv2

import Utils


class Window(QMainWindow):
    utils = Utils.Utils()

    counter = 0

    dynamic_path = ""

    updated_path = ""
    edit_line_text = ""

    image = None
    lb = None
    path_line_edit = None
    convert_to_text_btn, increase_brightness, fill_gaps, remove_noise = None, None, None, None
    converted_text_txt_view, translated_text_view = None, None

    translate_btn, spell_btn, spell_translated_btn = None, None, None
    v_layout = QVBoxLayout()

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Reading Made Easy")
        icon = QIcon("D:\\4thComputer\\2ndTerm\\Image\\Project\\icon1.png")
        self.setWindowIcon(icon)

        self.image = None
        # setting geometry
        self.setGeometry(100, 100, 1850, 900)

        # calling method
        self.ui_components()

        # showing all the widgets
        self.show()

    # method for components
    def ui_components(self):

        path_label = QLabel("Image Path", self)
        path_label.setGeometry(40, 0, 120, 60)
        path_label.setWordWrap(True)

        self.v_layout.addWidget(path_label)

        self.path_line_edit = QLineEdit("", self)
        self.path_line_edit.setGeometry(40, 40, 420, 30)  # x ,y , width, height

        self.v_layout.addWidget(self.path_line_edit)

        load_btn = QPushButton("Load", self)
        load_btn.setGeometry(480, 40, 60, 30)
        load_btn.clicked.connect(lambda: self.on_load_clicked())

        self.lb = QLabel("Loaded Image", self)
        self.lb.setVisible(False)

        self.label = QLabel("Modified Image", self)
        self.label.setVisible(False)

        self.convert_to_text_btn = QPushButton("Convert to text", self)
        self.convert_to_text_btn.setVisible(False)

        self.increase_brightness = QPushButton("Increase Brightness", self)
        self.increase_brightness.setVisible(False)

        self.fill_gaps = QPushButton("Fill Gaps", self)
        self.fill_gaps.setVisible(False)

        self.remove_noise = QPushButton("Remove Noise", self)
        self.remove_noise.setVisible(False)

        """self.layout = QtGui.QHBoxLayout()  # layout for the central widget
        self.widget = QtGui.QWidget(self)  # central widget
        self.widget.setLayout(self.layout)

        self.processing_type = QtGui.QButtonGroup(self.widget)

        self.increase_brightness = QtGui.QRadioButton("Increase brightness")
        self.processing_type.addButton(self.increase_brightness)

        self.fill_gaps = QtGui.QRadioButton("Fill gaps")
        self.processing_type.addButton(self.fill_gaps)

        self.remove_noise = QtGui.QRadioButton("Remove noise")
        self.processing_type.addButton(self.remove_noise)"""

        self.converted_text_txt_view = QTextEdit("", self)
        self.converted_text_txt_view.setVisible(False)
        self.converted_text_txt_view.setReadOnly(True)

        self.translate_btn = QPushButton("Translate", self)
        self.translate_btn.setVisible(False)

        self.translated_text_view = QTextEdit("", self)
        self.translated_text_view.setVisible(False)
        self.translated_text_view.setReadOnly(True)

        self.spell_btn = QPushButton("Spell", self)
        self.spell_btn.setVisible(False)

        self.spell_translated_btn = QPushButton("Spell", self)
        self.spell_translated_btn.setVisible(False)

    def on_load_clicked(self):
        self.counter = 0
        self.utils.counter_zero()
        shutil.rmtree('D:\\4thComputer\\2ndTerm\\Image\\Project\\A\\')
        path = os.path.join('D:\\4thComputer\\2ndTerm\\Image\\Project\\', 'A')
        os.mkdir(path)

        self.edit_line_text = self.path_line_edit.text()

        print(self.edit_line_text)
        if len(self.edit_line_text) == 0:
            message = "Please enter image path"
            self.utils.show_message(message)

        elif not os.path.isfile(self.edit_line_text):
            message = "Please enter a valid path"
            self.utils.show_message(message)

        elif os.path.isfile(self.edit_line_text):
            print("Valid path")

            self.load_image(self.edit_line_text)

        else:
            message = "hhhh"
            self.utils.show_message(message)

    def load_image(self, path):
        self.display_image(path)

    def display_image(self, path):
        self.lb.setVisible(True)
        self.lb.setGeometry(40, 100, 500, 500)

        pixmap = QPixmap(path)
        image = cv2.imread(path)

        self.lb.setPixmap(pixmap.scaled(self.lb.size()))
        self.prepare_convert_btn(self.edit_line_text)
        self.prepare_processing_btns(image)

    def display_modified_image(self, image_path):
        self.label.setVisible(True)
        self.label.setGeometry(600, 100, 500, 500)
        #  img = QtGui.QImage(image, image.shape[1], image.shape[0], image.shape[1] * 3, QtGui.QImage.Format_RGB888)
        #  img = self.utils.numpyQImage(image)
        pixMap = QPixmap(image_path)
        self.label.setPixmap(pixMap.scaled(self.label.size()))


    def prepare_convert_btn(self, path):
        self.convert_to_text_btn.setGeometry(1200, 40, 100, 30)
        self.convert_to_text_btn.setVisible(True)
        self.convert_to_text_btn.clicked.connect(lambda: self.on_convert_btn_clicked(path))

    def prepare_processing_btns(self, image):
        self.increase_brightness.setGeometry(600, 40, 120, 30)
        self.increase_brightness.setVisible(True)
        self.increase_brightness.clicked.connect(lambda: self.on_increase_brightness_btn_clicked(image))

        self.fill_gaps.setGeometry(750, 40, 120, 30)
        self.fill_gaps.setVisible(True)
        self.fill_gaps.clicked.connect(lambda: self.on_fill_gaps_btn_clicked(image))

        self.remove_noise.setGeometry(900, 40, 120, 30)
        self.remove_noise.setVisible(True)
        self.remove_noise.clicked.connect(lambda: self.on_remove_noise_btn_clicked(image))

    def on_convert_btn_clicked(self, path):
        if self.counter > 0:
            path = self.updated_path
        print("PATH   " + path)
        image = cv2.imread(path)
        converted_text = self.utils.convert(image)
        self.converted_text_txt_view.setGeometry(1200, 100, 500, 100)
        #  self.converted_text_txt_view.setWindowTitle("Converted Text")
        self.converted_text_txt_view.setVisible(True)
        self.converted_text_txt_view.setText(converted_text)
        self.converted_text_txt_view.setAlignment(Qt.AlignTop)
        self.converted_text_txt_view.setStyleSheet("padding: 5px")
        self.converted_text_txt_view.setFont(QFont("New Times", 12))
        self.prepare_translate_and_spell(converted_text)

    def on_increase_brightness_btn_clicked(self, image):
        print("on_increase_brightness_btn_clicked"+str(self.counter))
        img_path = ""
        if self.counter == 0:
            img_path = self.utils.increase_brightness(img=image)
        else:
            img_path = self.utils.increase_brightness(img_path=self.updated_path)
            print("Updated Path" + self.updated_path)
        self.display_modified_image(img_path)
        self.updated_path = img_path

        self.counter += 1

    def on_fill_gaps_btn_clicked(self, image):
        print("on_fill_gaps_btn_clicked"+str(self.counter))
        img_path = ""
        if self.counter == 0:
            img_path = self.utils.close_gaps(img=image)
        else:
            img_path = self.utils.close_gaps(img_path=self.updated_path, iterations=self.counter)
        print("From OnFillGaps")
        self.display_modified_image(img_path)
        self.updated_path = img_path


        self.counter += 1

    def on_remove_gaps_btn_clicked(self, image):
        pass

    def on_remove_noise_btn_clicked(self, image):
        print("on_remove_noise_btn_clicked"+str(self.counter))
        img_path = ""
        if self.counter == 0:
            img_path = self.utils.remove_noise(img=image)
        else:
            img_path = self.utils.remove_noise(img_path=self.updated_path)
        print("From OnRemoveNoise")
        self.display_modified_image(img_path)
        self.updated_path = img_path



        self.counter += 1


    def prepare_translate_and_spell(self, converted_text):
        self.translate_btn.setGeometry(1200, 220, 100, 30)
        self.translate_btn.setVisible(True)
        self.translate_btn.clicked.connect(lambda: self.on_translate_clicked(converted_text))

        self.spell_btn.setGeometry(1330, 220, 100, 30)
        self.spell_btn.setVisible(True)

        #  Todo
        dest_language = 'en'
        self.spell_btn.clicked.connect(lambda: self.on_spell_clicked(converted_text, dest_language))

    def on_translate_clicked(self, converted_text):
        dest_language = 'ar'
        translated_text = self.utils.translate(converted_text, dest_language)
        self.translated_text_view.setGeometry(1200, 280, 500, 100)

        self.translated_text_view.setVisible(True)
        self.translated_text_view.setText(translated_text)
        self.translated_text_view.setAlignment(Qt.AlignTop)
        self.translated_text_view.setStyleSheet("padding: 5px")
        self.translated_text_view.setFont(QFont("New Times", 12))

        self.prepare_spell_translated(translated_text)

    def on_spell_clicked(self, converted_text, dest_language):
        self.utils.spell(converted_text, dest_language)

    def prepare_spell_translated(self, translated_text):

        self.spell_translated_btn.setGeometry(1200, 400, 100, 30)
        self.spell_translated_btn.setVisible(True)

        # Todo
        dest_language = 'ar'
        self.spell_translated_btn.clicked.connect(
            lambda: self.on_spell_translated_clicked(translated_text, dest_language))

    def on_spell_translated_clicked(self, translated_text, dest_language):
        self.utils.spell(translated_text, dest_language)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
