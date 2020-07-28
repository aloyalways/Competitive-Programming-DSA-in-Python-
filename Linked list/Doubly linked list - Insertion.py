class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        
    def insertFirst(self,value):
        newNode=Node(value)
        
        newNode.next=self.head
        newNode.prev=None
        if self.head is not None:
            self.head.prev=newNode
        self.head=newNode
        
    def insertAfter(self,prev_node,value):
        if prev_node==None:
            print("This node doesn't exist.")
            
        newNode=Node(value)
        newNode.next=prev_node.next
        newNode.prev=prev_node
        prev_node.next=newNode
        if newNode.next is not None:
            newNode.next.prev=newNode
        
    def insertLast(self,value):
        newNode=Node(value)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newNode
        newNode.prev=temp
        newNode.next=None
    
    def printList(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.next
            
dll=DoublyLinkedList()
dll.insertFirst(10)
dll.insertFirst(20)
dll.insertFirst(30)
dll.insertAfter(dll.head.next,40)
dll.insertLast(50)
dll.printList()
