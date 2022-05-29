y = int(input("輸入一個度數(正整數)"))
if y < 120:
    print("Summer months:",y*2.10,"\nNon-Summer months",y*2.10)
elif 121<y<330:
    print("Summer months:",(y-120)*3.02+120*2.10,"\nNon-Summer months",(y-120)*2.68+120*2.10)
elif 331<y<500:
    print("Summer months:",(y-330)*4.39+210*3.02+120*2.10,"\nNon-Summer months",(y-330)*3.61+210*2.68+120*2.10)
elif 501<y<700:
    print("Summer months:",(y-500)*4.97+170*4.39+210*3.02+120*2.10,"\nNon-Summer months",(y-500)*4.01+170*3.61+210*2.68+120*2.10)
else:
    print("Summer months:",(y-700)*5.63+200*4.97+170*4.39+210*3.02+120*2.10,"\nNon-Summer months",(y-700)*4.50+200*4.01+170*3.61+210*2.68+120*2.10)
    