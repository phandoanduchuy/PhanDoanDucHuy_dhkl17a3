class ThiSinh:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
    
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa
    
    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}, Toán: {self.diem_toan}, Lý: {self.diem_ly}, Hoá: {self.diem_hoa}, Tổng điểm: {self.tinh_tong_diem()}")

def nhap_danh_sach_thi_sinh():
    danh_sach = []
    so_luong = int(input("Nhập số lượng thí sinh: "))
    for i in range(so_luong):
        print(f"Nhập thông tin thí sinh thứ {i + 1}:")
        ho_ten = input("Họ tên: ")
        diem_toan = float(input("Điểm Toán: "))
        diem_ly = float(input("Điểm Lý: "))
        diem_hoa = float(input("Điểm Hoá: "))
        thi_sinh = ThiSinh(ho_ten, diem_toan, diem_ly, diem_hoa)
        danh_sach.append(thi_sinh)
    return danh_sach

def in_ds_trung_tuyen(danh_sach, diem_chuan):
    print("\nDanh sách thí sinh trúng tuyển (điểm chuẩn >= 20):")
    danh_sach_trung_tuyen = [ts for ts in danh_sach if ts.tinh_tong_diem() >= diem_chuan]
    
    danh_sach_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)
    
    if not danh_sach_trung_tuyen:
        print("Không có thí sinh nào trúng tuyển.")
    else:
        for ts in danh_sach_trung_tuyen:
            ts.in_thong_tin()

if __name__ == "__main__":
    diem_chuan = 20
    danh_sach = nhap_danh_sach_thi_sinh()
    in_ds_trung_tuyen(danh_sach, diem_chuan)
