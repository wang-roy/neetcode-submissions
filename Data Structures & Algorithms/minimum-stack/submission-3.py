class MinStack:

    def __init__(self):
        self.minimum = None
        self.stack = []

    def push(self, val: int) -> None:
        previous_min = self.minimum
        if self.minimum is None:
            self.minimum = val
        elif val < self.minimum:
            self.minimum = val
        
        self.stack.append((val, previous_min))

    def pop(self) -> None:
        val, previous_min = self.stack[-1]
        self.minimum = previous_min
        self.stack.pop(-1)

    def top(self) -> int:
        val, _ = self.stack[-1]
        # print('here? top')
        return val

    def getMin(self) -> int:
        print(self.stack)
        # print('here? getmin')
        return self.minimum
        
