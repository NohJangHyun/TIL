import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

number = []
for i in range(0, N-1):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            number.append(cards[i] + cards[j] + cards[k])

number = sorted(list(set(number)))
for i in range(len(number)):
    if number[i] >  M:
        print(number[i-1])
        break
    elif i == len(number)-1:
        print(number[-1])
        break