def fizzBuzz():
    l = []
    n = 1
    while (n <= 1000):
        if(n % 3 == 0 and n % 5 == 0):
            l.append("FizzBuzz")
        elif(n % 3 == 0):
            l.append("Fizz")
        elif(n % 5 == 0):
            l.append("Buzz")
        else:
            l.append(n)
        n = n + 1
    return l
# error 3 should not be shown in example output
def test_fizzBuzz():
    l = []
    n= 1
    while n in range(1, 1000):
        if(n % 3 == 0):
            l.append("Fizz")
        elif(n % 5 == 0):
            l.append("Buzz")
        if(n % 3 == 0 and n % 5 == 0):
            l.append("FizzBuzz")
        else:
            l.append(n)
        n +=1
    return l
print(test_fizzBuzz())
print("Second:")
print(fizzBuzz())
if(test_fizzBuzz() != fizzBuzz()):
    print("eror")