  
def fizzbuzz(a):
    m=1
    while(m<a):
        m+=1
        if(m%3==0):
            print("Fizz")
        elif(m%5==0):
            print("Buzz")
        elif(m%3==0 and m%5==0):   
             print("FizzBuzz")
        else:
             print(m)    

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

fizzbuzz(100)