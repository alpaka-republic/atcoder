N = int(input())
An = list(map(int,input().split()))
ret = [0] * N
for k in range(len(An)):
  ret[An[k] - 1] += 1
for k in range(N):
  print(ret[k])
