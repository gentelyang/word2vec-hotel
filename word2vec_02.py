from gensim.models import word2vec
import logging
from imp import reload
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"result.txt")
model = word2vec.Word2Vec(sentences,size=200)
print(model)
y1=model.similarity("早","中")
print(y1)
print("------\n")