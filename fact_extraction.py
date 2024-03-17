import spacy
import textacy.extract
from pathlib import Path


class FactExtraction:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def extract_facts(self, text_file):
        text = Path(text_file).read_text()
        doc = self.nlp(text)
        facts = textacy.extract.semistructured_statements(doc, entity="Dogs", cue="be", )
        for statement in facts:
            subject, verb, fact = statement
            return f" - {fact}"
