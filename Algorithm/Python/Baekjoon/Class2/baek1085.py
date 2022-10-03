import sys

x, y, w, h = map(int, sys.stdin.readline().split())

list = []
list.append(abs(w-x))
list.append(abs(h-y))
list.append(abs(x-0))
list.append(abs(y-0))
print(min(list))