# redcoder
s = list(input())

former = s[:(len(s)//2)]
latter = s[(len(s)-len(s)//2):]
latter.reverse()

print(sum([former[i]!=latter[i] for i in range(len(former))]))
