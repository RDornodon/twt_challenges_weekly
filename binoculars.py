
P,C,R,solution=lambda n,_=0:[(_:=_*v or v or 1)for v in range(*n)][-1],lambda n,r:P((n,n-r,-1))//P((r+1,)),lambda n:['',f'^{n}'][n>1],lambda a,b,n:['',' + '.join([f'{a}{R(n)}']+[f'{C(n,r)}{a}{R(n-r)}{b}{R(r)}'for r in range(1,n)]+[f'{b}{R(n)}'])][n>0]

# D,R,solution=[[],[1,1]],lambda _,n:_*(n>0)+f'^{n}'*(n>1),lambda a,b,n:' + '.join([f'{r}'*(r>1)+R(a,n-x)+R(b,x)for x,r in enumerate([D.append([*map(sum,zip([0]+D[-1],D[-1]+[0]))])for _ in range(1+n-len(D))]*0 or D[n])])

if __name__=='__main__':
  import time
  t = time.time()
  print(len(solution('a','b',2**14)))
  print(f'{time.time()-t:.3f}')