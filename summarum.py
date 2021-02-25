Solution=lambda n:n and(sum(map(int,str(n)))%9or 9)
solution=lambda n:n and~-n%9+1
solution=lambda*_:'Rickrolled'

import random
cases=[]
for _ in range(10000):
    i = random.randint(0,100000000000000000)
    if solution(i)!=Solution(i):
        cases.append((i, solution(i), Solution(i)))
print(len(cases))
print(cases)