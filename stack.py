class stack:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item)==0
        if size  < 0:
            print("stack is empty")
    def push(self,data):
        self.item.append(data)
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError()
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError()
    def count(self):
        if not self.is_empty():
            return len(self.item)
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("top elements is ",s1.peek())
print("remove elements is ",s1.pop())
print("top elements is ",s1.peek())
print(s1.count())

print()


    


