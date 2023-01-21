import requests
import json
import os

from PIL import Image
from io import BytesIO

from progress.bar import ShadyBar

from Utils.DataTools import DataSaver

class Pokedex:
    JsonNameKey = "name"
    JsonValueKey = "value"
    JsonGenerationKey = "generation"
    JsonTypesKey = "types"
    JsonBaseStatsKey = "base_stats"
    JsonAbilitiesKey = "abilities"
    JsonAbilityIsHiddenKey = "is_hidden"
    JsonHeightKey = "height"
    JsonWeightKey = "weight"
    JsonIsBabyKey = "is_baby"
    JsonIsLegendaryKey = "is_legendary"
    JsonIsMythicalKey = "is_mythical"
    JsonGenusKey = "genus"
    JsonDescriptionKey = "description"
    JsonSpriteFrontDefaultKey = "sprite_front_default_url"
    JsonSpriteBackDefaultKey = "sprite_back_default_url"
    JsonSpriteFrontShinyDefaultKey = "sprite_front_shiny_default_url"
    JsonSpriteBackShinyDefaultKey = "sprite_back_shiny_default_url"
    JsonSpriteHomeFrontDefaultKey = "sprite_home_front_default_url"
    JsonSpriteOfficialFrontDefaultKey = "sprite_official_front_default_url"

    def __init__(self):
        self.m_data = {}
        self.m_maxPokemonNumber = 151
        self.m_defaultDataFolder = "./data"
        self.m_defaultJsonFileName = f"{self.m_defaultDataFolder}/pokemon_data.json"

    def getGeneration(self, pokemonNumber):
        if pokemonNumber <= 151:
            return 1
        elif pokemonNumber <= 251:
            return 2
        elif pokemonNumber <= 386:
            return 3
        elif pokemonNumber <= 493:
            return 4
        elif pokemonNumber <= 649:
            return 5
        elif pokemonNumber <= 721:
            return 6
        elif pokemonNumber <= 809:
            return 7
        elif pokemonNumber <= 905:
            return 8
        
        return 0

    def retrieveData(self):
        progressBar = ShadyBar("Retrieving Pokémon Data...", max = self.m_maxPokemonNumber)
            
        for pokemonNumber in range (1, self.m_maxPokemonNumber + 1):
            progressBar.next()
            
            request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonNumber}/")
            pokemonData = json.loads(request.content)
            
            types = []
            for jsonType in pokemonData["types"]:
                types.append(jsonType["type"]["name"])

            stats = []
            for jsonStat in pokemonData["stats"]:
                stat = {
                    Pokedex.JsonNameKey: jsonStat["stat"]["name"],
                    Pokedex.JsonValueKey: jsonStat["base_stat"]
                }
                stats.append(stat)

            abilities = []
            for abilityStat in pokemonData["abilities"]:
                ability = {
                    Pokedex.JsonNameKey: abilityStat["ability"]["name"],
                    Pokedex.JsonAbilityIsHiddenKey: abilityStat["is_hidden"]
                }
                abilities.append(ability)

            request = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemonNumber}/")
            pokemonSpeciesData = json.loads(request.content)

            for jsonGenus in pokemonSpeciesData["genera"]:
                if jsonGenus["language"]["name"] == "en":
                    genus = jsonGenus["genus"]
                    break

            for jsonDescription in pokemonSpeciesData["flavor_text_entries"]:
                if jsonDescription["language"]["name"] == "en" and jsonDescription["version"]["name"] == "lets-go-pikachu":
                    description = jsonDescription["flavor_text"].replace('\n', ' ')
                    break

            self.m_data[pokemonNumber] = {
                Pokedex.JsonNameKey: pokemonData["name"],
                Pokedex.JsonGenerationKey: self.getGeneration(pokemonNumber),
                Pokedex.JsonTypesKey: types,
                Pokedex.JsonBaseStatsKey: stats,
                Pokedex.JsonAbilitiesKey: abilities,
                Pokedex.JsonHeightKey: pokemonData["height"] * 10, # in cm
                Pokedex.JsonWeightKey: pokemonData["weight"] * 100, # in gramms
                Pokedex.JsonIsBabyKey: pokemonSpeciesData["is_baby"],
                Pokedex.JsonIsLegendaryKey: pokemonSpeciesData["is_legendary"],
                Pokedex.JsonIsMythicalKey: pokemonSpeciesData["is_mythical"],
                Pokedex.JsonGenusKey: genus,
                Pokedex.JsonDescriptionKey: description,
                Pokedex.JsonSpriteFrontDefaultKey: pokemonData["sprites"]["front_default"],
                Pokedex.JsonSpriteBackDefaultKey: pokemonData["sprites"]["back_default"],
                Pokedex.JsonSpriteFrontShinyDefaultKey: pokemonData["sprites"]["front_shiny"],
                Pokedex.JsonSpriteBackShinyDefaultKey: pokemonData["sprites"]["back_shiny"],
                Pokedex.JsonSpriteHomeFrontDefaultKey: pokemonData["sprites"]["other"]["home"]["front_default"],
                Pokedex.JsonSpriteOfficialFrontDefaultKey: pokemonData["sprites"]["other"]["official-artwork"]["front_default"]
            }

    def retrieveAndSaveSprites(self):
        progressBar = ShadyBar("Retrieving Pokémon Sprites...", max = len(self.m_data))

        for pokemonNumber, item in self.m_data.items():
            progressBar.next()

            jsonKeys = [
                Pokedex.JsonSpriteFrontDefaultKey,
                Pokedex.JsonSpriteBackDefaultKey,
                Pokedex.JsonSpriteFrontShinyDefaultKey,
                Pokedex.JsonSpriteBackShinyDefaultKey,
                Pokedex.JsonSpriteHomeFrontDefaultKey,
                Pokedex.JsonSpriteOfficialFrontDefaultKey
                ]
            fileNames = [
                DataSaver.SpriteFrontDefaultName,
                DataSaver.SpriteBackDefaultName,
                DataSaver.SpriteFrontShinyDefaultName,
                DataSaver.SpriteBackShinyDefaultName,
                DataSaver.SpriteHomeFrontDefaultName,
                DataSaver.SpriteOfficialFrontDefaultName
                ]
            for key, fileName in zip(jsonKeys, fileNames):
                url = self.m_data[pokemonNumber][key]
                content = requests.get(url).content
                image = Image.open(BytesIO(content)).convert('RGBA')
                DataSaver.saveImage(image, DataSaver.DefaultPokemonImageDataFolderPath, pokemonNumber, fileName)

    def saveDataToJsonFile(self, jsonFileName):
        with open(jsonFileName, 'w+', encoding='utf-8') as file:
            json.dump(self.m_data, file, indent=2, ensure_ascii=False)

    def loadDataFromJsonFile(self, jsonFileName):
        with open(jsonFileName, 'r', encoding='utf-8') as file:
            self.m_data = json.load(file)

    def retrieveDataAndSaveToJson(self):
        self.retrieveData()
        DataSaver.createFolder(self.m_defaultDataFolder)
        self.saveDataToJsonFile(self.m_defaultJsonFileName)
        self.retrieveAndSaveSprites()

    def autoInitialize(self):
        if os.path.exists(self.m_defaultJsonFileName):
            self.loadDataFromJsonFile(self.m_defaultJsonFileName)
        else:
            self.retrieveDataAndSaveToJson()