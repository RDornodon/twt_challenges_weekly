#_,h,S,B,solution=int,20,str,lambda n,c='':_(c)if n<1else B(n//h,S(n%10)+c),lambda a,b:B(_(S(a),h)+_(S(b),h))
#t,_=10,lambda a,b,c=0,d=0:c*(a+b<1)or _(a//t,b//t,c+t**d*((a+b)%t),d+1);solution=_


_,I=input,int;print((sum(n:=[*map(I,(_(),_()))])==n[0]*2)*n[0]or abs(n[0]-n[1]))









# _=lambda a,b,c='':_(a//10,b//10,str(a+b)[-1]+c)if a+b else int(c);solution=_
# _=lambda a,b,m=1,r=0:_(a//10,b//10,m*10,r+k%10*m)if(k:=a+b)else r;solution=_
#
#
# def solution(a,b,c=''):
#  while a+b:c,a,b=str(a+b)[-1]+c,a//10,b//10
#  return int(c)
#
# print(solution(123456789,987654321))
# print(solution(1234,5678))
