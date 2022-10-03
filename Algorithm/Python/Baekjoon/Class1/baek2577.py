import sys 

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

num = str(A*B*C)
for n in range(10):
    cnt = num.count(str(n))
    print(cnt)
