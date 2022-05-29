from unicodedata import name


n = int(input("輸入筆數 n:"))
x = []
for i in range(n):
    m = input()
    m.split()
    x.append(m)
for i in x:
    print(i[0],"牌得到 ",i[1],"面")