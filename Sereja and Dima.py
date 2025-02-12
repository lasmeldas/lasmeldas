x=int(input())
y=[int(i) for i in input().split()]
s=0
d=0
l=0
r=len(y)-1
turn=0
while l<=r:
    if y[l]>y[r]:
        k=y[l]
        l+=1
    else:
        k=y[r]
        r-=1
    if turn%2==0:
        s+=k
    else:
        d+=k
    turn+=1
print(s,d)
