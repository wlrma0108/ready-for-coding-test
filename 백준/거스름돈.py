#500원 100원 50원 10원이 무한하게 존재한다. 
#그리디 알고리즘 문제

coin = [500,100,50,10]
#이걸 몇번 추출했냐 카운팅을 해야한다. 

money = int(input())
cost = int(input())
remain = money - cost

for a in coin:
    count += remain/coin
    remain %= coin


print(count)

