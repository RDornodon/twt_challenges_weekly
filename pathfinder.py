solution=lambda q:1^any([sum(a:=[*map(q.count,'news')])>10,a[0]^a[3],a[2]^a[1]])
solution=lambda q:not(q[:-10]or sum(('ne ws'.index(c)-2)**5for c in q))


print(solution([]))
print(solution([*'news']))
print(solution([*'newsnews']))
print(solution([*'newsnewsnews']))
print(solution([*'nnnwww']))
print(solution([*'nnneee']))
print(solution([*'nnnsss']))
print(solution([*'nns']))
print(solution([*'nws']))
