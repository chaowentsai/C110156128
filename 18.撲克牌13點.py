
A=1
J=11
Q=12
K=13
card=input("輸入一副牌:").split(" ")
ans=0
for i in card:
    if i=="A":
        ans+=1
    elif i=="J":
        ans+=11
    elif i=="Q":
        ans+=12
    elif i=="K":
        ans+=13
    else:
        ans+=int(i)
print(ans)