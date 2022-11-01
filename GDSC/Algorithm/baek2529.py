import sys
from itertools import permutations

k = int(sys.stdin.readline())
A = sys.stdin.readline().split()

result = []
for per in permutations([0,1,2,3,4,5,6,7,8,9],k+1) :
    sign = True
    for a in range(len(A)):
        if A[a] == '<':
            if per[a] < per[a+1] : 
                continue
            else: 
                sign = False
                break
        else:
            if per[a] > per[a+1] : 
                continue
            else: 
                sign = False
                break
    if sign:
        result.append(per)

print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))