class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insertLast(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            
    def reverse(self):
        prev=None
        curr=self.head
        while curr is not None:
            curr_next=curr.next
            curr.next=prev
            prev=curr
            curr=curr_next
        self.head=prev
            
    def view(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            print("HEAD -> ",end="")
            while temp is not None:
                print(temp.data,end=" -> ")
                temp=temp.next
            print(None)

l1=LinkedList()
l1.insertLast(1)
l1.insertLast(2)
l1.insertLast(3)
l1.insertLast(4)
l1.insertLast(5)
l1.insertLast(6)
l1.view()
l1.reverse()
l1.view()