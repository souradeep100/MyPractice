class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLL:
    def __init__(self):
        self.tail = None

    def insert(self, data):
        if (self.tail == None):
            self.tail = Node(data)
            self.tail.next = self.tail
        else:
            tmp = Node(data)
            end = self.tail
            beg = end.next
            tmp.next = beg
            end.next = tmp
            self.tail = tmp
    def traverse(self):
        if (self.tail):
            tmp = self.tail.next
            while(tmp != self.tail):
                print(tmp.data, end=" ")
                tmp = tmp.next
            print(tmp.data, end=" ")
    def split(self):
        if (self.tail == None):
            return None
        else:
            slow = self.tail.next
            first = self.tail.next
            while(first.next != self.tail and first.next.next != self.tail):
                slow = slow.next
                first = first.next.next
            mid = slow
            print(mid.data)
            start = self.tail.next
            start2 = slow.next
            print(start2.data)
            half1 = CircularLL()
            half1.tail = mid
            mid.next = start
            print(half1.tail.next.data)
            self.tail.next = start2
            half2 = CircularLL()
            half2.tail = self.tail
        return (half1, half2)


if __name__ == "__main__":
    ccl = CircularLL()
    ccl.insert(1)
    ccl.insert(2)
    
    ccl.traverse()
    h1, h2 = ccl.split()
    h1.traverse()
    print ("soura")
    h2.traverse()