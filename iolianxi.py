import re
import jieba
def jieba_cut(inputFile,outputFile):

    fin = open('1.txt','r').readlines()
    fout = open('corpus2.txt','w')

    for eachLine in fin:
        line = eachLine.strip().decode('utf-8','ignore')
        line = re.sub('<.*?>','',line)
        wordlist = list(jieba.cut(line))
        outStr = ''
        for word in wordlist:
            outStr += word
            outStr += ' '
        fout.write(outStr.strip().encode('utf-8')+'\n')#写入到文件中

    fin.close()
    fout.close()