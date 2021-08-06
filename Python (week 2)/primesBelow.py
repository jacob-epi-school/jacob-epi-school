
 
import math
def test_primes_below(n):
    t=2
    l=[]
    while (t<n):
        m=0
        for i in l:
            if t%i==0:
                m=m+1
                break
            if (i>math.sqrt(t)):
                break

        if m==0:
            l.append(t)
        
        t=t+1
    return l

def is_prime(n):
    if n > 1:
        for x in range(2, n):
            if n % x == 0:
                return False # not a prime number
        else:
            return True # a prime number
    else:
        return False # not a prime number
def print_prime(n):
    
    primes_list = []
    
    for i in range(2, n):
        if is_prime(i): # if True
            primes_list.append(i)
            
    return primes_list
# l=test_primes_below(634)
# l.sort()
# s = primes_below(634)
# s.sort()
# print(l)
# print(s)
# for x in range(len(l)):
#     if(l[x] != s[x]):
#         print("error: ", l[x], s[x])
for x in range(1000):
    l=test_primes_below(x)
    l.sort()
    s = print_prime(x)
    s.sort()
    if(l != s):
        print("error at ",x)

    


