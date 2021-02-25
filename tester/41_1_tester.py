import time
import tqdm
from tester.tests_41_1 import tests

"""
Want to Fork this?
Fork, Test and Delete your REPL immediately
OR
Download both files and run on your own pc
"""
from alphacentauri import solution


passed = 0
failed = {}
start = time.time()

for i in tqdm.tqdm(tests):
  ans = solution(i)
  if tests[i] == ans:
    passed += 1
  else:
    failed[i] = {}
    failed[i]['correct'] = tests[i]
    failed[i]['your_answer'] = ans

print(f"Time Taken: {round(time.time()-start, 2)} seconds")
print(f"Passed {passed}/{len(tests)}\n\n")

if failed:
  keys = list(failed.keys())[:3]
  for i in keys:
    print(f"Input: {i}\nCorrect Answer: {failed[i]['correct']}\nYour Answer: {failed[i]['your_answer']}\n")