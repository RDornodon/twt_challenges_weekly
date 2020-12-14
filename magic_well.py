solution=lambda a,b,n:sum(map(lambda x,y:x*y,range(a,a+n),range(b,b+n)))
Solution=lambda a,b,n:sum(x*y for x,y in zip(range(a,a+n),range(b,b+n)))

solution=lambda a,b,n:sum((a+c)*(b+c)for c in range(n))

solution=lambda a,b,n:n*a*b+a*(g:=n*(n-1))//2+g*b//2+g*(2*n-1)//6
solution=lambda a,b,n:n*a*b+(a+b)*(g:=n*n-n)//2+g*(2*n-1)//6

solution=lambda a,b,n:n*(a*b*6+(n-1)*((a+b)*3+(2*n-1)))//6




print(s:=solution(1,2,3),S:=Solution(1,2,3),s==S)

print(s:=solution(1234,23456,34567890),S:=Solution(1234,23456,34567890),s==S)
