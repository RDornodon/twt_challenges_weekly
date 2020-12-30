solution=lambda l,_='[':sum(1if _==c else(_:='')or 0for c in f'{l}')
def solution(l,c=0):
 while f'{l}'[c]=='[':c+=1
 return c

l = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

print(solution(l))