from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"result.txt")
model = word2vec.Word2Vec(sentences, size=200)

print(model)
# 计算两个词的相似度/相关程度
try:
    y1 = model.similarity(u"早餐", u"宾馆")
except KeyError:
    y1 = 0
print(u"【国家】和【国务院】的相似度为：", y1)

#
# 计算某个词的相关词列表
y2 = model.most_similar(u"控烟", topn=20)  # 20个最相关的
print
u"和【控烟】最相关的词有：\n"
for item in y2:
    print
    item[0], item[1]
print
"-----\n"

# 寻找对应关系
print
u"书-不错，质量-"
y3 = model.most_similar([u'质量', u'不错'], [u'书'], topn=3)
for item in y3:
    print
    item[0], item[1]
print
"----\n"

# 寻找不合群的词
y4 = model.doesnt_match(u"书 书籍 教材 很".split())
print
u"不合群的词：", y4
print
"-----\n"