import os

from PIL import Image

class DataSaver:
    DefaultImageDataFolderPath = "./data/image"
    DefaultPokemonImageDataFolderPath = f"{DefaultImageDataFolderPath}/pokemon"
    DefaultTypeImageDataFolderPath = f"{DefaultImageDataFolderPath}/type"
    
    SpriteFrontDefaultName = "sprite_front_default.png"
    SpriteBackDefaultName = "sprite_back_default.png"
    SpriteFrontShinyDefaultName = "sprite_front_shiny_default.png"
    SpriteBackShinyDefaultName = "sprite_back_shiny_default.png"
    SpriteHomeFrontDefaultName = "sprite_home_front_default.png"
    SpriteOfficialFrontDefaultName = "sprite_official_front_default.png"

    def createFolder(folderName):
        if not os.path.isdir(folderName):
            os.makedirs(folderName, exist_ok=True)

    def getImageNumber(folderName):
        listOfFiles = os.listdir(folderName)
        return len(listOfFiles) + 1

    def saveImage(image : Image, saveDirectory, pokemonNumber, fileName):
        DataSaver.createFolder(f"./{saveDirectory}/{pokemonNumber}")
        image.save(f"./{saveDirectory}/{pokemonNumber}/{fileName}")