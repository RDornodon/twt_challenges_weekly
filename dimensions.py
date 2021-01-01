solution=lambda l,_='[':sum(1if _==c else(_:='')or 0for c in f'{l}')
def solution(l,c=0):
 while f'{l}'[c]=='[':c+=1
 return c

solution=_=lambda l,c=0:c*(f'{l}'[c]<'[')or _(l,c+1)
solution=_=lambda l,c=0:f'{l}'[c]>'Z'and _(l,c+1)+1
l = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

print(solution(l))