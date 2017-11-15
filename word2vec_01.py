#encoding=utf-8

from gensim.models import word2vec
import logging
import sys
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences=word2vec.Text8Corpus("corpus.txt") #jia zai yu liao ku
model=word2vec.Word2Vec(sentences,size=200)
print(model)
# try:
#     y1=model.similarity(u"电脑",u"平板")#计算两个词的相似度
# except KeyError:
#     y1=0
# print(u"电脑和笔记本的相似度为：",y1)
# print("--------\n")
# #计算某个词的相关词列表
# y2=model.most_similar(u"电脑",topn=10)
# print(u"和电脑相关的有：\n")
# for item in y2:
#     print(item[0],item[1])
# print("-----\n")
#
# #寻找对应关系
# print(u"男童鞋的最爱")
# y3=model.most_similar([u'最爱'],[u'男童鞋'],topn=3)
# for item in y3:
#     print(item[0],item[1])
# print("------\n")
#
# #寻找不合群的词
# y4=model.doesnt_match(u"男童鞋的最爱奥".split())
# print("不合群的词：",y4)
# print("----\n")
#
# #保存模型，以便重用
# model.save(u"corpus.model")

# from gensim.models import  word2vec
# sentences=word2vec.Text8Corpus("result.txt")
# model=word2vec.Word2Vec(sentences,min_count=5,size=50)
# print(model)
#
# y2=model.similarity("早","中")
# print(y2)
# #
# # for i  in model.most_similar(u"电脑"):
# #     print(i[0],i[1])


























