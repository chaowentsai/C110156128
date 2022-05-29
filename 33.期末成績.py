chi = int(input("國文:"))
eng = int(input("英文:"))
mat = int(input("微積分"))
pyc = int(input("體育"))
pyt = int(input("程式設計"))
avg = (chi+eng+mat+pyc+pyt)/5
max = max(chi,eng,mat,pyc,pyt)
min = min(chi,eng,mat,pyc,pyt)
print("平均分數:%.2f"%(avg))
if max == chi:
    print("最高分科目：國文",max,"分")
elif max == eng:
    print("最高分科目：英文",max,"分")
elif max == mat:
    print("最高分科目：微積分",max,"分")
elif max == pyc:
    print("最高分科目：體育",max,"分")
elif max == pyt:
    print("最高分科目：程式設計",max,"分")

if min == chi:
    print("最低分科目：國文",min,"分")
elif min == eng:
    print("最低分科目：英文",min,"分")
elif min == mat:
    print("最低分科目：微積分",min,"分")
elif min == pyc:
    print("最低分科目：體育",min,"分")
elif min == pyt:
    print("最低分科目：程式設計",min,"分")
    
