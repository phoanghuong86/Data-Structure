class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.min_arr = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = float('inf') 
        if val <= self.min:
            self.min = val
            self.min_arr.append(val)
        self.stack.append(val)  

    def pop(self) -> None:
        if self.stack[-1] == self.min_arr[-1]:
            self.min_arr.pop()
            if self.min_arr:
                self.min = self.min_arr[-1]
            else:
                self.min = float('inf') 
        self.stack.pop()

        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
