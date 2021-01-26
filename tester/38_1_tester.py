import json
import time
import copy
from tqdm import tqdm
from rotavirus import solution


with open("38_1_tests_1.json") as f:
    data=json.load(f)

failed_cases=[]
start=time.time()
last=start
for i in tqdm(data['cases'],desc=f"Testing: ", ncols=100):
    args=copy.deepcopy(i)
    res=solution(*args[:2])
    ans=i[2]
    if res!=ans:
        failed_cases.append(i+[res])
end=time.time()

print(f"""Passed: {len(data['cases'])-len(failed_cases)}/{len(data['cases'])}
Time: {end-start}
{"Failed_cases:"if failed_cases else ""}""")

for t in failed_cases[:min(3,len(failed_cases))]:
    print(f"""A: {t[0]}
s: {t[1]}
your answer: {t[3]}
Actual answer(Atleast according to my tester. It may just be that your's is correct afterall but who knows?): {t[2]}""")