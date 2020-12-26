#solution=lambda a,b:[E.count(p)%2for E in[sum(b,())]for p in{*E}].count(1)in(0,2)
#solution=lambda a,b:[E:=sum(b,()),[E.count(p)%2for p in{*E}].count(1)in(0,2)][1]
#solution=lambda a,b:[E:=sum(b,())]and[E.count(p)%2for p in{*E}].count(1)in(0,2)
solution=lambda a,b:[sum(b,()).count(p)%2for p in{*sum(b,())}].count(1)in(0,2)

print(solution([(0, 0), (1, 1), (2, 3), (5, 2)], [(0, 1),(0, 2),(0, 3),(1, 2), (2, 3)]))
True
print(solution([(0, 0), (1, 1), (2, 3), (5, 2)], [(0, 1),(0, 2),(0, 3)]))
False
print(solution([(3, 13), (3, 5), (8, 2), (1, 4), (16, 3)], [(1, 0), (2, 0), (3, 0), (2, 3), (1, 2)]))
True
print(solution([(3, 1), (7, 19), (20, 13), (0, 3), (9, 4)], [(1, 0), (3, 1), (2, 3), (2, 1), (4, 3)]))
False
print(solution([(16, 1), (14, 7), (20, 7), (14, 19), (3, 4)], [(2, 0), (1, 3), (3, 0), (4, 3), (1, 2)]))
True
print(solution([(6, 8), (0, 0), (3, 2), (8, 4), (11, 14)], [(2, 4), (4, 0), (1, 2), (1, 0), (0, 2)]))
True
print(solution([(14, 9), (1, 1), (17, 1), (0, 2), (4, 16)], [(1, 4), (3, 4), (3, 1), (0, 3), (4, 2)]))
False