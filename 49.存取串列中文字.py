x=input("請輸入英文句子:")
list1=x.split(" ")
list2=[]
for i in range(len(list1)):
    list2.append(list1[i])
n=list(reversed(list2))
print("輸出結果:",n)