
# def palindrome_primes():
#     prime_list = five_dig_primes()
#     out_list = []
#     for x in prime_list:
#         if(str(x) == reverse_string(str(x))):
#             out_list.append(x)
#     return out_list

# def five_dig_primes():
#     out_list = []
#     num = 10000
#     while(len(str(num)) == 5):
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 if(not(num in out_list)):
#                         out_list.append(num)
#         num = num + 1
#     return out_list

# def reverse_string(str):  
#     str1 = ""   # Declaring empty string to store the reversed string  
#     for i in str:  
#         str1 = i + str1  
#     return str1

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2,num):
#         if(num % i == 0):
#             return False
#     return True


# def is_palindrome(num):
#     i = 0
#     j = len(str(num)) - 1
#     while(i < j):
#         first = str(num)[0]
#         last = str(num)[len(str(num)) - 1]
#         if(first != last):
#             return False
#         i += 1
#         j -= 1
#     return True

# def palindrome_primes(digits):
#     output = []
#     for i in range(10**(digits - 1), 10**digits):
#         if is_prime(i):
#             if is_palindrome(i):
#                 output.append(i)
#     return output

def is_prime(a):
    i=2
    Prime = "True" 
    while i<a:
        if a%i==0: 
            Prime = "False"
        i=i+1
    
    if a==1:
        Prime = "False"

    print (Prime)
is_prime(100)