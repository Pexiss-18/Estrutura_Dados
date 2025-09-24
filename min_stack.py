from stack import Stack

class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_in_stack = Stack()
    
    def push(self,val):
        if self.stack.is_empty() or val <= self.min_in_stack.peek():
            self.min_in_stack.push(val)
        
        self.stack.push(val)

    def pop(self):
        if self.stack.peek() == self.min_in_stack.peek():
            self.min_in_stack.pop()
        self.stack.pop()

    def top(self):
        top = self.stack.peek()
        print(top)
        return top
        
    def getMin(self):
        min = self.min_in_stack.peek()
        print(f'Current Min: {min}')
        return min

stack = MinStack()

stack.push(4)
stack.push(12)
stack.push(3)
stack.push(10)
stack.push(45)
stack.push(1)
stack.push(100)
stack.getMin() 
stack.pop()
stack.pop()
stack.getMin()
stack.pop()
stack.pop()
stack.pop()
stack.getMin()
