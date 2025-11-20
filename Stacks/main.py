
# A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
# Basic operations we can do on a stack are:

# Push: Adds a new element on the stack.
# Pop: Removes and returns the top element from the stack.
# Peek: Returns the top (last) element on the stack.
# isEmpty: Checks if the stack is empty.
# Size: Finds the number of elements in the stack.
stack = []

# Using a Python list as a stack:

#Push elements onto the stack
stack.append("A")
stack.append("B")
stack.append("C")

print("Stack:", stack)
# Pop elements from the stack
x = stack.pop() 
 # Removes "C"
print(x)  # Output: C
print("Stack after pop:", stack)

 # Checks if stack is non-empty
x = not bool(stack) 

# Peek at the top element without removing it
peek = stack[-1] if stack else None  
print("Top element (peek):", peek)  # Output: Bprint("Is stack empty?", x)  # Output: Falseprint("Is stack empty?", x)  # Output: False

# Get the current size of the stack
size = len(stack)  
print("Current stack size:", size)  # Output: 2


print("\n--- Stack Implementation using Class ---\n")

class Stack: 
    def __init__(self):
        self.stack = []

    def push (self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    

myStack = Stack()
myStack.push("X")
myStack.push("Y")
myStack.push("Z")
print("Stack:", myStack.stack)

print("Popped element:", myStack.pop())  # Output: Z
print("Stack after pop:", myStack.stack)

print("Is stack empty?", myStack.isEmpty())
print("Top element (peek):", myStack.peek())  # Output: Y
print("Current stack size:", myStack.size())  # Output: 2