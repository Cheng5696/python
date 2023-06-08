import jieba
with open("E:\python学习资料\宠魅.txt","r",encoding="utf-8") as f:
    li = jieba.lcut(f.read())
    count = {}
    for i in li:
        if len(i) == 1:
            continue
        else:
            count[i] = count.get(i,0) + 1
    li1 = list(count.items())
    li1.sort(key=lambda x:x[1],reverse=True)
    print(li1)