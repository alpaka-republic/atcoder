import numpy as np

A = [0] * 3
A[0] = list(map(int,input().split()))
A[1] = list(map(int,input().split()))
A[2] = list(map(int,input().split()))
N = int(input())
bn = []
for n in range(N):
  bn.append(int(input()))
for i in range(3):
  for j in range(3):
    A[i][j] = A[i][j] in bn
A = np.array(A)
if sum(np.prod(A,1)) != 0:
  print('Yes')
elif sum(np.prod(A,0)) != 0:
  print('Yes')
elif A[0][0] * A[1][1] * A[2][2] != 0:
  print('Yes')
elif A[2][0] * A[1][1] * A[0][2] != 0:
  print('Yes')
else:
  print('No')
