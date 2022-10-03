import sys

#input : 29 10 14 37 13
#input : 8 31 48 73 3 65 20 29 11 15

# 1. 정렬할 원소 array에 담기
array = []
array = list(map(int, sys.stdin.readline().split()))

# 2. 인접한 두 원소를 비교하면서 제일 큰 원소를 뒤로 이동하는 과정 반복
for a in range(len(array)-1, 0, -1):
    print("progress", len(array)-a)
    print("--------------------")
    for i in range(0, a):
        print("idx : ", i, "and", i+1, "comparing")
        print("array[%d] : "%i, array[i])
        print("array[%d] : "%(i+1), array[i+1])
        
        if array[i] > array[i+1]:
            print("change", array[i], "and", array[i+1])
            print("before : ", array)
            array[i],  array[i+1] = array[i+1], array[i]
            print("after : ", array, "\n")
        else:
            print("nothing changed")
            print("before : ", array)
            print("after : ", array, "\n")
            continue
print("--------------------")
print("final : ", array)