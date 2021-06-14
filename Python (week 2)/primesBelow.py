def primes_below(n):
    
    out_list = []
    if(n > 2):
        out_list.append(2)
    for num in range(1, n):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i == 0):
                    break
                else:
                    if(not(num in out_list)):
                        out_list.append(num)
    return out_list

print(primes_below(17))

