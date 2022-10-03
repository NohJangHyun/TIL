import sys

N = int(sys.stdin.readline())
num = str(sys.stdin.readline())
sum = 0
for n in range(N):
    sum += int(num[n])
    
print(sum)