n=1
total = 1
m = int(input("請輸入階層值M"))
while (total<m):
    total *= n
    n += 1
    if total > m :
        print("超過M為",m,"的最小階層N值為:",n-1)