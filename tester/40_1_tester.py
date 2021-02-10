import json
from candy_bendy import solution

with open("40_1_tests.json") as jsonfile:
    tests = json.load(jsonfile)

'''
Fork, Test and Delete your REPL immediately
OR
Download both files and run on your own pc
'''

passes = 0
failures = 0

for test in tests:
    answer = solution(test["price_per"], test["bills"])
    if test["answer"] != answer:
        failures += 1
        print("Invalid entry")
        print(f"solution({test['price_per']}, {test['bills']})")
        print("returned:")
        print(answer)
        print("instead of")
        print(test["answer"])
        print("-----------------------------------")
    else:
        passes += 1

print(f"Passes: {passes}/{len(tests)}")
print(f"Failures: {failures}/{len(tests)}")