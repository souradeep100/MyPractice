class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        
        tmp = self.head
        self.head = Node(data)
        self.head.next = tmp
    def traverse(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next

    def delete(self,key=None):
        if (key==None):
            if (self.head):
                self.head = self.head.next
                self.traverse()
        else:
            tmp = self.head
            if (tmp):
                if (tmp.data == key):
                    self.head = self.head.next
                    print("found")
                    return
                prev = tmp
                tmp = tmp.next
                while (tmp):
                    if (tmp.data == key):
                        prev.next = tmp.next
                        print("found the key")
                        return
                    prev = tmp
                    tmp = tmp.next

if __name__ == "__main__":
    llist = LinkedList()
    
    
    llist.traverse()
    
    
    llist.delete(2)
    llist.delete(3)
    llist.delete(0)
    llist.delete()
    llist.traverse()
