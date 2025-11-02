pythonn, p, q = map(int, input().split())
straw_berry = list(map(int, input().split()))
grape = list(map(int, input().split()))

magic_numbers = []
possible = True

for dalgichoding, muscat in zip(straw_berry, grape):
    found = False
    for robot_moves in range(10001):
        if dalgichoding + robot_moves * p == muscat + robot_moves * q:
            magic_numbers.append(robot_moves)
            found = True
            break
    if not found:
        possible = False
        break

if possible:
    print("YES")
    print(*magic_numbers)
else:
    print("NO")