# thanks for not letting us use 'just any' itertools functions :/
Q,P,F,solution=lambda i,v:i[1]-i[0]==v[1]-v[0],lambda a,b,c,d:[(A,B,C,D)for A in a for C in c for B in b for D in d],lambda A,B,D:[(i,j)for i in range(len(A))if A[i]in{*A}&{*B}for j in range(i+2,len(A))if A[j]in{*A}&{*D}],lambda s:sum(len([*filter(lambda v:Q(*v[::2])and Q(*v[1::2])and A[v[0][0]]==B[v[1][0]]and A[v[0][1]]==D[v[3][0]]and B[v[1][1]]==C[v[2][0]]and C[v[2][1]]==D[v[3][1]],P(F(A,B,D),F(B,A,C),F(C,B,D),F(D,A,C)))])for A,B,C,D in __import__('itertools').permutations(s))
#solution=lambda s:sum(len([*filter(lambda v:v[0][1]-v[0][0]==v[2][1]-v[2][0]and v[1][1]-v[1][0]==v[3][1]-v[3][0]and A[v[0][0]]==B[v[1][0]]and A[v[0][1]]==D[v[3][0]]and B[v[1][1]]==C[v[2][0]]and C[v[2][1]]==D[v[3][1]],P(F(A,B,D),F(B,A,C),F(C,B,D),F(D,A,C)))])for A,B,C,D in _(s))

def Solution(s):
    sol = 0
    for A,B,C,D in __import__('itertools').permutations(s):
        p = P(F(A,B,D),F(B,A,C),F(C,B,D),F(D,A,C))
        g = [*filter(lambda v:v[0][1]-v[0][0]==v[2][1]-v[2][0]and v[1][1]-v[1][0]==v[3][1]-v[3][0]and A[v[0][0]]==B[v[1][0]]and A[v[0][1]]==D[v[3][0]]and B[v[1][1]]==C[v[2][0]]and C[v[2][1]]==D[v[3][1]],p)]
        [print() or print_xwords((A,B,C,D), v) for v in g]
        sol += len(g)
    return sol

F=lambda A,B,D:[(i,j)for i in range(len(A))if A[i]in{*A}&{*B}for j in range(i+2,len(A))if A[j]in{*A}&{*D}]

o,solution=enumerate,lambda W,n=0:[[[[b:=[i for i,c in o(w[1])if c==w[0][s]],[[y:=[i for i,c in o(w[2])if c==w[0][d]],[n:=n+((j,k)==(l,z))for g in b for h in y for j,k in zip(w[1][g+2:],w[2][h+2:])for l,z in zip(w[3],w[3][d-s:])]]for d in range(s+2,len(w[0]))]]for s in range(len(w[0])-2)]for w in __import__('itertools').permutations(W)],n][1]

def print_xwords(z,x):
    a,b,c,d = z
    k,l,m,n = x
    left_k = max(k[0], m[0])-k[0]
    left_m = max(k[0], m[0])-m[0]
    top_l = max(l[0], n[0])-l[0]
    top_n = max(l[0], n[0])-n[0]
    box_x = k[1] - k[0] - 1
    box_l = left_k + k[0]
    line = 0
    while True:
        if line==top_l+l[0]:
            print('  '*left_k+' '+' '.join(a))
        elif line==top_l+l[1]:
            print('  '*left_m+' '+' '.join(c))
        else:
            print('  '*box_l,end='',sep='')
            if line-top_l>=0 and line<top_l+len(b):
                print(' '+b[line-top_l],end='',sep='')
            else:
                print('  ',end='',sep='')
            print('  ' * box_x,end='',sep='')
            if line-top_n>=0 and line<top_n+len(d):
                print(' '+d[line - top_n],end='',sep='')
            print()
        line += 1
        if line > max(len(d)+top_n,len(b)+top_l):
            break

TESTS = (
    (["crossword", "square", "formation", "something"], 6),

    (["anaesthetist", "thatch", "ethnics", "sabulous"],0),

    (["eternal", "texas", "chainsaw", "massacre"],4),

    (["africa", "america", "australia", "antarctica"],62),

    (["phenomenon", "remuneration", "particularly", "pronunciation"],62),

    (["onomatopoeia", "philosophical", "provocatively", "thesaurus"],20))

for test, result in TESTS:
     print(S:=solution(test),S==result,result)
print_xwords(('eternal', 'texas', 'chainsaw', 'massacre'),((1, 5), (0, 3), (2, 6), (1, 4)))
