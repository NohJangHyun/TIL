import sys

N = int(sys.stdin.readline())
for n in range(1,N+1):
    cnt = N-n
    print(" "*cnt+ "*"*n)