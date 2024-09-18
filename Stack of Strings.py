class Stack:
    def __init__(self):
        self.data = []  

    def push(self, item: str):
        if isinstance(item, str):  
            self.data.append(item)
        else:
            raise ValueError("Only strings are allowed")

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(self.data)}]"


stack = Stack()
stack.push("hello")
stack.push("world")
print(stack)  

print(stack.peek())  
print(stack.pop())   
print(stack.is_empty())  
print(stack.pop())   
print(stack.is_empty())  
