full=250
half=175
x=int(input("組數為"))
for i in range(x):
    mov=input("第"+str(i+1)+"組(以空白間隔開)：")
    money=mov.split()
    print("第"+str(i+1)+"組應收費用:",(int(money[0])*250)+(int(money[1])*175),"元")