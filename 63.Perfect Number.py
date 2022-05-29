s=0
n=int(input("請輸入正整數"))
for i in range(1,n+1):
    if n!=i:
        if n%i==0:
            s+=i
if s==n:
    print("perfect")
elif s>n:
    print("abundant")
else:
    print("dcficient")