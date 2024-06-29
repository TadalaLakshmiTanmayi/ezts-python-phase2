class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertatbeg(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def insertatend(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=newnode
    def deleteatbeg(self):
        if self.head==None or self.head.next==None:
            return 0
        else:
            self.head=self.head.next
    def deleteatend(self):
        if self.head==None or self.head.next==None:
            return 0
        else:
            curr=self.head
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None
    def count(self):
        curr=self.head
        count=0
        while(curr!=None):
            count+=1
            curr=curr.next
        print(count)
    def printlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data,end="-->")
            curr=curr.next
        print("null")
    def reversell(self):
        prev=None
        next=None
        curr=self.head
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
l=LinkedList()
l.insertatbeg(1)  
l.insertatbeg(2)
l.insertatbeg(3)
l.insertatend(5)
l.count()
l.printlist()
l.deleteatbeg()
l.printlist()
l.deleteatend()
l.printlist()
l.reversell()
l.printlist()