def fizzBuzz():
    n = 1
    while (n <= 1000):
        if(n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz")
        elif(n % 3 == 0):
            print("Fizz")
        elif(n % 5 == 0):
            print("Buzz")
        else:
            print(n)
        n = n + 1
fizzBuzz()
# error 3 should not be shown in example output