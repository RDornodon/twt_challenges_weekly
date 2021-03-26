def solution(s):
  B,W,E=zip(*[(w[0],w[1:-1],w[-1])for w in s.split()])
  if len(B)<2:return s
  elif len(B)%2:B,E=[*B[1:]]+[B[0]],[E[-1]]+[*E[:-1]]
  else:B,E=[B[-1]]+[*B[:-1]],[*E[1:]]+[E[0]]
  return ' '.join(b+w+e for b,w,e in zip(B,W,E))

print(solution('Hello World'))
print(solution("Tech with Tim"))
print(solution("Hi 001 Bye ELLO"))

