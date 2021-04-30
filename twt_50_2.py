def solution(a:int, b:str, c:int):
  if b == '+':
    v = a + b
  elif b == '-':
    v = a - b
  elif b == '*':
    v = a * b
  elif b == '/':
    v = a // b if c else 0
  else:
    raise Exception('it wasn\'t agreed')
  return v

solution=lambda a,c,b:[a*b,a+b,0,a-b,0,b and a//b][ord(c)%6]