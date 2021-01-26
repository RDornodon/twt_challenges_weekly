import copy,json,time
from tqdm import tqdm

#Your Solution here
R,L=range,len;solution=lambda a,b:b in[[a[Y+y][x:x+L(b[0])]for Y in R(L(b))]for x in R(L(a[0])-L(b[0])+1)for y in R(len(a)-L(b)+1)]
#Your Solution here

with open("tester/37_2_tests.json") as f:
    data=json.load(f)

failed_cases=[]
start=time.time()
for i in tqdm(data['cases'],desc="Testing", ncols=100):
    args=copy.deepcopy(i[:2])
    res=solution(*args)
    ans=i[2]
    if res!=ans:
        failed_cases.append(i+[res])
end=time.time()

print(f"""Passed: {len(data['cases'])-len(failed_cases)}/{len(data['cases'])}
Time: {end-start}
Failed_cases(top 3):""")

for t in failed_cases[:3]:
    print(f"""A: {t[0]}
B: {t[1]}
your answer: {t[3]}
Actual answer(Atleast according to my tester. It may just be that your's is correct afterall but who knows?): {t[2]}""")