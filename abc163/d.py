def partsum(n,k):
  ret1 = n*(n+1)/2
  ret2 = (n-k+1)*(n-k)/2
  return ret1 - ret2
  # ret = sum(range(n-k+1,n+1))
  # return ret

N, K = map(int,input().split())
ret  = 0
for k in range(K, N+2):
  ret += partsum(N,k) - partsum(k-1,k) + 1
print(int(ret)%(10**9+7))
