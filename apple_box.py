import timeit
import random

solution1=lambda a:a*(a+1)//(2,-2)[a&1]
print(timeit.repeat(lambda: solution1(random.randint(0,1E31))))
solution9=lambda a:(a,-a)[a&1]*(a+1)//2
print(timeit.repeat(lambda: solution9(random.randint(0,1E31))))
solution8=lambda a:(a,-a)[a&1]*(a+1)>>1
print(timeit.repeat(lambda: solution8(random.randint(0,1E31))))

#solution2=lambda a:-a*(a+1)//(a%2*4-2)
#print(timeit.repeat(lambda: solution2(random.randint(0,1E31))))
#solution3=lambda a:(-1)**a*(a*a+a)//2
#print(timeit.repeat(lambda: solution3(random.randint(0,1E31))))
# solution=lambda a:-a*(a+1)*(a%2-.5)
# print(timeit.repeat(lambda: solution(random.randint(0,1E31))))
