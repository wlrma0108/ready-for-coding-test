n, m , k= int(input())
#<- 이건 내가짠 코드다. 답지에서는 아래와 같이 짠다. 
# n,m,k = map(int, input().split) 왜 스플릿을 하고 map을 사용는지 모르겠다. 
# 이해 했다. map함수가 (적용할 함수 여기에서는 int, 데이터) 이대로 입력하면 강제로 원하는 자료형형태로 데이터를 반환한다. 

n,m,k = map(int, input().split())
# 위함수는 input받은 데이터를 공백에 따라서 구분하고, 찢고, 정수형으로 반환한다는 뜻
# n = 데이터의 수 m = 숫자가 더해지는 횟수 k = 같은 숫자를  연속적으로 더할 수 있는 기회  

data = list(map(int,input().split()))

data.sort()
# 이거한줄이면 정렬이 된다. 어이가 없다 

first = data[n-1]
second = data[n-2]

#여기에데는 숫자 2개만 필요하구나

result = 0
while True:
    for i in range(k):
        if m ==0:
            break
         result +=first
         m-=1
    if m ==0 :
        break
    result += second
    m -= 1

print(result)