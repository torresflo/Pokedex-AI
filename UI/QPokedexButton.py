from PySide6 import QtCore, QtWidgets, QtGui

class QPokedexButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        currentFont = self.font()
        currentFont.setPointSize(14)
        currentFont.setBold(True)
        self.setFont(currentFont)

        self.m_isHovered = False
        self.m_isClicked = False 

    def paintEvent(self, event: QtGui.QPaintEvent):
        rect = event.rect()

        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setPen(QtGui.Qt.NoPen)

        color = QtGui.QColor(0, 0, 0)
        if self.m_isClicked:
            color = QtGui.QColor(30, 30, 30)
        elif self.m_isHovered:
            color = QtGui.QColor(50, 50, 50)

        if not self.isEnabled():
            color = QtGui.QColor(200, 200, 200)

        painter.setBrush(color)
        painter.drawRoundedRect(rect, 10, 10)

        color = QtGui.QColor(255, 255, 255)
        painter.setPen(color)
        painter.setFont(self.font())
        painter.drawText(event.rect(), self.text(), QtGui.QTextOption(QtGui.Qt.AlignCenter))

        painter.end()

    def enterEvent(self, event: QtGui.QEnterEvent) -> None:
        self.m_isHovered = True
        return super().enterEvent(event)

    def leaveEvent(self, event: QtCore.QEvent) -> None:
        self.m_isHovered = False
        return super().leaveEvent(event)

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.m_isClicked = True
        return super().mousePressEvent(e)

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        self.m_isClicked = False 
        return super().mouseReleaseEvent(e)

    def sizeHint(self) -> QtCore.QSize:
        currentFont = self.font()
        fontMetrics = QtGui.QFontMetrics(currentFont)

        result = QtCore.QSize(0, 0)
        boudingRect = fontMetrics.boundingRect(self.text())
        result.setWidth(boudingRect.width() + 30)
        result.setHeight(boudingRect.height() + 10)

        return result