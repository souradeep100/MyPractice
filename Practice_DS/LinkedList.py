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

    def delete(self, key=None):
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
    
    def delete_pos(self, pos):
        tmp = self.head
        if (tmp):
            count = 0
            if pos == 0:
                self.head = self.head.next
                print("Deleted")
                return
            prev = tmp
        
            while (count != pos):
                prev = tmp
                if (tmp.next == None):
                    return
                tmp = tmp.next
                count = count+1
            prev.next = tmp.next
            print("deleted now")

    def  findlengthrec(self, current=None):
        if (current == None):
            if (self.head):
                tmp = self.head
                return (self.findlengthrec(tmp))
            else:
                return 0
        else:
            if (current.next == None):
                return 1
            else:
                return (1+self.findlengthrec(current.next))
    
    def findkeyrec(self,cur,key):
        if cur.data == key:
            return True
        if cur.next == None:
            return False
        else:
            return self.findkeyrec(cur.next,key)

    def findkey(self,key):
        tmp = self.head
        return self.findkeyrec(tmp,key)
if __name__ == "__main__":
    llist = LinkedList()
    llist.insert(1)
    
    
    llist.traverse()
    lenth = llist.findlengthrec()
    print(lenth)
    print(llist.findkey(2))
    
    
    
    

    
