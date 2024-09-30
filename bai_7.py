class Date:
    def __init__(self, day=1, thang=1, nam=1):
        self.day = day
        self.thang = thang
        self.nam = nam

    def display(self):
        print(f"Ngày: {self.day}/{self.thang}/{self.nam}")

    def next(self):
        ngay_thang = [31, 28 + (1 if self.nam_nhuan() else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day += 1
        if self.day > ngay_thang[self.thang - 1]:  
            self.day = 1
            self.thang += 1
            if self.thang > 12:  
                self.thang = 1
                self.nam += 1

    def nam_nhuan(self):
        return (self.nam % 4 == 0 and self.nam % 100 != 0) or (self.nam % 400 == 0)
