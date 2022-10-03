# 각 자리수를 나누기를 통해 구하려고 함 => map
# import sys

# N = int(sys.stdin.readline())
# list = [0, 1, 10, 100, 1000, 10000, 100000, 1000000]
# sum = 0

# if len(str(N)) == 1:
#     print(N)    
# elif N <= 117:       
#     for i in range(10, 100):
#         sum = i + i//list[len(str(i))] + i%list[len(str(i))]
#         if N == sum:
#             print(i)
#             break
#         else:
#             continue
# else:
#     for i in range(100, N):
#         sum = i + (i//list[len]) + (i%100//10) + (i%10//1)
#         if sum == N:
#             print(i)
#             break
#         else:
#             continue

# Solution
import sys

N = int(sys.stdin.readline())

result = 0
for i in range(1, N+1):
    num = list(map(int, str(i)))
    result = i + sum(num)
    if result == N:
        print(i)
        break
    
    if i == N:
        print(0)
