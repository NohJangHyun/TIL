import sys

N = int(sys.stdin.readline())
grade = list(map(int, sys.stdin.readline().split()))

M = max(grade)

for g in range(len(grade)):
    grade[g] = grade[g]/M*100

print(sum(grade)/N)
        