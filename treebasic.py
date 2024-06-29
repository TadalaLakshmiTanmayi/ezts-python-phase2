class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
t=Node(1)
a=Node(2)
b=Node(3)
t.left=a
t.right=b
print(t.right.data)
