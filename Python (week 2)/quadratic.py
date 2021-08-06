import math

def test_solve_quadratic(a,b,c):
    discriminate = b**2 - 4 * a * c
    if discriminate < 0:
        print( "No Solution")
    elif discriminate == 0:
        sol_1 = -b / (2*a)
        print(sol_1)
    else:
        sol_tup = (-b + math.sqrt(discriminate) / (2*a), -b - math.sqrt(discriminate) / (2*a))


import cmath 
a = int (input ('enter a: '))
b = int (input ('enter b: '))
c = int (input ('enter c: '))
def solve_quadratic(a,b,c):
    d = (b**2)-(4*a*c)
    if d < 0:
        return None
    if d == 0:
        solution1 = (-b + cmath.sqrt (d))/(2*a)
        return solution1 
    if d > 0:
        solution1 = (-b + cmath.sqrt (d))/(2*a) 
        solution2 = (-b - cmath.sqrt(d))/(2*a) 
        return (solution1, solution2)
print (solve_quadratic(a,b,c))

