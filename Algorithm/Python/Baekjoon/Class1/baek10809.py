S = input()

alphabets = []
for i in range(97, 123):
    alphabets.append(chr(i))

for alphabet in alphabets:
    print(S.find(alphabet), end= " ")