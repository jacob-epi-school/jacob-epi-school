import math

def solve_quadratic(a,b,c):
    discriminate = b**2 - 4 * a * c
    if discriminate < 0:
        print( "No Solution");
    elif discriminate == 0:
        sol_1 = -b / (2*a)
        print(sol_1)
    else:
        sol_tup = (-b + math.sqrt(discriminate) / (2*a), -b - math.sqrt(discriminate) / (2*a))


solve_quadratic(1,0,1)