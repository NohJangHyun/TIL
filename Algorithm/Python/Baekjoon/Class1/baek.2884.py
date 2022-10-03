import sys

H, M = map(int, sys.stdin.readline().split())
M -= 45
if M < 0:
    if H == 0: 
        H = 23
        M = 60 - abs(M)
    else:
        H -= 1
        M = 60 - abs(M)
print(H, M)
