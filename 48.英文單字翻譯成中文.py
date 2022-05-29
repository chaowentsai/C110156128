num = int(input("輸入筆數n:"))
x = {}
for i in range(num):
    a,b= input().split()
    x[a]=b
s = input("輸入欲查詢單字:")
if s in x:
    print(s,"的中文意思是",x.get(s))
else:
    print("字典未有此單字")