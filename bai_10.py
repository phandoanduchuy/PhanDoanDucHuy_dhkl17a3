import math

class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Diem({self.x}, {self.y})"


class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a 
        self.b = b  

    def tinh_dien_tich(self):
        return math.pi * self.a * self.b

    def __str__(self):
        return f"Elip(tọa độ: {self.x}, {self.y}, bán trục lớn: {self.a}, bán trục nhỏ: {self.b})"


class DuongTron(Elip):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r) 
        self.r = r

    def __str__(self):
        return f"DuongTron(tọa độ: {self.x}, {self.y}, bán kính: {self.r})"

x = float(input("Nhập tọa độ x của điểm: "))
y = float(input("Nhập tọa độ y của điểm: "))
a = float(input("Nhập bán trục lớn (a) của elip: "))
b = float(input("Nhập bán trục nhỏ (b) của elip: "))

elip = Elip(x, y, a, b)
print(elip)
print(f"Diện tích của elip: {elip.tinh_dien_tich()}")

r = float(input("Nhập bán kính (r) của đường tròn: "))
duong_tron = DuongTron(x, y, r)
print(duong_tron)
print(f"Diện tích của đường tròn: {math.pi * r * r}")
