import googletrans
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from cv2 import cv2
from googletrans import Translator
import os
from gtts import gTTS
from playsound import playsound

from pytesseract import pytesseract


class Utils:
    counter = 0

    def __init__(self):
        self.dtype = None

    def counter_zero(self):
        self.counter = 0

    # show a message to the user
    def show_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setGeometry()
        msg.setText(message)
        msg.setWindowTitle("File not found :D")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

    # convert the input image to text using tesseract
    def convert(self, img):
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)
        return text

    # translate the text
    def translate(self, converted_text, dest_language):
        trans = Translator()
        t = trans.translate(converted_text, dest=dest_language)
        print(googletrans.LANGUAGES)
        return t.text

    # spell the text
    def spell(self, text, dest_language):
        myobj = gTTS(text=text, lang=dest_language, slow=False)
        # Saving the converted audio in a mp3 file named welcome
        myobj.save("test.mp3")
        # Playing the converted file
        playsound("test.mp3")
        os.remove("test.mp3")

    # increase the brightness of the image
    def increase_brightness(self, img_path, value=20):
        img = cv2.imread(img_path)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value

        final_hsv = cv2.merge((h, s, v))
        image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)  # was img
        #  writing the image to disk
        path = "D:\\4thComputer\\2ndTerm\\Image\\Project\\A\\" + str(self.counter) + ".jpg"
        cv2.imwrite(path, image)
        self.counter += 1
        return path

    # fill the gaps of the image
    def close_gaps(self, img_path, iterations=1):
        img = cv2.imread(img_path)
        square_kernel = np.ones(((2 * iterations) + 1, (2 * iterations) + 1), np.uint8)
        out = cv2.dilate(cv2.erode(img, square_kernel, iterations=1), square_kernel, iterations=1)
        path = "D:\\4thComputer\\2ndTerm\\Image\\Project\\A\\" + str(self.counter) + ".jpg"
        cv2.imwrite(path, out)
        self.counter += 1
        return path

    # unglue connected parts of the image
    def open_gaps(self, img_path, iterations=1):
        img = cv2.imread(img_path)
        square_kernel = np.ones(((2 * iterations) + 1, (2 * iterations) + 1), np.uint8)
        out = cv2.erode(cv2.dilate(img, square_kernel, iterations=1), square_kernel, iterations=1)
        path = "D:\\4thComputer\\2ndTerm\\Image\\Project\\A\\" + str(self.counter) + ".jpg"
        cv2.imwrite(path, out)
        self.counter += 1
        return path

    # remove noise from the image
    def remove_noise(self, img_path):
        img = cv2.imread(img_path)
        img = cv2.medianBlur(img, 3)  # 3
        path = "D:\\4thComputer\\2ndTerm\\Image\\Project\\A\\" + str(self.counter) + ".jpg"
        cv2.imwrite(path, img)
        self.counter += 1
        return path

    # convert numpy array representation of an image to QImage
    def numpyQImage(self, image):
        qImg = QtGui.QImage()
        if image.dtype == np.uint8:
            if len(image.shape) == 2:
                channels = 1
                height, width = image.shape
                bytesPerLine = channels * width
                qImg = QtGui.QImage(
                    image.data, width, height, bytesPerLine, QtGui.QImage.Format_Indexed8
                )
                qImg.setColorTable([QtGui.qRgb(i, i, i) for i in range(256)])
            elif len(image.shape) == 3:
                if image.shape[2] == 3:
                    height, width, channels = image.shape
                    bytesPerLine = channels * width
                    qImg = QtGui.QImage(
                        image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888
                    )
                elif image.shape[2] == 4:
                    height, width, channels = image.shape
                    bytesPerLine = channels * width
                    fmt = QtGui.QImage.Format_ARGB32
                    qImg = QtGui.QImage(
                        image.data, width, height, bytesPerLine, QtGui.QImage.Format_ARGB32
                    )
        return qImg
