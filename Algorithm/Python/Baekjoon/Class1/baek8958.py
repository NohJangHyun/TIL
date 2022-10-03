import sys

T = int(sys.stdin.readline())

for t in range(T):
    quiz = sys.stdin.readline()
    ans, cnt = 0, 1
    for q in quiz:
        if q == "O":
            ans += cnt
            cnt += 1
        else:
            cnt = 1
    print(ans)