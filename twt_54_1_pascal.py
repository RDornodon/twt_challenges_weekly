
#for i in range(int(input())):A=[1];B=[*range(1,int(input()))];[A.append(A[-1]*b//c)for b,c in zip(B[::-1],B)];print(' '.join(map(str,A)))

#for A in'.'*int(input()):A=[1];B=[*range(1,int(input()))];[A.append(A[-1]*b//c)for b,c in zip(B[::-1],B)];print(' '.join(map(str,A)))
#for _ in'.'*int(input()):A=[1];B=int(input());[A.append(A[-1]*b//(B-b+1))for b in range(B,0,-1)];print(' '.join(map(str,A)))


def testing():
  import time
  import contextlib
  from tqdm import tqdm

  t = time.time()
  for _ in tqdm(range(19900,20001), desc=f"Testing: ", ncols=50):
    with contextlib.redirect_stdout(None):
      B=_-1;print(A:=1,*[A:=A*(B-b)//-~b for b in range(B)])
  t2 = time.time()
  print(f'Elapsed time: {t2-t:.3f} secs.')

if __name__=='__main__':
  testing()
  for _ in'.'*int(input()):A=[1];B=int(input())-1;[A.append(A[-1]*(B-b)//-~b)for b in range(B)];print(' '.join(map(str,A)))
  for _ in'.'*int(input()):B=int(input())-1;print(A:=1,*[A:=A*(B-b)//-~b for b in range(B)])
  # for _ in'.'*int(input()):
  #  A=[1];B=int(input())-1
  #  for b in range(B):A+=[A[-1]*(B-b)//-~b]
  #  print(*A)

for _ in'.'*int(input()):B=int(input())-1;print(A:=1,*[A:=A*(B-b)//-~b for b in range(B)])
