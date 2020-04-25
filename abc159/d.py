from math import factorial

N = int(input())
An = list(map(int, input().split()))

def combination(n,r):
  if n < 2:
    return 0
  else:
    return factorial(n) / factorial(r) / factorial(n-r)

lens = []
ans = 0
for p in range(N):
  lens.append(An.count(p))
for p in range(N):
  ans = 0
  if lens[p] == 0:
    continue
  for k in range(N):
    if k == p:
      ans += combination(lens[k]-1, 2)
    else:
      ans += combination(lens[k], 2)
  print(int(ans))

#  (n-1)!/(n-r-1)!/(r-1)!
# n(n-1)/2
# (n-1)(n-2)/2 = n(n-1)/2 -2/2*(n-1)
# 4 3 / 2 1
# nCr - n + 1
# 10 - 5 + 1 = 6
# 
