"""
猜数字
if else 练习
"""
import random

num = random.randint(1,100)

# 定义变量，记录测试次数
count = 0

# 设置循环标记
flag = True

while flag:
    guess_num = int(input("请输入你猜测的数据"))
    count += 1
    if guess_num == num : 
        print("猜中了")
        flag = False
    else :
        if guess_num > num :
            print("你输入大了")
        else :
            print("你输入小了")

print(f"你总共猜了{count}次")