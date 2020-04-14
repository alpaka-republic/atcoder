from functools import reduce
import fractions
 
def gcd(*numbers):
	return reduce(fractions.gcd, numbers)
 
sum = 0
K = int(input())
 

for j in range(1,K+1):
  for k in range(j,K+1):
    for i in range(1,K+1):
      sum += gcd(i,j,k)

print(sum)
