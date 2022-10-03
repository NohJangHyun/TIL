import sys

T = int(sys.stdin.readline())
for t in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    room = []
    for w in range(1, W+1):
        for h in range(1, H+1):
            if w < 10:
                num = int(str(h) + "0" + str(w))
                room.append(num)
            else:
                num = int(str(h) + str(w))
                room.append(num)
    print(room[N-1])
    

#더 효율적인 방법
# T = int(input())
# while T > 0:
#     h, w, n = map(int, input().split())
#     floor = n%h
#     num = n//h+1
#     if floor == 0:
#         num = n//h
#         floor = h
#     print(floor*100+num)
#     T-=1