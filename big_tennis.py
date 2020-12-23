#solution=lambda *_:sorted(_)in([0,6],[1,6],[2,6],[3,6],[4,6],[5,7],[6,7])
solution=lambda *_:(*sorted(_),)in zip(range(7),[6]*5+[7,7])
#def solution(*_):a,b=sorted(_);return(7==b>a>4)|(a<b-1==5)
#def solution(*_):a,b=sorted(_);return 7==b>a>4or a<b-1==5
#solution=lambda *_:[a<b-1<6==b or 7==b>a>4for a,b in[sorted(_)]][0]

print(solution(1,2))
print(solution(2,4))
print(solution(6,2))
print(solution(6,7))
print(solution(7,2))
print(solution(7,7))
print(solution(11,2))