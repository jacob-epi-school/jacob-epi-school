
def primes_below(n):
    numbers = set(range(n-1, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

  
def test_primes_below(n):
    numbers = set(range(n-1, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

for x in range(1000):
    l=test_primes_below(x)
    l.sort()
    s = primes_below(x)
    s.sort()
    if(l != s):
        print("error at ",x)

    


