import spacy
from spacy import displacy
from contextlib import redirect_stdout

sp = spacy.load("en_core_web_lg")
def display_entities(text):
     with open ('/pfs/out/ner-list.txt', 'w') as f:
         with redirect_stdout(f):
             if text.ents:
                 for i in text.ents:
                     print(i.text+' - '+str(i.start_char)+' - '+str(i.end_char)+' - '+i.label_+' - '+str(spacy.explain(i.label_)))
text = sp(open('/pfs/data-clean/text.txt', "r", encoding='utf-8').read())
display_entities(text)

with open ('/pfs/out/ner-labels.html', 'w') as f:
      with redirect_stdout(f):
          for i in text.ents:
              html=displacy.render(text, style="ent", page=True)
              print(html)
