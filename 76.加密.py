while True:
    x=list(input("請輸入密碼:"))
    if len(x)!=6:
        print("請重新輸入密碼")
        continue
    a=""
    for i in range(0,6):
        b=str((int(x[i])*2)%7)
        a+=b
    print(a)