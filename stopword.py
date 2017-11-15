import jieba

f=open('fenci3_result','r',encoding='utf-8').read()
stopwords={}.fromkeys([line.rstrip() for line in open('stopword.txt')])
outstr=''
for word in f:
    if word not  in stopwords:
        if word !='\t':
            outstr+=word
            outstr+=" "

print(outstr)



