list = list(map(int, input().split()))

sum=0
for l in list:
    sum += l*l
ans = sum%10 
print(ans)