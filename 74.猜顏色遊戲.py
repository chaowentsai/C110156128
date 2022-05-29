ans=["red","blue","red","green"]
while True:
    gus=input()
    if(gus=="red blue red green"):
        print("正確答案")
        break
    else:
        a=""
        b=gus.split(" ")
        for i in range(4):
            if ans[i]==b[i]:
              a+="1"
            elif ans[i]!=b[i] and ans.count(b[i])>0:
                a+="2"
            else:
                a+="3"
        print(a)