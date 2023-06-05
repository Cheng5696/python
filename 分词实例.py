import jieba

txt = open("E:\Quan Qiu Jin Hua - Yao Gou.txt",encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse = True)
print("出现次数最多的是",items[0][0])
print("一共出现{}次".format(items[0][1]))