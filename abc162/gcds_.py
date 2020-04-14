from functools import reduce
import functools
import fractions
 
@functools.lru_cache(maxsize=None)
def gcd(*numbers):
  return reduce(gcd_, numbers)

@functools.lru_cache(maxsize=None)
def gcd_(a, b):
  if (b == 0):
    return a
  return gcd(b, a % b)
 
sum = 0
K = int(input())
 
for i in range(1,K+1):
  for j in range(i,K+1):
    for k in range(j,K+1):
      # print(i,j,k)
      # print(gcd(i,j,k))
      if (i == j) & (j == k):
        sum += gcd(i,j,k)
      elif (i == j) & (j != k):
        sum += gcd(i,j,k)*3
      elif (i != j) & (j == k):
        sum += gcd(i,j,k)*3
      elif (i != j) & (j != k):
        sum += gcd(i,j,k)*6

print(sum)
