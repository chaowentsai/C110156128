ans=list(input("請輸入第一組數字:"))
qus=list(input("請輸入第二組數字:"))
a=0
b=0
for i in ans:
    for j in qus:
        if i==j:
            if ans.index(i)==qus.index(j):
                a+=1
            else:
                b+=1
if a==4:
    print(a,"A",b,"B全對")
else:
    print(a,"A",b,"B加油")