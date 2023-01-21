from PySide6 import QtCore, QtWidgets, QtGui

from Model.PokemonData import Pokedex
from Model.PokemonModel import PokemonModel

from UI.QPokemonImageLabel import QPokemonImageLabel
from UI.QPokedexButton import QPokedexButton

from Utils.DataTools import DataSaver

class QPokedexWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.m_dragPosition = QtCore.QPointF(0, 0)
        super().__init__(parent)

        self.m_pokedex = Pokedex()
        self.m_pokedex.autoInitialize()

        self.m_fileName = ""
        self.m_predictionModel = PokemonModel()

        # Title Bar
        self.m_minimizeWindowButton = QPokedexButton("_")
        self.m_closeWindowButton = QPokedexButton("X")
        
        # Select file
        self.m_selectFileButton = QPokedexButton("Select image...")
        self.m_classifyImageButton = QPokedexButton("Search Pokémon")
        self.m_classifyImageButton.setEnabled(False)

        self.m_selectFileLayout = QtWidgets.QHBoxLayout()
        self.m_selectFileLayout.addWidget(self.m_selectFileButton)
        self.m_selectFileLayout.addWidget(self.m_classifyImageButton)
        self.m_selectFileLayout.addStretch()
        self.m_selectFileLayout.addWidget(self.m_minimizeWindowButton)
        self.m_selectFileLayout.addWidget(self.m_closeWindowButton)

        # Pokemon Page
        font = self.font()

        self.m_pokemonNumberLabel = QtWidgets.QLabel("Number")
        font.setPointSize(14)
        self.m_pokemonNumberLabel.setFont(font)
        self.m_pokemonNameLabel = QtWidgets.QLabel("Name")
        font.setPointSize(32)
        self.m_pokemonNameLabel.setFont(font)

        self.m_pokemonType1Label = QtWidgets.QLabel("Type 1")
        self.m_pokemonType2Label = QtWidgets.QLabel("Type 2")
        self.m_pokemonTypesLayout = QtWidgets.QHBoxLayout()
        self.m_pokemonTypesLayout.addWidget(self.m_pokemonType1Label)
        self.m_pokemonTypesLayout.addWidget(self.m_pokemonType2Label)
        self.m_pokemonTypesLayout.addStretch()

        self.m_pokemonGenusLabel = QtWidgets.QLabel("Genus")
        font.setPointSize(22)
        self.m_pokemonGenusLabel.setFont(font)

        self.m_pokemonDescriptionLabel = QtWidgets.QLabel("Description")
        self.m_pokemonDescriptionLabel.setFixedWidth(410)
        self.m_pokemonDescriptionLabel.setFixedHeight(100)
        self.m_pokemonDescriptionLabel.setWordWrap(True)
        font.setPointSize(16)
        self.m_pokemonDescriptionLabel.setFont(font)

        self.m_pokemonAbilitiesLabel = QtWidgets.QLabel("Abilities")
        font.setPointSize(12)
        self.m_pokemonAbilitiesLabel.setFont(font)

        self.m_pokemonHeightLabel = QtWidgets.QLabel("Height")
        self.m_pokemonWeightLabel = QtWidgets.QLabel("Weight")
        self.m_pokemonHeightLabel.setFont(font)
        self.m_pokemonWeightLabel.setFont(font)

        self.m_pokemonFrontSpriteLabel = QtWidgets.QLabel("Front")
        self.m_pokemonBackSpriteLabel = QtWidgets.QLabel("Back")
        self.m_pokemonFrontShinySpriteLabel = QtWidgets.QLabel("Front Shiny")
        self.m_pokemonBackShinySpriteLabel = QtWidgets.QLabel("Back Shiny")
        self.m_pokemonSpritesLayout = QtWidgets.QHBoxLayout()
        self.m_pokemonSpritesLayout.addWidget(self.m_pokemonFrontSpriteLabel)
        self.m_pokemonSpritesLayout.addWidget(self.m_pokemonBackSpriteLabel)
        self.m_pokemonSpritesLayout.addWidget(self.m_pokemonFrontShinySpriteLabel)
        self.m_pokemonSpritesLayout.addWidget(self.m_pokemonBackShinySpriteLabel)
        self.m_pokemonSpritesLayout.addStretch()
        self.m_pokemonSpritesLayout.setContentsMargins(0, 0, 50, 0)

        self.m_pokemonDataLayout = QtWidgets.QVBoxLayout()
        self.m_pokemonDataLayout.addWidget(self.m_pokemonNumberLabel)
        self.m_pokemonDataLayout.addWidget(self.m_pokemonNameLabel)
        self.m_pokemonDataLayout.addLayout(self.m_pokemonTypesLayout)
        self.m_pokemonDataLayout.addWidget(self.m_pokemonGenusLabel)
        self.m_pokemonDataLayout.addWidget(self.m_pokemonDescriptionLabel)
        self.m_pokemonDataLayout.addWidget(self.m_pokemonAbilitiesLabel)
        self.m_pokemonDataLayout.addWidget(self.m_pokemonHeightLabel)
        self.m_pokemonDataLayout.addWidget(self.m_pokemonWeightLabel)
        self.m_pokemonDataLayout.addStretch()
        self.m_pokemonDataLayout.addLayout(self.m_pokemonSpritesLayout)
        self.m_pokemonDataLayout.setContentsMargins(20, 20, 20, 20)
        
        self.m_pokemonImageLabel = QPokemonImageLabel()
        self.m_pokemonLayout = QtWidgets.QHBoxLayout()
        self.m_pokemonLayout.addLayout(self.m_pokemonDataLayout)
        self.m_pokemonLayout.addWidget(self.m_pokemonImageLabel)

        # Navigation
        self.m_tenPreviousPokemonButton = QPokedexButton(" << ")
        self.m_previousPokemonButton = QPokedexButton(" < ")
        self.m_nextPokemonButton = QPokedexButton(" > ")
        self.m_tenNextPokemonButton = QPokedexButton(" >> ")
        self.m_navigationLayout = QtWidgets.QHBoxLayout()
        self.m_navigationLayout.addStretch()
        self.m_navigationLayout.addWidget(self.m_tenPreviousPokemonButton)
        self.m_navigationLayout.addWidget(self.m_previousPokemonButton)
        self.m_navigationLayout.addWidget(self.m_nextPokemonButton)
        self.m_navigationLayout.addWidget(self.m_tenNextPokemonButton)
        self.m_navigationLayout.addStretch()

        # Main Layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addLayout(self.m_selectFileLayout)
        self.layout.addLayout(self.m_pokemonLayout)
        self.layout.addLayout(self.m_navigationLayout)
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)

        # Window
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)

        # Connect
        self.m_minimizeWindowButton.clicked.connect(self.showMinimized)
        self.m_closeWindowButton.clicked.connect(self.close)

        self.m_selectFileButton.clicked.connect(self.onSelectFileButtonClicked)
        self.m_classifyImageButton.clicked.connect(self.onClassifyImageButtonClicked)
        self.m_tenPreviousPokemonButton.clicked.connect(self.onTenPreviousPokemonButtonClicked)
        self.m_previousPokemonButton.clicked.connect(self.onPreviousPokemonButtonClicked)
        self.m_nextPokemonButton.clicked.connect(self.onNextPokemonButtonClicked)
        self.m_tenNextPokemonButton.clicked.connect(self.onTenNextPokemonButtonClicked)

        # Load data
        self.fillPokemonData(1)

    def fillPokemonData(self, pokemonNumber):
        self.m_currentSelectedPokemon = pokemonNumber
        pokemonData = self.m_pokedex.m_data[f"{pokemonNumber}"]

        self.m_pokemonFrontSpriteLabel.setPixmap(self.generateSpritePixmap(pokemonNumber, DataSaver.SpriteFrontDefaultName))
        self.m_pokemonBackSpriteLabel.setPixmap(self.generateSpritePixmap(pokemonNumber, DataSaver.SpriteBackDefaultName))
        self.m_pokemonFrontShinySpriteLabel.setPixmap(self.generateSpritePixmap(pokemonNumber, DataSaver.SpriteFrontShinyDefaultName))
        self.m_pokemonBackShinySpriteLabel.setPixmap(self.generateSpritePixmap(pokemonNumber, DataSaver.SpriteBackShinyDefaultName))

        self.m_pokemonImageLabel.setPixmap(QtGui.QPixmap(f"{DataSaver.DefaultPokemonImageDataFolderPath}/{pokemonNumber}/{DataSaver.SpriteOfficialFrontDefaultName}"))
        self.m_pokemonType1Label.clear()
        self.m_pokemonType2Label.clear()

        self.m_pokemonNumberLabel.setText("N°{:0>3d}".format(pokemonNumber))
        self.m_pokemonNameLabel.setText(f"{pokemonData[Pokedex.JsonNameKey].upper()}")
        self.m_pokemonGenusLabel.setText(f"{pokemonData[Pokedex.JsonGenusKey]}")
        self.m_pokemonDescriptionLabel.setText(f"{pokemonData[Pokedex.JsonDescriptionKey]}")

        abilitiesText = "Abilities:"
        abilities = pokemonData[Pokedex.JsonAbilitiesKey]
        for ability in abilities:
            abilityText = ability[Pokedex.JsonNameKey].replace("-", " ")
            if ability[Pokedex.JsonAbilityIsHiddenKey]:
                abilityText = f"{abilityText} (hidden)"
            abilitiesText = f"{abilitiesText} {abilityText},"
        abilitiesText = abilitiesText[:-1]
        self.m_pokemonAbilitiesLabel.setText(abilitiesText)

        self.m_pokemonHeightLabel.setText(f"Height: {pokemonData[Pokedex.JsonHeightKey]/100} meters")
        self.m_pokemonWeightLabel.setText(f"Weight: {pokemonData[Pokedex.JsonWeightKey]/1000} kilograms")
        
        types =  pokemonData[Pokedex.JsonTypesKey]
        if len(types) >= 1:
            self.m_pokemonType1Label.setPixmap(QtGui.QPixmap(f"{DataSaver.DefaultTypeImageDataFolderPath}/{types[0]}.png"))
        if len(types) >= 2:
            self.m_pokemonType2Label.setPixmap(QtGui.QPixmap(f"{DataSaver.DefaultTypeImageDataFolderPath}/{types[1]}.png"))

        self.update()

    def generateSpritePixmap(self, pokemonNumber, fileName):
        spritePixmap = QtGui.QPixmap(f"{DataSaver.DefaultPokemonImageDataFolderPath}/{pokemonNumber}/{fileName}")
        spriteOpaqueRegion = QtGui.QRegion(spritePixmap.createMaskFromColor(QtCore.Qt.transparent)).boundingRect()
        newPixmap = QtGui.QPixmap(spriteOpaqueRegion.width(), spritePixmap.size().height())
        newPixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(newPixmap)
        drawPoint = QtCore.QPoint(0, newPixmap.height() - spriteOpaqueRegion.height())
        painter.drawPixmap(drawPoint, spritePixmap, spriteOpaqueRegion)
        painter.end()
        return newPixmap

    def validatePokemonNumber(self, pokemonNumber):
        if pokemonNumber < 1:
            return self.m_pokedex.m_maxPokemonNumber
        elif pokemonNumber > self.m_pokedex.m_maxPokemonNumber:
            return 1
        return pokemonNumber

    def paintEvent(self, event: QtGui.QPaintEvent):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setPen(QtGui.Qt.NoPen)

        rect = event.rect()
        width = rect.width()
        height = rect.height()
        offset = width / 10

        # Left shape
        polygon = QtGui.QPolygon()
        polygon.append(QtCore.QPoint(width / 70, height / 10))
        polygon.append(QtCore.QPoint(width, height / 10))
        polygon.append(QtCore.QPoint(width, height - height / 10))
        polygon.append(QtCore.QPoint(width / 70, height - height / 10))

        painter.setBrush(QtGui.QColor(251, 114, 72))
        painter.drawPolygon(polygon)

        # Middle shape
        polygon.clear()
        polygon = QtGui.QPolygon()
        polygon.append(QtCore.QPoint(width / 2 + offset - 30, 0))
        polygon.append(QtCore.QPoint(width, 0))
        polygon.append(QtCore.QPoint(width, height))
        polygon.append(QtCore.QPoint(width / 2 - offset - 30, height))
        
        painter.setBrush(QtGui.QColor(253, 121, 73))
        painter.drawPolygon(polygon)

        # Right shape
        polygon.clear()
        polygon = QtGui.QPolygon()
        polygon.append(QtCore.QPoint(width / 2 + offset, 0))
        polygon.append(QtCore.QPoint(width, 0))
        polygon.append(QtCore.QPoint(width, height))
        polygon.append(QtCore.QPoint(width / 2 - offset, height))

        painter.setBrush(QtGui.QColor(245, 82, 59))
        painter.drawPolygon(polygon)

        painter.end()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.buttons() == QtCore.Qt.LeftButton:
            newPosition = event.localPos() - self.m_dragPosition + self.window().pos()
            self.window().move(newPosition.x(), newPosition.y())
        else:
            return super().mouseMoveEvent(event)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.m_dragPosition = event.localPos()
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.m_dragPosition = QtCore.QPointF(0, 0)
        return super().mouseReleaseEvent(event)

    def event(self, e: QtCore.QEvent) -> bool:
        if e.type() != QtCore.QEvent.Paint and self.m_dragPosition == QtCore.QPointF(0, 0):
            self.update()
        return super().event(e)

    @QtCore.Slot()
    def onSelectFileButtonClicked(self):
        fileName, selectedFilter = QtWidgets.QFileDialog.getOpenFileName(self, "Please select an image", "", "Images (*.png *.jpg)")
        fileInfo = QtCore.QFileInfo(fileName)
        if fileInfo.exists() and fileInfo.isFile():
            self.m_fileName = fileName
            self.m_selectFileButton.setText("Image selected")
            self.m_classifyImageButton.setEnabled(True)

    @QtCore.Slot()
    def onClassifyImageButtonClicked(self):
        if self.m_fileName:
            self.m_pokemonImageLabel.loadWaitingImage()
            self.repaint()

            prediction = self.m_predictionModel.computePrediction(self.m_fileName)
            self.fillPokemonData(prediction[0])

            self.m_selectFileButton.setText("Select image...")
            self.m_classifyImageButton.setEnabled(False)

    @QtCore.Slot()
    def onTenPreviousPokemonButtonClicked(self):
        newPokemonNumber = self.validatePokemonNumber(self.m_currentSelectedPokemon - 10)
        self.fillPokemonData(newPokemonNumber)

    @QtCore.Slot()
    def onPreviousPokemonButtonClicked(self):
        newPokemonNumber = self.validatePokemonNumber(self.m_currentSelectedPokemon - 1)
        self.fillPokemonData(newPokemonNumber)

    @QtCore.Slot()
    def onNextPokemonButtonClicked(self):
        newPokemonNumber = self.validatePokemonNumber(self.m_currentSelectedPokemon + 1)
        self.fillPokemonData(newPokemonNumber)

    @QtCore.Slot()
    def onTenNextPokemonButtonClicked(self):
        newPokemonNumber = self.validatePokemonNumber(self.m_currentSelectedPokemon + 10)
        self.fillPokemonData(newPokemonNumber)
        