import spacy
from pathlib import Path

class VerbExtraction:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def extract_verbs(self, text_file):
        text = Path(text_file).read_text(encoding="utf-8")
        doc = self.nlp(text)
        verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
        return verbs