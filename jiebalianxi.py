import jieba
s=list(map(jieba.lcut("我是李洋，我爱自然语言处理",1)))
# s=jieba.lcut("我是李洋，我爱自然语言处理")
print(s)