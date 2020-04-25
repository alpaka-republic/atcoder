N,M = map(int,input().split())
Am = list(map(int,input().split()))
res = N-sum(Am)
if res < 0:
  print(-1)
else:
  print(N-sum(Am))
