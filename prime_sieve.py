# Sieve of Eratosthenes

def sieve(limit):
    a = [1] * limit;
    a[0] = a[1] = 0
    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i * i, limit, i):
                a[n] = 0
