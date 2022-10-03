import sys

N = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
list.sort()
print(list[0], list[N-1])