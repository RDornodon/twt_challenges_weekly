def solution(s,l=-1):
  while(s[l]<=s[l-1]):l-=1
  return s[:l-1]+s[l]+''.join(sorted(s[l-1]+(s[l+1:]if l<-1else'')))

print(solution('abcd'))
print(solution('abcdcba'))