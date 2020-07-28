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
            
    # Inorder traversal
    # Left -> Root -> Right
    def InOrderTraversal(self,root):
        res=[]
        if root:
            res=self.InOrderTraversal(root.left)
            res.append(root.val)
            res+=self.InOrderTraversal(root.right)
        return res 
    
root=Node(3)
root.left=Node(9)
root.right=Node(20)
root.right.left=Node(15)
root.right.right=Node(7)
print(root.InOrderTraversal(root))
