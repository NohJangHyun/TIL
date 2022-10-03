import sys

word = sys.stdin.readline().upper()
W = list(set(word.strip()))

cnt = []
for w in W:
    cnt.append(word.count(w))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(W[cnt.index(max(cnt))])