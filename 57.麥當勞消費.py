upg = input("請選擇主餐及升級的套餐:")
dri = input("是否升級成大杯飲料:")
fri = input("是否換成大薯:")
money = 0
if upg[0] == "1":
    money += 72
    if upg[1] =="A":
        money += 55
    else:
        money += 68
elif upg[0] == "2":
    money += 62
    if upg[1] =="A":
        money += 55
    else:
        money += 68
elif upg[0] == "3":
    money += 82
    if upg[1] =="A":
        money += 55
    else:
        money += 68
elif upg[0] == "4":
    money += 44
    if upg[1] =="A":
        money += 55
    else:
        money += 68
elif upg[0] == "5":
    money += 72
    if upg[1] =="A":
        money += 55
    else:
        money += 68
if dri == "是":
    money += 7
if fri == "是":
    money += 13
print("總共為:",money,"元")