#입력 받는 3변의 길이는 각각 x,y,z를 의미하지 않음, 그냥 변의 길이가 주어지는 것
import sys

while True:
    T = list(map(int, sys.stdin.readline().split()))
    if sum(T) == 0:
        break
    max_T = max(T)
    T.remove(max_T)
    if T[0]**2 + T[1]**2 == max_T**2:
        print("right")
    else:
        print("wrong")