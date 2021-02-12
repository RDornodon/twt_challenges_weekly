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
solution=lambda s,v:(Z:=[*zip(range(len(s)),s,v)])and(Q:=[(S-s)/(v-V)if(v-V)else-1for x,s,v in Z for X,S,V in Z if x>X])and[-1,int(.5+(1+8*(R:=max([Q.count(q)for q in{*Q}if q>0]or[0])))**.5/2)][R>0]
solution=lambda s,v:(Z:=[*zip(range(len(s)),s,v)])and(Q:=[(S-s)/(v-V)if(v-V)else-1for x,s,v in Z for X,S,V in Z if x>X])and-int(-(8*max([Q.count(q)for q in{*Q}if q>0]+[0]))**.5//2)or-1

x = 0
s = "\|/-"
def szejpojgo():
    global x, s
    x = (x + 1) % 4
    print(f'\b{s[x]}', end='')


if __name__=='__main__':
    print(solution([], []))
    print(solution([1], [1]))
    print(solution([1, 2, 3, 4, 5], [1, 1, 1, 1, 1]))
    print(solution([1, 2, 3, 4, 5], [1, 1, 1, 1, 0]))
    print(solution([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
    print(solution([1, 2, 3, 4, 5], [5, 4, 3, 2, 0]))
    print(solution([1, 4, 2], [27, 18, 24]))

    # create random cases
    import random
    import json
    cases = []
    while len(cases)<1000:
        meetings = [-1,6,5,4,3,2,2,2,2,2][len(cases)%10]
        counts = random.randint(max(meetings,2),max(meetings*(meetings-1),10))
        starts = [*range(100)]
        speeds = [starts.pop(random.randint(0,len(starts)-1))for s in range(counts)]
        velocities = [random.randint(0,20)for v in range(counts)]
        sol = solution(speeds, velocities)
        if sol == meetings == -1 or 1 < meetings <= sol:
            cases.append([speeds, velocities, sol])
            if len(cases)%50 == 0: print('\b* ', end='')
        szejpojgo()
    with open("./tester/40_2_tests_random_1k.json", "w") as of:
        json.dump(cases, of)

