class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def inorder(self,root):#left root right
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)