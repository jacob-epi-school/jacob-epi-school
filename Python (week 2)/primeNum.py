import math
def test_is_prime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:                
                # print(i,"times",num//i,"is",num)
                return False
                break

        else:
            return True
    else:
        return False
  
  
def is_prime(n, i=2):
    if n <= 1:
        return False
    elif (n % i == 0):
        return False
    elif (i * i > n):
        return True
    return is_prime(n, i + 1)


for x in range(1000):
    if(test_is_prime(x) != is_prime(x)):
        print("error at ",x, test_is_prime(x), is_prime(x))
