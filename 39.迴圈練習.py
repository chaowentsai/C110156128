n = int(input())
for i in range(1,n-2):
    print(" "*(4-i)+"*"*(i)+"*"*(i-1))
for i in reversed(range(1,n-3)):
    print(" "*(4-i)+"*"*(i)+"*"*(i-1))