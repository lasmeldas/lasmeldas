a,b=map(int,input().split())
m=[int(i) for i in input().split()]
c=0
for i in m:
    if i>b:
        c+=2
    elif i<=b:
        c+=1
print(c)
