import sys

r=sys.stdin.buffer.readline
t=int(r())
o=[]
for _ in range(t):
    n,k=map(int,r().split())
    s=n-1
    lo,hi=0,2*s//k+1
    while lo<=hi:
        m=(lo+hi)//2
        v=k*m*(m+1)//2
        if v<=s: lo=m+1
        else: hi=m-1
    m=hi
    d=s-k*m*(m+1)//2
    if m&1: p=k*((m+1)//2)
    else: p=-k*(m//2)
    if d==0:
        o.append(f"{p} {'R' if (m+1)&1 else 'L'}")
    else:
        if (m+1)&1:
            o.append(f"{p+d} R")
        else:
            o.append(f"{p-d} L")
print("\n".join(o))
