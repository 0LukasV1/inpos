class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return not bool(self.stack)
    def push(self, item):
        self.stack.append(item)
    def pop_item(self):
        if not self.is_empty():
            return self.stack.pop()
    def top(self):
        return self.stack[-1]
def get_precedence(operator):
    if operator in ['*', '/']:
        return 2
    elif operator in ['+', '-']:
        return 1
    return 0
operator_stack = Stack()
expression = input("napis input: ")

output = []

for char in expression:
    if char.isdigit():
        output.append(char)
    elif char == '(':
        operator_stack.push(char)
    elif char == ')':
        while operator_stack.top() != '(':
            output.append(operator_stack.pop_item())
        operator_stack.pop_item()
    else:
        while (not operator_stack.is_empty() and
               operator_stack.top() != '(' and
               get_precedence(char) <= get_precedence(operator_stack.top())):
            output.append(operator_stack.pop_item())
        operator_stack.push(char)

while not operator_stack.is_empty():
    output.append(operator_stack.pop_item())

print(''.join(output))