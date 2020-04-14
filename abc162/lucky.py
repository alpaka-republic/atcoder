n = int(input())
n1 = n%10
n2 = (n//10)%10
n3 = (n//100)%10

if (n1==7) | (n2==7) | (n3==7):
  print('Yes')
else:
  print('No')
