from ast import Num


num = int(input("輸入一正整數:"))
if num % 2 == 0 and num % 11 == 0 and num % 5 != 0 and num % 7 != 0:
    print(num,"為新公倍數?:YES")
else:
    print(num,"為新公倍數?:NO")