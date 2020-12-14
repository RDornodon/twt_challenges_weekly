solution=lambda a:a%2*[28,30]+[31]
solution=lambda x:[28,30,31][3782%x:]
solution=lambda x:[28,30,31][~x%2*2:]


print(solution(28))
print(solution(30))
print(solution(31))

def tester(solution):
    a = {28:[31],30:[31],31:[28,30,31]}
    for x in [28,30,31]:
        if solution(x)!=a[x]:raise Exception(f"Nope, your solution isn't correct (failed with {x})")

import timeit
#print(timeit.timeit(lambda:tester(solution)))


