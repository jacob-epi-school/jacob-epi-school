import math
class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        perimeter = self.perimeter()
        return math.sqrt((perimeter/2) * ((perimeter/2) - self.a) * ((perimeter/2) - self.b) * ((perimeter/2) - self.c))

    def scale(self, scale_factor):
        return Triangle(scale_factor * self.a, scale_factor * self.b, scale_factor * self.c)

    def is_valid(self):
        if(self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            return True
        else:
            return False
    
    def is_right(self):
        longest = self.c
        if(longest < self.a):
            longest = self.a
        if(longest < self.b):
            longest = self.b

        if(longest == self.c):
            if(longest * longest == (self.a * self.a + self.b * self.b)):
                return True
        if(longest == self.b):
            if(longest * longest == (self.a * self.a + self.c * self.c)):
                return True
        if(longest == self.a):
            if(longest * longest == (self.c * self.c + self.b * self.b)):
                return True
        return False

t = Triangle(12,16,20)

print("Is t valid?: ", t.is_valid())

print("Is t an right triangle?:", t.is_right())

print("t's perimeter: ", t.perimeter())
print("t's area: ", t.area())
print("Scale t by 2 for new traingle")
p = t.scale(2)
print("p's perimeter: ", p.perimeter())
print("p's area: ", p.area())



