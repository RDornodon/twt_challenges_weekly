import random as rand

class testers_list(list):
  def index(self, *_):
    raise Exception("Don't use index!")


def Solution(l, i):
  return (a:=l.index(i)),1-a&1

def solution(l,i,ix=0):
  while(mp:=len(l)//2)and(v:=l[mp])!=i:l,ix=(l[mp:],ix+mp)if(v<i)else(l[:mp],ix)
  return 1-(ix+mp)&1

solution=_=lambda l,i,x=0:_(*(l[m:],i,x+m)if(l[m]<i)else(l[:m],i,x))if(m:=len(l)//2)and l[m]!= i else(x+m,1-(x+m)&1)

S = []
F = []
for X in range(50):
  L = sorted({(G:=rand.randint(0,1000000))for _ in range(100000)})
  L=testers_list(L)
  S.append(Solution(L,G)[1]==solution(L,G)[1])
  if not S[-1]: F.append((Solution(L,G),solution(L,G)))
print(S.count(False))
print(F)