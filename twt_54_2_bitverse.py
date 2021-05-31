
for _ in[0]*int(input()):
 a=int(input())
 while a:_+=_+(a&1);a//=2
 print(_)

for _ in[0]*int(input()):
 a=int(input())
 while a:_+=_+a%2;a//=2
 print(_)

