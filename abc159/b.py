s = list(input())
n = len(s)

def kaibun(st):
  sta = list()
  for k in range(len(st)//2):
    sta.append(st[k])
  for k in range(len(st)//2):
    if st[-(-len(st)//2)+k] != sta.pop():
      return False
  return True

if kaibun(s) == False:
  print('No')
elif kaibun(s[:(n-1)//2]) == False:
  print('No')
elif kaibun(s[(n+3)//2-1:]) == False:
  print('No')
else:
  print('Yes')
