#이항 계수의 정의 기억 안나서 찾아봄
import sys

N, K = map(int, sys.stdin.readline().split())

def fac(X):
    num = 1
    for x in range(X, 0, -1):
        num = num * x
    return num

if K < 0 or K > N:
    print(0)
else:
    ans = int(fac(N)/(fac(K) * fac(N-K)))
    print(ans)