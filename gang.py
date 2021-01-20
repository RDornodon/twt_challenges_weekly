solution=lambda l,n:len({sum(2**b for b,d in enumerate({*l})if n%d<1)for n in range(1,n+1)})
solution=lambda l,n:len({sum(2**b for b,d in enumerate({*l})if n%d)for n in range(1,n+1)})
solution=lambda l,n:len({sum(2**b for b,d in enumerate({*l})if(n+1)%d)for n in range(n)})
solution=lambda l,n:len({sum(2**b for b,d in enumerate({*l})if~n%d)for n in range(n)})
# solution=lambda l,n:(G:=[*enumerate({*l})])and len({sum(2**b*(~n%d>0)for b,d in G)for n in range(n)})


import json
from tqdm import tqdm
import time

with open("tester/35_1_tests.json", "r") as f:
  cases = json.load(f)

failed = []

t = time.time()

for i in tqdm(cases):
  y = solution(*i[0])
  if i[1] != y:
    failed.append((i[0], i[1], y))

e = time.time()

print(f"\nFinished in {e - t} seconds!")
print(f"\n{len(failed)} failed cases!\n")

try:
  for e, i in enumerate(failed[:5]):
    print(f"Case {e}")
    print(f"Input: {i[0]}")
    print(f"Expected Output: {i[1]}")
    print(f"Solution Output: {i[2]}")
    print()
except:
  pass
