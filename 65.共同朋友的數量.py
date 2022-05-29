a = list(input("請輸入A的好友：").split())
b = list(input("請輸入B的好友：").split())
n = 0
for i in a:
    if i in b:
        n += 1
print(n)