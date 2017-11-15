import jieba
import re
fin=open("posWords.txt",'rb').readlines()
fout=open("fenci3.txt",'wb')
fout1=open("fenci3_result2",'wb')
for line in fin:
    line=line.strip()
    wordlist=list(jieba.cut(line))
    for word in wordlist:
        fout.write(word.encode('utf-8'))
        stopwords={}.fromkeys([line.rstrip() for line in open('stopword.txt')])
        for seg in wordlist:
            if seg not in stopwords:
                fout1.write(seg)