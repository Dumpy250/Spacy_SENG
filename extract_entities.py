import spacy
from pathlib import Path
class EntityExtraction:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def extract_entities(self, text_file):
        text = Path(text_file).read_text(encoding="utf-8")
        doc = self.nlp(text)
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        return entities
