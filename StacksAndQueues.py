class Stack:

    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0


# Implement a stack using two queues.
from _collections import deque


class CreatingStackWithTwoQueues:

    def __init__(self):

        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):

        # Push x first in empty q2
        self.q2.append(x)

        # Push all the remaining
        # elements in q1 to q2.
        while (self.q1):
            self.q2.append(self.q1.popleft())

        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):

        # if no elements are there in q1
        if self.q1:
            self.q1.popleft()

    def top(self):
        if (self.q1):
            return self.q1[0]
        return None

    def size(self):
        return len(self.q1)

#Implement a queue using two stacks.
class CreatingQueueWithTwoStacks:

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, item):
        self.stack_1.push(item)

    def dequeue(self):
        if not self.stack_1.is_empty():
            while self.stack_1.size() > 0:
                self.stack_2.push(self.stack_1.pop())
            res = self.stack_2.pop()
            while self.stack_2.size() > 0:
                self.stack_1.push(self.stack_2.pop())
            return res

#Write a program to check if a given string of parentheses is balanced.
def is_balanced_parentheses(input_string):
    stack = Stack()

    for char in input_string:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if not is_matching_parentheses(top_element, char):
                return False

    return stack.is_empty()

def is_matching_parentheses(opening, closing):
    # Helper function to check if the opening and closing parentheses match
    return (opening == '(' and closing == ')') or \
           (opening == '{' and closing == '}') or \
           (opening == '[' and closing == ']')



if __name__ == "__main__":
    # Test Stack implementation
    print("Testing Stack:")
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Pop:", stack.pop())
    # Accessing the top element directly from the 'elements' list
    top_element = stack.elements[-1] if stack.elements else None
    print("Top:", top_element)
    print("Size:", stack.size())
    print("Is Empty:", stack.is_empty())
    print()

    # Test CreatingStackWithTwoQueues implementation
    print("Testing CreatingStackWithTwoQueues:")
    stack_with_queues = CreatingStackWithTwoQueues()

    stack_with_queues.push(1)
    stack_with_queues.push(2)
    stack_with_queues.push(3)

    print("Pop:", stack_with_queues.pop())
    print("Top:", stack_with_queues.top())
    print("Size:", stack_with_queues.size())
    print()

    # Test CreatingQueueWithTwoStacks implementation
    print("Testing CreatingQueueWithTwoStacks:")
    queue_with_stacks = CreatingQueueWithTwoStacks()

    queue_with_stacks.enqueue(1)
    queue_with_stacks.enqueue(2)
    queue_with_stacks.enqueue(3)

    print("Dequeue:", queue_with_stacks.dequeue())
    print()

    # Test is_balanced_parentheses function
    print("Testing is_balanced_parentheses:")
    test_strings = [
        "({[]})",
        "({[}])",
        "({[]",
        "{[()]}"
    ]

    for test_str in test_strings:
        if is_balanced_parentheses(test_str):
            print(f"{test_str} is balanced.")
        else:
            print(f"{test_str} is not balanced.")
    print()
