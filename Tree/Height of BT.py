class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
    
    def height(self,root):
        if root is None:
            return 0
        lheight=root.height(root.left)
        rheight=root.height(root.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1
    
root=Node(3)
root.left=Node(9)
root.right=Node(20)
root.right.left=Node(15)
root.right.right=Node(7)
print(root.height(root))