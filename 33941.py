n=int(input())
wallet=[-1]*500
wallet[0]=0
for _ in range(n):
    card=int(input())
    if 500<card<20000:
        loot,junk=card-500,card%500
        fresh=wallet[:]
        for i in range(500):
            if wallet[i]>=0:fresh[(i+junk)%500]=max(fresh[(i+junk)%500],wallet[i]+loot)
        wallet=fresh
print(max(wallet[0],0))