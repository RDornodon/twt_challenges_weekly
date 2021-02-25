# S,B,solution=sum,lambda n:bin([n,256+n][n<0])[2:],lambda e:(q:=[*map(B,l:=(v:=[*map(int,e.split(r:=[' - ',' + ']['+'in e]))])+[S(v)])])and((S(v),f'{q[0]}{r}{q[1]} = {q[2]}')if-129<min(l)<=max(l)<128else'Invalid')

B,solution=lambda n:bin(256*(n<0)+n)[2:],lambda e:(l:=(v:=[*map(int,e.split(r:=f' {"-+"["+"in e]} '))])+[sum(v)])and((l[2],f'{B(l[0])}{r}{B(l[1])} = {B(l[2])}')if-129<min(l)<=max(l)<128else'Invalid')
solution=lambda e:(l:=(v:=[*map(int,e.split(r:=f' {"-+"["+"in e]} '))])+[sum(v)])and((l[2],f'{B(l[0])}{r}{B(l[1])} = {B(l[2])}')if-129<min(l)<=max(l)<128else'Invalid')

def solution(e):r="+"in e;a,b=map(int,e.split(f' {"-+"[r]} '));c=a+[-b,b][r];return['Invalid',(c,f'%s {"-+"[r]} %s = %s'%(*map(lambda n:bin(256*(n<0)+n)[2:],(a,b,c)),))][-129<c<128]

def solution(e):a,o,b=e.split();a,m,b=map(int,(a,o+'1',b));r=lambda x:f"{x%256:b}";return(z:=a+b*m,r(a)+f" {o} {r(b)} = "+r(z))*(-129<z<128)or"Invalid"


if __name__ == '__main__':

    print(solution("2 + 5") == (7, '10 + 101 = 111'))

    print(solution("0 + -1") == (-1, '0 + 11111111 = 11111111'))

    print(solution("100 + 100") == "Invalid" )

    print(solution("100 - 100"))#== "Invalid" )