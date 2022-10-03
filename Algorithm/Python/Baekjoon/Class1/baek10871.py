import sys

N, X = map(int, sys.stdin.readline().split())
list = sys.stdin.readline().split()

for l in list:
    if int(l) < X:
        print(l, end= " ")
    else:
        continue