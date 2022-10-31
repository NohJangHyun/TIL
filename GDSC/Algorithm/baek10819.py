# 1. 입력 받은 순서대로 계산한 경우: 20 1 15 8 4 10 => 50
# 2. 최대, 최소, 2번째 최대, 2번째 최소로 계산: 20 1 15 4 10 8 => 52
# 3. 양 끝에 중앙 값, 그 사이에 2번 적용 후 계산: 8 20 1 15 4 10 => 62
import sys
from itertools import permutations #반복 가능 객체 중에서 r개를 선택한 순열을 반환하는 함수


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

res = 0 #현재까지 가장 큰 합
for per in permutations(A):
  temp = 0 #현재 시도한 가장 큰 합
  for i in range(N-1) :
    temp += abs(per[i]-per[i+1])
  res = max(res,temp)

print(res)