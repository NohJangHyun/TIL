import sys

T = int(sys.stdin.readline())

#풀이 방법1
for t in range(T):
    R, S = sys.stdin.readline().split()
    for s in S:
        for r in range(int(R)):
            print(s, end="")
    print()
    
# 풀이 방법2    
# for t in range(T):
#     R, S = sys.stdin.readline().split()
#     for s in S:
#         print(s*int(R), end="")
#     print()