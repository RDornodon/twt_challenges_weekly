
from tqdm import tqdm
from time import time
import pickle

def solution(a, b):
	return 0

with open("test_cases.pkl", "rb") as f:
	test_cases = pickle.load(f)

failed = []
t = time()

for i in tqdm(test_cases):
	if solution(i[0], i[1]) != i[2]:
		failed.append((i[0], i[1], i[2], solution(i[0], i[1])))
e = time()

print(f"Finished in {int(e - t)} seconds.")
print("\n" + str(len(failed)), "failed cases.\n")
for i in range(3):
	try:
		print(f"Case {i + 1}:")
		print(f"Input: {failed[i][0]}, {failed[i][1]}")
		print(f"Correct Output: {failed[i][2]}")
		print(f"Solution Output: {failed[i][3]}")
		print()
	except:
		pass