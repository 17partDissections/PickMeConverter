from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
from random import randint

class WindowDefault(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.emojis = [")", "))", ")))", ":)", ":))", ":3", "<3", ":x", ":p", ":D", "^^", "^ ^", "^._.^"]

        self.SetDefaultWindow()

    def SetDefaultWindow(self):
        self.setFixedSize(500, 250)
        self.setWindowTitle('PickMeConverter')
        self.setWindowIcon(QIcon(r'_internal\icon\icon_blackOutline.ico'))

        logo = QLabel(self)
        logo.move(200, -20)
        logoPixmap = QPixmap(r'_internal\img\logo_blackOutline.png')
        logo.setPixmap(logoPixmap.scaled(100, 100))
        logo.show()

        #title = QLabel("PickMe", self)
        #title.move(210, 0)
        #title.setFont(QFont("Arial", 20))

        #title2 = QLabel("Converter", self)
        #title2.move(195, 20)
        #title2.setFont(QFont("Arial", 20))

        vLabel = QLabel("version 1.0   by Q17pD", self)
        vLabel.move(5, 235)
        vLabel.setFont(QFont("Arial", 10))

        self.textInput = QTextEdit(self)
        self.textInput.move(10, 50)
        self.textInput.resize(230, 100)
        self.textInput.setPlaceholderText("Text input")

        self.textOutput = QTextEdit(self)
        self.textOutput.move(260, 50)
        self.textOutput.resize(230, 100)
        self.textOutput.setPlaceholderText(self.ConvertText("Text output"))
        self.textOutput.setReadOnly(True)

        self.convertButton = QPushButton("Convert!", self)
        self.convertButton.move(150, 160)
        self.convertButton.resize(200, 50)
        self.convertButton.clicked.connect(self.ConvertTextButton)

        self.show()

    def ConvertTextButton(self):
        inputText = self.textInput.toPlainText()
        convertedText = self.ConvertText(inputText)
        self.textOutput.setText(convertedText)

    def ConvertText(self, text):
        words = text.split()
        convertedWords = []
        for word in words:
            if word:
                converted = word
                if(randint(0,2) == 2):
                    converted = f"{word[0]}-{word}"
                isWordHaveEndingPunctuationMarks = self.CheckForEndingPunctuationMarks(word)
                if (isWordHaveEndingPunctuationMarks == False and randint(0, 2) == 2):
                    if (randint(0, 1) == 0):
                        converted += ".."
                    elif (randint(0, 1) == 1):
                        converted += "..."
                convertedWords.append(converted)
        if(randint(0,1) == 1):
            randomEmoji = random.choice(self.emojis)
            return ' '.join(convertedWords) + randomEmoji
        else:
            return ' '.join(convertedWords)

    def CheckForEndingPunctuationMarks(self, word):
        maxIndex = len(word) - 1
        if(maxIndex == "." or maxIndex == "," or maxIndex == "!" or maxIndex == "?"or maxIndex == ":" or maxIndex == ";"):
            return True
        else:
            return False