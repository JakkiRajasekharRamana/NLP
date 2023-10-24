
import spacy
nlp=spacy.load('en_core_web_sm')

def show_lemmas(text):
  for token in text:
    print(f'{token.text:{12}}{token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}')

doc=nlp(u'India is holding the cricket world cup this year')

show_lemmas(doc)
