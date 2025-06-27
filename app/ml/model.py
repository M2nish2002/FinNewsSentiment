from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import torch.nn.functional as F

MODEL_NAME = "yiyanghkust/finbert-tone"  # A well-known financial sentiment model

class SentimentModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        self.model.eval()  # Set to eval mode

    def predict(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = F.softmax(outputs.logits, dim=1)
            confidence, predicted_class = torch.max(probs, dim=1)
            label = self.model.config.id2label[predicted_class.item()]
            return {"label": label, "confidence": confidence.item()}