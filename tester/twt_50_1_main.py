'''
Fork, Test and Delete immediately
OR
Download files and test on your own pc
'''
from tqdm import tqdm
import time
from twt_50_1_tests import tests
from twt_50_1 import solution


passed = 0
failed = {}
start = time.time()

for i in tqdm(tests):
  msg, key = i
  ans = solution(msg, key)
  if ans == tests[i]:
    passed += 1
  else:
    failed[i] = {}
    failed[i]['Your Answer'] = ans
    failed[i]['Correct Answer'] = tests[i]

print(f"Time Taken: {round(time.time()-start, 2)} seconds")
print(f"Passed {passed}/{len(tests)}")

if failed:
  keys = [*failed.keys()][:3]
  for i in keys:
    msg, key = i
    print(f"Message: {msg}\nKey: {key}\nYour Answer: {failed[i]['Your Answer']}\nCorrect Answer: {failed[i]['Correct Answer']}")

