def Solution(s, v):
    Z = [*zip(range(len(s)), s, v)]
    T = [0]
    C = 0
    for x, s, v in Z:
        for X, S, V in Z:
            if x <= X: continue
            if v == V:
                if s == S: C += 1
            elif (t := (S - s) / (v - V)) >= 0:
                T.append(t)
    m = max(T.count(t) for t in {*T})
    return m + C


solution=lambda s,v:(Z:=[*zip(range(len(s)),*zip(*{*zip(s,v)}))])and(Q:=[(S-s)/(v-V)if(v-V)else-1for x,s,v in Z for X,S,V in Z if x>X])and max(Q.count(q)for q in{*Q}if 0<=q)+len(s)-len(Z)
L,W,solution=len,zip,lambda s,v:(k:=((Z:=[*W(range(L(s)),*W(*{*W(s,v)}))])and(Q:=[(S-s)/(v-V)if(v-V)else-1for x,s,v in Z for X,S,V in Z if x>X]+[0])and max([Q.count(q)for q in{*Q}if 0<=q])+L(s)-L(Z)))*[-1,1][k>1]
L,W,solution=len,zip,lambda s,v:[k:=((Z:=[*W(range(L(s)),*W(*{*W(s,v)}))])and(Q:=[(S-s)/(v-V)if(v-V)else-1for x,s,v in Z for X,S,V in Z if x>X]+[0])and max([Q.count(q)for q in{*Q}if 0<=q])+L(s)-L(Z)),-k][k<2]

solution=lambda s,v:(Z:=[*zip(range(len(s)),s,v)])and(Q:=[(S-s)/(v-V)if(v-V)else-1for x,s,v in Z for X,S,V in Z if x>X]+[0])
def solution(s,v):
    Z=[*zip(range(len(s)),s,v)]
    Q=[(S-s)/(v-V)if(v-V)else-1for x,s,v in Z for X,S,V in Z if x>X]
    R=max([Q.count(q)for q in{*Q}if q>0]or[0])
    return [-1,int(.5+(1+8*R)**.5/2)][R>0]
solution=lambda s,v:(Z:=[*zip(range(len(s)),s,v)])and(Q:=[(S-s)/(v-V)if(v-V)else-1for x,s,v in Z for X,S,V in Z if x>X])and-int(-(8*max([Q.count(q)for q in{*Q}if q>0]+[0]))**.5//2)or-1

def solution(s,v):
    Z=[*zip(range(len(s)),s,v)]
    Q=[(S-s)/(v-V)if(v-V)else-1for x,s,v in Z for X,S,V in Z if x>X]
    R=max([Q.count(q)for q in{*Q}if q>0]or[0])
    return [-1,int(.5+(1+8*R)**.5/2)][R>0]
solution=lambda s,v:(Z:=[*zip(range(len(s)),s,v)])and(Q:=[(S-s)/(v-V)if(v-V)else-1for x,s,v in Z for X,S,V in Z if x>X])and[R:=int(.5+(1+8*max([Q.count(q)for q in{*Q}if q>0]or[0]))**.5/2),-R][R<2]
solution=lambda s,v:(Z:=[*zip(range(len(s)),s,v)])and(Q:=[(t:=(S-s)/(v-V),s+t*v)for x,s,v in Z for X,S,V in Z if x>X and v-V]+[(0,0)])and[R:=int(.5+(1+8*max([Q.count(q)for q in{*Q}if q[0]>0]or[0]))**.5/2),-R][R<2]

x = 0
s = "\|/-"
def szejpojgo(n):
    global x, s
    x = (x + 1) % 4
    print(f'\r{n:4d}{s[x]}', end='')


if __name__=='__main__':
    print(solution([1,2,3,4],[1,2,3,4]))

    print(solution([1,2,11,12],[2,1,2,1]))

    print(solution([87, 67, 18, 83, 25, 78, 74, 72, 66], [9, 11, 13, 13, 6, 0, 18, 6, 10]))

    create_tester = 1
    if create_tester:
        # create random cases
        import random
        import json
        cases = []
        while len(cases)<1000:
            meetings = [-1,5,4,3,2,2,2,2,2,2][len(cases)%10]
            counts = random.randint(max(meetings,2),max(meetings**2,10))
            starts = [*range(100)]
            speeds = [starts.pop(random.randint(0,len(starts)-1))for s in range(counts)]
            velocities = [random.randint(0,20)for v in range(counts)]
            sol = solution(speeds,velocities)
            if sol == meetings == -1 or 1 < meetings <= sol:
                cases.append([speeds, velocities, sol])
            szejpojgo(len(cases))
        with open("./tester/40_2_tests_random_1k.json", "w") as of:
            json.dump(cases, of)

