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
Solution=lambda s,v:(Z:=[*zip(range(len(s)),s,v)])and(Q:=[(t:=(S-s)/(v-V),s+t*v)for x,s,v in Z for X,S,V in Z if x>X and v-V]+[(0,0)])and[(q,Q.count(q))for q in{*Q}if q[0]>0 and Q.count(q)>1]

x = 0
s = "\|/-"
def szejpojgo(n):
    global x, s
    x = (x + 1) % 4
    print(f'\r{n:4d}{s[x]}', end='')


if __name__=='__main__':
    # print(solution([1,2,3,4],[1,2,3,4]))

    # print(solution([1,2,11,12],[2,1,2,1]))

    # print(solution([87, 67, 18, 83, 25, 78, 74, 72, 66], [9, 11, 13, 13, 6, 0, 18, 6, 10]))

    for _ in sorted(Solution([-1046, -1683, -7375, 7255, -9096, 8740, 9135, 5866, -5127, 9378, 2293, -7689, -4293, 1196, -8415, 5211, -713, 12, 8787, 9849, 2807, -5499, 4871, -6941, 6340, -9882, 3417, 7895, -8827, 5363, 8032, 747, -1127, 4211, 1505, -1381, -7359, -2750, -6324, 9371, 5181, 7490, -1678, 3301, -32, -1274, 1297, 8256, -2934, -7581, -9181, -4261, -2866, 507, -3594, -494, 1198, 4961, 4295, -6184, -3699, 6847, 8981, -2866, -4319, -9759, 8357, -9371, 3832, 1092], [25, 59, 89, 32, 61, 91, 91, 68, 84, 23, 1, 67, 12, 87, 67, 77, 48, 44, 61, 33, 88, 73, 29, 6, 46, 99, 20, 12, 94, 41, 81, 84, 29, 97, 99, 54, 71, 8, 18, 65, 71, 54, 9, 17, 73, 100, 65, 54, 3, 78, 50, 21, 69, 58, 82, 94, 100, 3, 96, 28, 53, 81, 21, 69, 84, 20, 93, 8, 39, 82])):
        print(_)
    create_tester = 0
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

