class Hinh_Chu_Nhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))
    
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
    
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    
    def in_thong_tin(self):
        print(f"Hình chữ nhật có chiều dài: {self.chieu_dai} và chiều rộng: {self.chieu_rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

if __name__ =="__main__":
    chieu_dai = float(input("Nhập chiều dài: "))
    chieu_rong = float(input("Nhập chiều rộng: "))
    hcn = Hinh_Chu_Nhat(chieu_dai, chieu_rong)
    hcn.in_thong_tin()
