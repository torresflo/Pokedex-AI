import sys
from PySide6 import QtWidgets

from UI.MainWindow import PokedexWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    mainWindow = PokedexWidget()
    mainWindow.setWindowTitle("Pokédex AI")
    mainWindow.show()

    sys.exit(app.exec())
