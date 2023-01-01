from PySide6 import QtCore
from PySide6 import QtWidgets, QtGui

class QPokemonImageLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loadPlaceholderImage()

    def loadPlaceholderImage(self):
        self.loadImageWithText("Please select an image to search for a Pokémon.")

    def loadWaitingImage(self):
        self.loadImageWithText("Searching in progress, please wait...")

    def loadImageWithText(self, text:str, width=475, height=475):
        image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
        
        painter = QtGui.QPainter()
        painter.begin(image)
        font = painter.font()
        font.setPixelSize(14)
        painter.setFont(font)
        imageRect = QtCore.QRectF(0, 0, width, height)
        textOptions = QtGui.QTextOption(QtGui.Qt.AlignCenter | QtGui.Qt.AlignVCenter)
        backgroundColor = QtGui.QColor.fromRgb(200, 200, 200)
        painter.fillRect(imageRect, backgroundColor)
        painter.setPen(QtGui.QPen(QtGui.QColor.fromRgb(150, 150, 150)))
        painter.drawText(imageRect, text, textOptions)
        painter.end()

        self.setPixmap(QtGui.QPixmap.fromImage(image))
        