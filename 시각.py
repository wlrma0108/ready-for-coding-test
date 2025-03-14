h = int(input())

count = 0

#어째서 +1을 하지?? 0시부터 시작이구나!

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                # 이게 왜 돌아가지? str로서 123이러한 문자열이 만들어진다. 그중에 3이 포함되었는지...
                count +=1

print(count)