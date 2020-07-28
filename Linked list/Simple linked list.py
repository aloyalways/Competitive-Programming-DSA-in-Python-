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
            
    def deleteFirst(self):
        if self.head==None:
            print("List is empty")
        else:
            self.head=self.head.next
            
    def view(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next
                
mylist=LinkedList()
mylist.insertLast(10)
mylist.insertLast(20)
mylist.insertLast(30)
mylist.insertLast(40)
print("Linked list before deleting:",end=' ')
mylist.view()
print()
print("Linked list after deleting:",end=' ')
mylist.deleteFirst()
mylist.view()