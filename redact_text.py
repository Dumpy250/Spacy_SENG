import spacy
from pathlib import Path
class Redact:
	def __init__(self):
		self.nlp = spacy.load('en_core_web_sm')

	def replace_name_with_placeholder(self, token):
		if token.ent_iob != 0 and token.ent_type_ == "DOG":
			return "[REDACTED] "
		else:
			return token.text

	def scrub(self, text_file):
		text = Path(text_file).read_text()
		doc = self.nlp(text)
		with doc.retokenize() as retokenizer:
			for ent in doc.ents:
				retokenizer.merge(ent)
		tokens = map(self.replace_name_with_placeholder, doc)
		return "".join(tokens)
