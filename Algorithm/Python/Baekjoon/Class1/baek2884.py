H, M = map(int, input().split())
if M >= 45:
    M -= 45
    print(H, M)
else:
    M = 60-(45-M)
    if H == 0:
        H = 23
        print(H, M)
    else:
        print(H-1, M)

# 기존 풀이
# import sys

# H, M = map(int, sys.stdin.readline().split())
# M -= 45
# if M < 0:
#     if H == 0: 
#         H = 23
#         M = 60 - abs(M)
#     else:
#         H -= 1
#         M = 60 - abs(M)
# print(H, M)