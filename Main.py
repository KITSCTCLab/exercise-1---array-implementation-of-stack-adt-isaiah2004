
class Stack:
    def __init__(self, size):
        self.items = [] * null;
        self.size = size

    def is_empty(self):
        """
        Check The List items if it is empty.
        Returns true if empty false if not.
        """
        # Write code here
        if items[0] == null:
            return true
        return false



    def is_full(self):
        """
        Check if The stack is full.
        Returns true if full
        returns false if not full.
        """
        # Write code here
        if items[size-1]!=null :
            return true
        return false

    def push(self, data):
        """Pushes value to stack if stack is empty"""
        if not self.is_full():
            # Write code here
            items.append(data)

    def pop(self):
        if not self.is_empty():
            # Write code here
            items.pop()

    def status(self):
        # Write code here
        for i in range (items):
            if i!=null:
                println(i)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
