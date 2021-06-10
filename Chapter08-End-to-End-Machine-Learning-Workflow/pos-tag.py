import spacy
import en_core_web_sm
from spacy import displacy
import IPython
from pathlib import Path
import spacy.attrs
from contextlib import redirect_stdout

sp = spacy.load('en_core_web_sm')
textfile = sp(open('/pfs/data-clean/lemmatized.txt', "r", encoding='utf-8').read())
with open('/pfs/out/pos-table.txt', 'w') as f:
     with redirect_stdout(f):
         for word in textfile:
             print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

with open('/pfs/out/pos-number.txt', 'w') as file:
     with redirect_stdout(file):
         count_tags = textfile.count_by(spacy.attrs.IDS['POS'])
         for i, count in count_tags.items():
             tags = textfile.vocab[i].text
             print(tags, count)

image = displacy.render(textfile, style='dep', options={"compact": True, "distance": 70})
f = open('/pfs/out/pos-tag-dependency.svg', "w")
f.write(image)
f.close()
