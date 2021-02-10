solution=lambda b,a:[*range(-((~sum(a)+min(a or[0]))//b),(_:=sum(a)//b)+1)]or[_]
solution=lambda b,a:[*range(-((~sum(a)+min(a or[0]))//b),(_:=sum(a)//b)+1)]or[[],[_]][_>0]
solution=lambda b,a:[*range(-((~(_:=sum(a))+min(a or[0]))//b),_//b+1)]
solution=lambda b,a:[*range(-((~sum(a)+min(a or[0]))//b),sum(a)//b+1)]
solution=lambda b,a:a and[*range(-((~sum(a)+min(a))//b),sum(a)//b+1)]
solution=lambda b,a:a and[*range((sum(a)-min(a))//b+1,sum(a)//b+1)]
# solution=lambda _,O:[*range(1+sum(sorted(O)[1:])//_,1+sum(O)//_)]




print(solution(10,[20]))
print(solution(10,[20,20]))
print(solution(10,[40]))
print(solution(10,[20,5]))
print(solution(10,[]))
print(solution(10,[31]))

