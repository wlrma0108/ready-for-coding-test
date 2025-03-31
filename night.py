input =input()
row = int(input[1])
column = int(input - int(ord('a'))) + 1
#이거보다 깔끔한 방법 없나?
step = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2), (-1,2),(-2,1)]

result = 0

for ste in step:
    nextr = row + step[0]
    nextc = column + step[1]
    # 다른 방법 없나?
    if ???

print(result)