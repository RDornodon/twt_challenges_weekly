# pi = g(1,0,1,1,3,3) where
#  g(q,r,t,k,n,l) = if 4*q+r-t<n*t
#   then n : g(10*q,10*(r-n*t),t,k,div(10*(3*q+r))t-10*n,l)
#   else g(q*k,(2*q+r)*l,t*l,k+1,div(q*(7*k+2)+r*l)(t*l),l+2)

def solution(N,D=[]):
  if not D: D+=[(1,0,1,1,3,3)]
  while N>len(D)-2:
    q, r, t, k, n, l=D.pop()
    while (4*q+r-t) >= (n*t):
      q, r, t, k, n, l = (q * k, (2 * q + r) * l, t * l, k + 1, (q * (7 * k + 2) + r * l)//(t * l), l + 2)
    D += [(q, r, t, k, n, l)]
    q, r, t, k, n, l = (10 * q, 10 * (r - n * t), t, k, (10 * (3 * q + r))//t - 10 * n, l)
    D += [(q, r, t, k, n, l)]
  return D[N][4]


if __name__=='__main__':
  import time
  t = time.time()
  solution(25000)
  print(f'{time.time() - t:.4f}')