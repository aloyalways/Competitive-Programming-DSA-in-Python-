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
            
    # Postorder traversal
    # Left -> Right -> Node
    def PostOrderTraversal(self,root):
        res=[]
        if root:
            res=self.PostOrderTraversal(root.left)
            res+=self.PostOrderTraversal(root.right)
            res.append(root.val)
        return res 
    
root=Node(3)
root.left=Node(9)
root.right=Node(20)
root.right.left=Node(15)
root.right.right=Node(7)
print(root.PostOrderTraversal(root))
