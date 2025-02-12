x=int(input())
y=[int(i) for i in input().split()]
shot=int(input())
for i in range(shot):
    w,p=map(int,input().split())
    w-=1
    l=p-1
    r=y[w]-p
    if w>0:
        y[w-1]+=l
    if w<x-1:
        y[w+1]+=r
    y[w]=0
for i in y:
    print(i)
