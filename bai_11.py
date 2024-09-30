import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a  
        self.b = b  
        self.c = c 
    def dien_tich(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def chu_vi(self):
        return self.a + self.b + self.c


class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, a) 

    def dien_tich(self):
        return (self.b / 2) * math.sqrt(self.a**2 - (self.b / 2)**2)


class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, math.sqrt(a**2 + b**2))  
    def dien_tich(self):
        return (self.a * self.b) / 2


class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a)  

    def dien_tich(self):
        return (math.sqrt(3) / 4) * (self.a ** 2)
