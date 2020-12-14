_=lambda a,b:a*(a==b)or(a+b)*(min(a,b)<1)or _(a%b,b%a);solution=lambda h,w:(h//(g:=_(h,w))+w//g-1)*g+2*(g-1)
