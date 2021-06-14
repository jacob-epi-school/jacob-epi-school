
def palindrome_primes():
    prime_list = five_dig_primes()
    out_list = []
    for x in prime_list:
        if(str(x) == reverse_string(str(x))):
            out_list.append(x)
    return out_list

def five_dig_primes():
    out_list = []
    num = 100
    while(len(str(num)) == 3):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                if(not(num in out_list)):
                        out_list.append(num)
        num = num + 1
    return out_list

def reverse_string(str):  
    str1 = ""   # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1

print(palindrome_primes())