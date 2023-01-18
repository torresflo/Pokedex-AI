import sys
from PySide6 import QtWidgets

from UI.QPokedexWidget import QPokedexWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    mainWindow = QPokedexWidget()
    mainWindow.setWindowTitle("Pokédex AI")
    mainWindow.show()

    sys.exit(app.exec())