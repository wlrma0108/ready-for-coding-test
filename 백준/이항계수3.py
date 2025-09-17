import sys

def power(base, exp):
    result = 1
    base %= p
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        exp //= 2
    return result

N, K = map(int, sys.stdin.readline().split())
p = 1000000007

fact = [1] * (N + 1)
for i in range(2, N + 1):
    fact[i] = (fact[i - 1] * i) % p

numerator = fact[N]
denominator = (fact[K] * fact[N - K]) % p

inverse_denominator = power(denominator, p - 2)

result = (numerator * inverse_denominator) % p

print(result)