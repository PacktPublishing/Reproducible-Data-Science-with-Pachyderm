import spacy
import random
from spacy.util import minibatch
from spacy.training import Example
from contextlib import redirect_stdout
import simplejson as json
import pickle

nlp=spacy.load("en_core_web_lg")
ner=nlp.get_pipe("ner")
data = open("/pfs/data/training-data.json")
data = json.loads(data.read())

optimizer = nlp.create_optimizer()
other_pipes = [p for p in nlp.pipe_names if p != "ner"]
with nlp.disable_pipes(*other_pipes):
    for i in range(30):
        random.shuffle(data)
        losses = {}
        for text, annotations in data:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.1, sgd=optimizer, losses=losses)
        print(losses)

test_text = 'Headless Horseman came to see Ichabod Crane.'
doc = nlp(test_text)
with open ('/pfs/out/ner-improved.txt', 'w') as f:
    with redirect_stdout(f):
        for i in doc.ents:
            print(i.label_, " -- ", i.text)

pickle.dump(nlp, open('/pfs/out/ner-improved-model.p', 'wb'))

