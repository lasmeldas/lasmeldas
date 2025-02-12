m=[]
for i in range(5):
    row=[int(i) for i in input().split()]
    m.append(row)
r=0
c=0
for i in range(5):
    for j in range(5):
        if m[i][j]==1:
            r=i
            c=j
a=abs(c-2)+abs(r-2)
print(a)
