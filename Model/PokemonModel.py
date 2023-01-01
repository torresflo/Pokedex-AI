import torch
from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification

class PokemonModel:
    DefaultModelPath = "./data/model"

    def __init__(self):
        self.m_device = "cuda" if torch.cuda.is_available() else "cpu"

        print("Loading model...")
        self.m_featureExtractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')
        self.m_model = ViTForImageClassification.from_pretrained(PokemonModel.DefaultModelPath).to(self.m_device)
        print("Model loaded")

    def computePrediction(self, fileName):
        with Image.open(fileName).convert("RGB") as image:
            inputs = self.m_featureExtractor(images=image, return_tensors="pt").to(self.m_device)
            outputs = self.m_model(**inputs)
            logits = outputs.logits
                
            predictedClass = logits.argmax().item()
            predictionProbability = logits.softmax(dim=1).max().item() * 100.0
            # predictedPokemon = self.m_model.config.id2label[predictedClass] 
            return [predictedClass + 1, predictionProbability]