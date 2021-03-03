def solution(t,I='n+-*0123456789abcdef',p=''):
 c=[];A,P=c.append,c.pop
 try:
  for _ in t:
   if _ in I:
    if(i:=I.index(_))<1:p+=str(P())
    elif i<2:A(P()+P())
    elif i<3:A(-P()+P())
    elif i<4:A(P()*P())
    else: A(i-4)
 except:p='something smells fishy...'
 return p

def solution(t,I='+-*n0123456789abcdef',p=''):
 c=[];A,P=c.append,c.pop
 try:
  for _ in t:
   if _ in I:
    if(i:=I.index(_))<3:f,e=P(),P();A([e+f,e-f,e*f][i])
    elif i<4:p+=str(P())
    else:A(i-4)
 except:p='something smells fishy...'
 return p

import time
from tqdm import tqdm
import json

with open("tester/test_42_1.json") as f:
  data = json.load(f)

failed_cases=[]
start=time.time()
last=start
for i in tqdm(data['cases'],desc=f"Testing: ", ncols=70):
    try:
        ans=solution(i[0])
        if ans!=i[1]:
            failed_cases.append(i+[ans])
    except BaseException as e:
        if "name 'solution' is not defined" in str(e):
            print("\nPlease copy solution in designated area in source code")
            quit()
        else:
            failed_cases.append(i+["Error: "+str(e)])


end=time.time()

print(f"""Passed: {len(data['cases'])-len(failed_cases)}/{len(data['cases'])}
Time: {end-start}
{"Failed_cases:"if failed_cases else ""}""")

for t in failed_cases[:min(3,len(failed_cases))]:
    print(f"""Input: {t[0]}
your answer: {t[2]}
Actual answer(At least according to my tester. It may just be that your's is correct after all but who knows?): {t[1]}""")