solution=lambda a,d:[*map(list,zip(*a[::1-2*(g:=d>'r')]))][::2*g-1]

a = [[1,2],[3,4]]
print(solution(a,'left'))
print(solution(a,'right'))