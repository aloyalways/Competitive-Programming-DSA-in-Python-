class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()
            
    # Preorder traversal
    # Root -> Left -> Right
    def PreOrderTraversal(self,root):
        res=[]
        if root:
            res.append(root.val)
            res+=self.PreOrderTraversal(root.left)
            res+=self.PreOrderTraversal(root.right)
        return res 
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print(root.PreOrderTraversal(root))
