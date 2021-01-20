import json
import time


# Your solution here
def solution(people: int, list_len: int, pairs_list: list) -> int:
    country_id: int = 0
    people_dict = dict.fromkeys(range(people))

    # country building
    while pairs_list:
        e, o = pairs_list.pop()
        if people_dict[e] and people_dict[o]:
            if people_dict[e] != people_dict[o]:
                pv = people_dict[o]
                for k in people_dict:
                    if people_dict[k] == pv:
                        people_dict[k] = people_dict[e]
        elif people_dict[e]:
            people_dict[o] = people_dict[e]
        elif people_dict[o]:
            people_dict[e] = people_dict[o]
        else:
            country_id += 1
            people_dict[e] = country_id
            people_dict[o] = country_id

    #remaining people country assignems
    for p in people_dict:
        if not people_dict[p]:
            country_id += 1
            people_dict[p] = country_id

    country_list = [*people_dict.values()]
    countries = {c: country_list.count(c) for c in {*country_list}}

    possible_pairs = 0
    while countries:
        v = countries.pop([*countries.keys()][0])
        possible_pairs += v * sum(countries.values())
    return possible_pairs



with open("tester/37_1_tests_1.json", encoding="utf-8") as f:
    data = json.load(f)

failed_cases = []
start = time.time()
for i in data['cases']:
    n_ = i[0]
    p_ = i[1]
    pairs_ = list(map(list,i[2]))
    res = solution(n_, p_, pairs_)
    ans = i[3]
    if res != ans:
        failed_cases.append(i+[res])
end=time.time()

print(f"""Passed: {len(data['cases'])-len(failed_cases)}/{len(data['cases'])}
Time: {end-start}
Failed_cases:""")

for t in [*sorted(failed_cases)][:3]:
    print(f"""n: {t[0]}
p: {t[1]}
pairs: {t[2]}
your answer: {t[4]}
Actual answer(At least according to my tester. It may just be that your's is correct afterall but who knows?): {t[3]}"""
          )

# print(solution(10, 6, [[1, 6], [0, 7], [8, 4], [7, 8], [3, 1], [4, 5]]))

# print(solution(5, 3, [[0, 0], [2, 3], [0, 4]]))
