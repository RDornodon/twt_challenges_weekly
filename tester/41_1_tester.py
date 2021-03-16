import json,time
from tqdm import tqdm
from binoculars import solution
#Your Solution here

#Your Solution here

test_file = "41_1_tests_c1.json"

with open(test_file,"r") as f:
    cases = json.load(f)["cases"]

n=len(cases)
passed=0
failed_cases=[]
start=time.time()
for test in tqdm(cases,desc="Testing: "):
    try:
        user_ans=solution(*test[:3])
        if user_ans == test[3]:
            passed+=1
        else:
            failed_cases.append(test+[user_ans])
    except Exception as e:
        if "name 'solution' is not defined" in str(e):
            print("\nPlease copy/paste your solution in the designated loaction in the code.")
            quit()
        else:
            failed_cases.append(test+["Error: "+str(e)])
end=time.time()

print(f"""Passed : {passed}/{n}
time : {end - start}""")

if failed_cases:
    print("Some failed cases")
    for test in failed_cases[:5]:

        print(f"""Arg1: {test[0]}
Arg2: {test[1]}
Arg3: {test[2]}
Solution(According to my tester): {test[3]}""")
        if str(test[4]).startswith("Error"):
            print(test[4])
        else:
            print(f"Your solution: {test[4]}")