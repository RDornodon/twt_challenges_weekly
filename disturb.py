import random

seats = \
    [[1, 1, 1, 1, 1],
    [-1, 0, -1, -1, 1],
    [1, 1, 1, 1, 1]]

def tester():
  length = random.randint(1,20)
  _2d_list = [[random.choice([1,-1]) for y in range(length)] for x in range(random.randint(1,20))]
  _2d_list[random.randint(0,len(_2d_list)-1)][random.randint(0,len(_2d_list[0])-1)] = 0
  return _2d_list

def whichExitReference(m):
    for r in m:
        if 0 in r:
            rc = r[r.index(0):].count(1)
            lc = r[:r.index(0)].count(1)
            v = lc-rc
    return ['same', 'right', 'left'][v and (1, 2)[v<0]]

#                                                                                                                  #
whichXxit=lambda m,v=[]:([v(r.count(1)-r[r.index(0):].count(1)*2)for r in m if 0 in r],['same','right','left'][v[-1]and(1,2)[v[-1]<0]])[1]


def whichExit(m):[v]=[(r.count(1)-r[r.index(0):].count(1)*2)for r in m if 0 in r];return['same','right','left'][v and(1,2)[v<0]]

for _ in range(10):
    seats = tester()
    print('\n'.join([' '.join([f"{cell:+d}" for cell in row]) for row in seats]))
    print(whichExitReference(seats), whichExit(seats))


badlambda = lambda x, y=[]:(y.append(x),y)[1]
for a in range(10):
        print(badlambda(a))