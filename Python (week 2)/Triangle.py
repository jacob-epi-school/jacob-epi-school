import math
class test_Triangle():
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
        return test_Triangle(scale_factor * self.a, scale_factor * self.b, scale_factor * self.c)

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



class Triangle:
    def __init__(self,a,b,c):
        self.length_a = a
        self.length_b = b
        self.length_c = c
        
    def perimeter(self):
     perimiter = self.length_a + self.length_b + self.length_c
     return print(perimiter)

    def area(self):
         s = (self.length_a + self.length_b + self.length_c) // 2
         area = math.sqrt(s *( s - self.length_a ) * ( s - self.length_b ) * ( s - self.length_c ))
         return print(area)

    def scale(self, scale_factor):
        return Triangle(scale_factor * self.length_a, scale_factor + self.length_b, scale_factor * self.length_c)
 

    def is_valid(self):
        if self.length_a + self.length_b > self.length_c:
            return True
        elif self.length_a + self.length_c > self.length_b:    
            return True
        elif self.length_b + self.length_c > self.length_a: 
            return True
        else:
            return False    

    def is_right(self):
        a = math.pow(self.length_a,2)
        b = math.pow(self.length_b,2)
        c = math.pow(self.length_c,2)
        if max(a, b, c) == (a + b + c - max(a, b, c)):
            return True 
        else:
            return False    
test1 = Triangle(1,3,5)
test2 = test_Triangle(1,3,5)
print(test1.is_valid(), test2.is_valid())

t = test_Triangle(12,16,20)

print("Is t valid?: ", t.is_valid())

print("Is t an right triangle?:", t.is_right())

print("t's perimeter: ", t.perimeter())
print("t's area: ", t.area())
print("Scale t by 2 for new traingle")
p = t.scale(2)
print("p's perimeter: ", p.perimeter())
print("p's area: ", p.area())


t2 = Triangle(12,16,20)

print("Is t2 valid?: ", t2.is_valid())

print("Is t2 an right triangle?:", t2.is_right())

print("t2's perimeter: ", t2.perimeter())
print("t's area: ", t2.area())
print("Scale t2 by 2 for new traingle")
p2 = t2.scale(2)
print("p's perimeter: ", p2.perimeter())
print("p's area: ", p2.area())


