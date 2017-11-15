import jieba
import sys
import re
import nltk,pprint
with open('corpus.txt','r',encoding='utf-8') as f:
    for line in f:
        seg=jieba.cut(line.strip(),cut_all=False)
        s=' '.join(seg)
        m=list(s)
        with open('corpus2.txt','w') as f:
            for word in m:
                f.write(word)








# with open('1.txt','r') as f:
#     for line in f:
#         seg=jieba.cut(line.strip(),cut_all=False)
#         s=' '.join(seg)
#         m=list(s)
#         with open('fc2.txt','a+') as f:
#             for word in m:
#                 f.write(word)








# raw=open('1.txt').read()
# # raw=raw.decode('utf-8')
# print(len(raw))
# print(raw[2:100])
# f=jieba.cut(raw)
#
# print(f)




# f=open("1.txt",'r').read()
# # f1=jieba.cut(f,cut_all=True)
# print(jieba.cut(f,cut_all=True))
# words=" ".join(f1)
# print(words)
# lines=f.readlines()
# for line in lines:
#     line.replace('\t','').replace('\n','').replace(' ','').replace('[','').replace('[','')
#     seg_list=jieba.cut(line,cut_all=False)
#     f.write(" ".join(seg_list))
# f.close()