for _ in[0]*int(input()):
    k,n=map(int,input().split());bag=[1]+[0]*n
    for dice in range(1,k+1):
        for coin in range(1,n+1):bag[coin]+=bag[coin-1]
        for coin in range(n,dice,-1):bag[coin]-=bag[coin-dice-1]
    print(bag[n])