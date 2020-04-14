n = int(input())

sum3 = 3*0.5*(n//3)*(n//3+1)
sum5 = 5*0.5*(n//5)*(n//5+1)
sum15 = 15*0.5*(n//15)*(n//15+1)
sums = 0.5*n*(n+1)
print(int(sums - sum3 - sum5 + sum15))
