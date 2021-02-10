def solution(s, v):
    Z = [*zip(range(len(s)), s, v)]
    T = []
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
L,W,solution=len,zip,lambda s,v:(Z:=[*W(range(L(s)),*W(*{*W(s,v)}))])and(Q:=[(S-s)/(v-V)if(v-V)else-1for x,s,v in Z for X,S,V in Z if x>X])and max(Q.count(q)for q in{*Q}if 0<=q)+L(s)-L(Z)



if __name__=='__main__':
    print(solution([1, 4, 2], [27, 18, 24]))
    print(solution([1, 4, 2, 2], [27, 18, 24, 24]))