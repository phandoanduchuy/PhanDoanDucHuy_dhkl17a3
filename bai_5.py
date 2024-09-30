class Stack:
    def __init__(self, kich_thuoc):
        self.kich_thuoc = kich_thuoc
        self.stack = []  # Mảng động lưu trữ các phần tử (float)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) == self.kich_thuoc
    
    def push(self, gia_tri):
        if self.isFull():
            print("Ngăn xếp đã đầy. Không thể thêm phần tử.")
        else:
            self.stack.append(float(gia_tri))
            print(f"Đã thêm {gia_tri} vào ngăn xếp.")
    
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống. Không thể lấy phần tử.")
            return None
        else:
            gia_tri_lay_ra = self.stack.pop()
            print(f"Popped {gia_tri_lay_ra} from the stack.")
            return gia_tri_lay_ra
    
    def count(self):
        return len(self.stack)
    
    def delete(self):
        print("Ngăn xếp đã bị hủy.")
