



import spacy
nlp=spacy.load('en_core_web_sm')
doc=nlp(u'India is helding the cricket world cup this year')
for token in doc.ents:
  print(token,token.label_)
