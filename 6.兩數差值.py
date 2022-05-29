N = str(input("輸入數值為:"))
b=N.split(",")
b.sort()
N2=sorted(b,reverse=True)
s=""
g=""
for i in range(0,5):
    s+=str(N2[i])
    g+=str(b[i])
    x=int(s)-int(g)
print(x)
