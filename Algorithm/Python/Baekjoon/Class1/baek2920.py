import sys

number = list(map(int, sys.stdin.readline().split()))
ascend = sorted(number)
descend = list(reversed(ascend))

if number == ascend:
    print("ascending")
elif number == descend:
    print("descending")
else:
    print("mixed")