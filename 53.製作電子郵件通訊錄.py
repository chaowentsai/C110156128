import email


n = int(input("輸入n值:"))
a = {}
for i in range(n):
    name = input("請輸入姓名:")
    email = input("請輸入電子郵件:")
    a[name] = email
sec =  input("請輸入要查詢的電子郵件的姓名:")
print(sec,"電子郵件帳號為:",a[sec])