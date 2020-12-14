# #solution=lambda n:sum(n%i<1for i in range(2,n))==1
#
# def sieve(limit):
#  a=[1]*limit;a[0]=a[1]= 0
#  for (i, isprime) in enumerate(a):
#   if isprime:
#    yield i*i
#    for n in range(i*i, limit, i):a[n] = 0
#
# # s=set(sieve(31622776));solution=lambda n:n in s
# #
# # def solution(n,l=0,s={}):
# #     m=int(n**.5)
# #     if m!=n**.5: return 0
# #     if l < (l:=(q:=len(str(n)))//3+(q%3>0)): s=set(sieve(2**(l*5)))
# #     return m in s
# # s=set(sieve(31622776));solution=lambda n:n in s
# #
# # solution=lambda n:0 if(m:=(n**.5))!=int(m)else sum(n%i<1for i in range(2,int(m)+1))==1
#solution=lambda n:n==4or(m:=n**.5)==int(m)>1and 1-any(n%i<1for i in range(2,int(m**.5)+1))
#solution=lambda n:n==4or n**.5==int(n**.5)>1and 1-any(n%i<1for i in range(2,int(n**.25)+1))
#solution=lambda n:n==4or(n>1)*(n==)*(1-any(n%i<1for i in range(3,int(n**.25)+1,2)))
# #s=set(sieve(31622776));solution=lambda n:n in s
# s=[*sieve(5623)];solution=lambda n:n==4or n%2and(m:=n**.5)==(m:=int(m))>1and 1-any(n//i*i==n for i in s if i<=m)

import json
from tqdm import tqdm

print("Reading testcases file...")
with open("tests.json") as f:
    tests = json.load(f)


# lambda
# unbound=lambda n:n==4or(m:=n**.5)==int(m)>1and 1-any(n%i<1for i in range(2,int(m**.5)+1))
#
#
# def sieve(limit):
#     a = [1] * limit
#     a[0] = a[1] = 0
#     for (i, isprime) in enumerate(a):
#         if isprime:
#             yield i * i
#             for n in range(i * i, limit, i): a[n] = 0
#
# s = sorted(sieve(5623))
#
# def solution(n):
#     if n > 10**15:
#         return unbound(n)
#     if n == 4:
#         return 1
#     if n == 1 or n % 2 < 1 or (m := n ** .5) != int(m):
#         return 0
#     for i in s:
#         if i > m:
#             break
#         if n % i < 1:
#             return 0
#     return 1
n=2**25;l=[1]*(n+1)
for i in range(2,n):
    if l[i]: l[i*i::i]=[0]*int(n//i-(i-1))
solution=lambda i:l[m]if(m:=int(i**.5))*m==i else 0



passed = 0
failed = []

print("Checking cases...")
for case in tqdm(range(len(tests[0]))):
    check = solution(tests[0][case])
    if check == tests[1][case]:
        passed += 1
    else:
        failed.append([tests[0][case], tests[1][case], check])

print(f'passed {passed} cases out of {len(tests[0])}')

if len(failed) > 0:
    print('\n\ntop three failed cases:')
    for i in range(3):
        if i < len(failed):
            print(f'case:{failed[i][0]}\ncorrect answer:{failed[i][1]}\nsolution answer:{failed[i][2]}\n')