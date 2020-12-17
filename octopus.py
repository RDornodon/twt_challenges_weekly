from prime_sieve import sieve

# convert list of ints back and forth to 6-bit encoded text
def octopus(int_list):
    temp = '8'.join(oct(n)[2:] for n in int_list)
    if len(temp) % 2:
        temp += '8'
    return ''.join(chr(32+(ord(a)-48)*9+(ord(b)-48))for a,b in zip(temp[::2], temp[1::2]))

deo=D=lambda _:[int(o,8)for o in''.join(f'{(ord(c)-32)//9}{(ord(c)-32)%9}'for c in _).split('8')if o]

s =  [*sieve(320)]
print(s)
o = octopus(s)
print(o)
d = deo(o)
print(d==s)
print(len(octopus(s)), len(' '.join(map(str,s))))