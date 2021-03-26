solution=lambda a,b:int(a*4**(4-f'{b:b}'.count('1')))
# solution=lambda a,b:[a:=[a*2,a//2][_>'0']for _ in f'{b:8b}'[::-1]][-1]

print(solution(2,5))
print(solution(5,100))
print(solution(255,255))
print(solution(69420,255))