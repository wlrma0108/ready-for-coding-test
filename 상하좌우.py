size = int(input())
#이해하지 못하면 당연하게 못 짜겠지. 고민을 많이하자 답이 안나오더라도.
go = input().split()
x, y = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 이거해설이 잘못된 것 같다. lrud와 매칭이 안된다. 내가 이해를 못한건가?
move = ['L','R','U','D']

for going in go:
    for i in range(len(move)):
        if go == move[i]:
            nx = x+ dx[i]
            ny = y+ dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)











