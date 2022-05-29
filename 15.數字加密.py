n = int(input("輸入一組四位數字為:"))
ans =[]
for i in range(n):
    ans.append((int(i)+7)%10)
print(str(ans[3])+str(ans[4])+str(ans[1])+str(ans[2]))