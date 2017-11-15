#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import gensim
# model = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# sentences = word2vec.Text8Corpus(u"E:\pyworksapce\COAE2015_opinion_identification-master\\result.txt")
# model = word2vec.Word2Vec(sentences, size=200)
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences=word2vec.Text8Corpus(u"corpus.txt")

model=word2vec.Word2Vec(sentences,size=200)
print(model)

# y1 = model.similarity([u'前'], [u'后'])
try:
    y1=model.similarity([u'前'], [u'后'])
except KeyError:
    y1=0
print (u"【少】和【早】的相似度为：", y1)
print ("--------\n")

# 计算某个词的相关词列表
y2 = model.most_similar([u""], topn=20)  # 20个最相关的
print (u"和【少】最相关的词有：\n")
for item in y2:
    print (item[0], item[1])
print ("--------\n")

# 寻找对应关系
print (u"书-不错，质量-")
y3 = model.most_similar([u'质量', u'不错'], [u'书'], topn=3)
for item in y3:
    print (item[0], item[1])
print ("--------\n")

# # 寻找不合群的词
# y4 = model.doesnt_match(u"书 书籍 教材 很".split())
# print u"不合群的词：", y4
# print "--------\n"

# 保存模型，以便重用
model.save(u"result.model")
# 对应的加载方式
# model_2 = word2vec.Word2Vec.load("text8.model")

# 以一种C语言可以解析的形式存储词向量
model.save_word2vec_format(u"result.model.bin", binary=True)
# 对应的加载方式
# model_3 = word2vec.Word2Vec.load_word2vec_format("text8.model.bin", binary=True)

if __name__ == "__main__":
    pass