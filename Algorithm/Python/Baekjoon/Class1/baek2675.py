import sys
T = int(sys.stdin.readline())

for t in range(T):
    R, S = sys.stdin.readline().split()
    w=""
    for s in S:
        w += s*int(R)
    print(w)