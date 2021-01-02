class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoubleLinkList:
    def __init__(self):
        self.tail = None
        
    
    def insertBeg(self, data):
        if (self.tail == None):
            tmp = Node(data)
            tmp.next = tmp
            tmp.prev = tmp
            self.tail = tmp
        else:
            tmp = Node(data)

            tmp.next = self.tail.next
            tmp.prev = self.tail
            self.tail.next = tmp
    def insertEnd(self, data):
        if (self.tail == None):
            tmp = Node(data)
            self.tail = tmp
            tmp.next = tmp
            tmp.prev = tmp
        else:
            tmp = Node(data)
            beg = self.tail.next
            self.tail.next = tmp
            tmp.prev = self.tail
            tmp.next = beg
            self.tail = tmp
    def traverse(self):
        if (self.tail):
            start = self.tail.next
            if (start==self.tail):
                print(start.data)
            else:
                while (start != self.tail):
                    print(start.data,end=" ")
                    start = start.next
                print(start.data,end=" ")
if __name__ == "__main__":
    ccl = CircularDoubleLinkList()
    ccl.insertBeg(10)
    ccl.insertBeg(20)
    ccl.insertBeg(30)
    ccl.insertEnd(40)
    ccl.insertEnd(50)
    ccl.traverse()
