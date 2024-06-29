class stacks:
    def __init__(self):
        self.l=[]
        self.size=5
    def push(self,data):
        if len(self.l)!=self.size:
            self.l.append(data)
        else:
            print("Stack overflow")
            return 0
    def pop(self):
        if(len(self.l)==0):
            print("Stack underflow")
        else:
            self.l.pop()

    def peek(self):
        if(len(self.l)==0):
            print("empty")
        else:
            print(self.l[-1])
s=stacks()
s.push(3)
s.push(4)
s.peek()
s.pop()
s.peek()
