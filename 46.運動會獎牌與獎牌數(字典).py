x = input("處理方式(1)字典(2)串列：")
gol = input("金 ")
sev = input("銀 ")
bro = input("銅 ")
god = input("優 ")
dict1 = {"金牌":gol,"銀牌":sev,"銅牌":bro,"優牌":god}
if x == "1":
    key = dict1.keys()
    value = dict1.values()
    key2 = list(key)
    value2 = list(value)
    for i in range(4):
        print("%s得到%s面"%(key2[i],value[i]))
else:
    items1 = list(dict1.items())
    for key3,value2 in items1:
        print("%s得到%s面"%(key3,value2))