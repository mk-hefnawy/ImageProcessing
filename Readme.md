# ReadingMadeEasy

ReadingMadeEasy is a helper tool To convert any printed or handwritten text to digital text. And convert that digital text to speech. Also translates that text into a Arabic.

## Tech

ReadingMadeEasy uses a number of open source projects to work properly:

- [googletrans==3.1.0a0] - google tool for translation
- [pytesseractr] - OCR tool
- [pyqt5] - open source library for GUI.
- [gTTS] - convert text to audio file.
- [playsound] - Plays the audio file.
- [opencv-python] - For digital image process operations.

And of course ReadingMadeEasy itself is open source with a [https://github.com/mk-hefnawy/ImageProcessing] on GitHub.

## Installation

ReadingMadeEasy requires:
1) You have to have a folder called 'A' in the same directory of the 
project files "Main.py and Utils.py" Or the directory of the "Main.exe" 
to get the project work properly.

2) You have to have pytesseract installed in your disk in the default installation 
directory like so C:\Program Files\Tesseract-OCR\tesseract.exe

```sh
pip install pyqt5
pip install opencv-python
pip install gTTS
pip install playsound
pip install pytesseract
pip install googletrans==3.1.0a0
```
## Task Break-down 
Mohamed Hussein Mostafa:
Image processing and dealing with translation api.

Mohamed Emad Mahmoud:
Image processing and dealing with translation api.

Mohamed Amr Ahmed:
Converting printed text to digital text.

Mohamed Amr Mohamed:
Converting text to voice.

Mohamed Khaled Rashad:
GUI