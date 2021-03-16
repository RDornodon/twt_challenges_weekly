def Solution(l,c=0):
  L=sorted(l)
  while l:c+=L.index(v:=l.pop(0));L.remove(v)
  return c

solution=lambda l:(L:=sorted(l)or 1)and sum([L.index(_),L.remove(_)][0]for _ in l)
solution=lambda l:[L:=sorted(l),sum([L.index(_),L.remove(_)][0]for _ in l)][1]


if __name__=='__main__':
  print(solution([0,2,2,0,0,3,1,44,2,1,44,4]))

  create_tester = 0
  if create_tester:
    # create random cases
    import random
    import json

    cases = []
    for _ in range(1000):
      counts = random.randint(0, 1000)
      elements = [random.randint(-100000,100000) for s in range(counts)]
      sol = solution(elements)
      cases.append([elements, sol])
    with open("./tester/41_2_tests_1k.json", "w") as of:
      json.dump(cases, of)
