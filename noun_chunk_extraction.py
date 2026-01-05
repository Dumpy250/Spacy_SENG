import spacy
from pathlib import Path


class NounExtraction:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def extract_nouns(self, text_file):
        text = Path(text_file).read_text(encoding="utf-8")
        doc = self.nlp(text)
        nouns = [token.text for token in doc if token.pos_ == "NOUN"]
        return nouns
