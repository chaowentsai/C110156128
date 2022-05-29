a=input("答案4位數字:")
while True:
    b=input("4位數字:")
    if b=="0000":
        break
    else:
        a1=0
        b1=0
        if a==b:
            print("4A0B")
        else:
            for i in range(len(a)):
                if a[i]==b[i]:
                    a1+=1
                elif a[i]!=b[i] and a.count(b[i])>0:
                    b1+=1
            print(str(a1)+"A"+str(b)+"B")