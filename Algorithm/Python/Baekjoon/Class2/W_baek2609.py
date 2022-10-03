#유클리드 호제법으로 접근
#최대공약수는 x1>x2일때 x1과 x2를 x2로 나눈 나머지의 최대 공약수와 같음
#최소공배수는 x1과 x2의 곱을 x1과 x2의 최대 공약수로 나눈 값
import sys

x1, x2 = map(int, sys.stdin.readline().split())

def gcd(x1, x2):
    while x2 > 0:
        x1, x2 = x2, x1 % x2
    return x1

# 최소공배수 
# a와 b의 곱을 a와 b의 최대 공약수로 나눈 값
def lcm(x1, x2):
    return x1 * x2 // gcd(x1, x2)


print(gcd(x1, x2))
print(lcm(x1, x2))


#틀린 풀이
# x1 = abs(x1)
# x2 = abs(x2)

# n = 2
# ans = 1
# while True:
#     if x1 == 0 or x2 == 0:
#         print(ans*max(x1,x2))
#         print(0)
#         break
#     if n == 9:
#         print(ans)
#         print(ans*x1*x2)
#         break 
#     elif x1%n == 0 and x2%n==0:
#         x1 = int(x1/n)
#         x2 = int(x2/n)
#         print(x1)
#         print(x2)
#         ans *= n
#         print(ans)
#         print("_____________")
#     else:
#         n += 1  