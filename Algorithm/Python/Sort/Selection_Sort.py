# Problem : last_array가 max_array인 경우 max 값이 제대로 출력 안됨
import sys

#input : 29 10 14 37 13
#input : 8 31 48 73 3 65 20 29 11 15

# 1. 정렬할 원소 array에 담기
array = []
array = list(map(int, sys.stdin.readline().split()))

# 2. array에서 가장 큰 원소 찾고 마지막 원소와 교체 과정 반복
for a in range(len(array)-1, 0, -1):
    print("idx range : 0 ~", a)
    max_a = max(array[:a+1])
    last_a = array[a]
    max_i = array.index(max_a)
    last_i = array.index(last_a)
    print("max array : ", max_a)
    print("last array : ", last_a)
    print("max idx : ", max_i)
    print("last idx : ", last_i)
    print("before : ", array)
    if last_i == max_i:
        print("after : ", array, "\n")
        continue
    else:
        array[max_i] = last_a
        array[a] = max_a
        print("after : ", array, "\n")