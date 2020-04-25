n = int(input())
s = input()

arr = []
R = len(list(filter(lambda x:x == 'R', s)))
G = len(list(filter(lambda x:x == 'G', s)))
B = len(list(filter(lambda x:x == 'B', s)))
tot = R*G*B

for i in range(n):
  for j in range(i+1, n):
    k = 2*j-i
    if k >= n:
      continue
    if (s[i] != s[j]) and (s[i] != s[k]) and (s[j] != s[k]):
      tot -= 1

print(tot)

