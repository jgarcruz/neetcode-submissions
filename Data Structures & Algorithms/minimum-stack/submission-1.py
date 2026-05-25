class MinStack:
    # push(-2), push(0), push(-3), pop(), pop(), push(-3), push(1), pop(), pop()

    # stack: []
    # minStack: [] 

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
