def is_prime(n):
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
def test_is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:                
                # print(i,"times",num//i,"is",num)
                return False
                break

        else:
            return True
       
    else:
        return False
for x in range(1000):
    if(test_is_prime(x) != is_prime(x)):
        print("error at ",x)
