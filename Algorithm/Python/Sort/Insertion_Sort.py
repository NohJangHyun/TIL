import sys

#input : 29 10 14 37 13
#input : 8 31 48 73 3 65 20 29 11 15

# 1. 정렬할 원소 array에 담기
array = []
array = list(map(int, sys.stdin.readline().split()))

for i in range(0, len(array)-1):
  print("index",i,"in progress")
  print("loc : ", array[:i+1])
  print("item : ", array[i+1])
  j = i
  while j >= 0 and array[j] > array[i+1]:
        j -= 1
  
  
  
lists = [8, 3, 2, 7, 6]

for i in range(1, len(lists)):
    j = i
    
    while j > 0 and lists[j - 1] > lists[j]:
        lists[j - 1], lists[j] = lists[j], lists[j - 1]
        j -= 1
print(lists)
  

      
    

