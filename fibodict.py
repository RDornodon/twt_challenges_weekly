Solution=lambda n,a=0,b=1:([a:=b+(b:=a)for _ in range(n)],b)[1]
F={1:0,2:1};solution=lambda n:([F.update({_:F[_-1]+F[_-2]})for _ in range(max(F.keys())+1,n+1)],F[n])[1]
solution=lambda n,a=0,b=1:([a:=b+(b:=a)for _ in range(n)],b)[1]
def solution(n,a=0,b=1):
 while n:=n-1:a,b=b+a,a
 return a


if __name__ == '__main__':
  import time
  import json
  t = time.time()
  res = []
  for _ in range(2000):
    res.append([v:=_+1, solution(v)])
  t = time.time()-t
  print(f'Time elapsed: {t:.2f}')
  with open('tester/38_2_tests_2k.json', 'w') as file_out:
    json.dump(res, file_out)
