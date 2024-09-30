class Stack:
    def __init__(self, kich_thuoc):
        self.kich_thuoc = kich_thuoc
        self.stack = [] 
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) == self.kich_thuoc
    
    def push(self, value):
        if self.isFull():
            print("Stack is full. Cannot push element.")
        else:
            self.stack.append(float(value))
            print(f"Pushed {value} into the stack.")
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty. Cannot pop element.")
            return None
        else:
            popped_value = self.stack.pop()
            print(f"Popped {popped_value} from the stack.")
            return popped_value
    
    def __del__(self):
        print("Stack is destroyed.")
