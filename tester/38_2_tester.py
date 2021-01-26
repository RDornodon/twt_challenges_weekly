from fibodict import solution
import time
import copy
from tqdm import tqdm
import json

with open("38_2_tests_2.json") as f:
  data = json.load(f)

failed_cases=[]
start=time.time()
last=start
for i in tqdm(data,desc=f"Testing: ", ncols=70):
    args=copy.deepcopy(i)
    res=solution(args[0])
    ans=i[1]
    if res!=ans:
        failed_cases.append(i+[res])
end=time.time()

print(f"""Passed: {len(data)-len(failed_cases)}/{len(data)}
Time: {end-start}
{"Failed_cases:"if failed_cases else ""}""")

for t in failed_cases[:min(3,len(failed_cases))]:
    print(f"""A: {t[0]}
s: {t[1]}
your answer: {t[3]}
Actual answer(Atleast according to my tester. It may just be that your's is correct afterall but who knows?): {t[2]}""")