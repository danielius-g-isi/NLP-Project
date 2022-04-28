import spacy
from spacy import displacy
from tabulate import tabulate

nlp = spacy.load('en_core_web_sm')

data = []

text = input('Input text: ')

tokens = nlp(text)

data = []

for word in tokens.ents:
    dataset = [word.text, word.label_, spacy.explain(word.label_)]
    data.append(dataset)

print(tabulate(data, headers = ['Word', 'Label', 'Explanation'], tablefmt = 'github'))

displacy.serve(tokens, style = 'ent')