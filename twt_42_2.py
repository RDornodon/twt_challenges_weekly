#E={f'{a//5+1}{a%5+1}':chr(97+a+(a>8))for a in range(25)}
D={chr(_+97):f'{(l:=_-(_>8))//5+1}{l%5+1}'for _ in range(26)}
E={v:k for k,v in reversed(D.items())}
def solution(t,r=''):
 while t:
  a,*t=t
  if a==' ':r+=a
  elif a in D:r+=D[a]
  else:b,*t=t;r+=E[a+b]
 return r


print(solution("hello world"))
print(solution("3534315412244543 434145114215"))
print(solution(" a  b   c    "))
print(solution(solution('11 22  33'))=='11 22  33')