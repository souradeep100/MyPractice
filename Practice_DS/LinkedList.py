class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.dict_prev = dict()
	def insert(self,data):
		
		tmp = self.head
		self.head = Node(data)
		
		self.head.next = tmp
		if (tmp != None):
			self.dict_prev[tmp.data] = self.head
		self.dict_prev[self.head.data] = self.head

	def traverse(self):
		tmp = self.head
		while(tmp):
			print(f"{tmp.data}", end="->")
			tmp = tmp.next
		print("//",end="")
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
	'''
	5->4->2->1-/
	'''
	def swapnodes(self, x, y):
		# Nothing to do if x and y are same 
		if x == y: 
			return       
		# Search for x (keep track of prevX and CurrX) 
		prevX = None
		currX = self.head
		while currX != None and currX.data != x:
			prevX = currX
			currX = currX.next       
		# Search for y (keep track of prevY and currY)
		prevY = None
		currY = self.head
		while currY != None and currY.data != y:
			prevY = currY
			currY = currY.next       
		# If either x or y is not present, nothing to do
		if currX == None or currY == None:
			return
		# If x is not head of linked list
		if prevX != None:
			prevX.next = currY
		else:  # make y the new head
			self.head = currY        
		# If y is not head of linked list
		if prevY != None:
			prevY.next = currX
		else:  # make x the new head
			self.head = currX        
		# Swap next pointers
		temp = currX.next
		currX.next = currY.next
		currY.next = temp
	def reverse(self, h=None):
		if (h):
			tmp = h
		else:
			tmp = self.head
		if (tmp):
			prev = None
			current = tmp
			while (current):
				next = current.next
				current.next = prev
				prev = current
				current = next
			
			tmp = prev
			return tmp
	def getMerge (self, left, right): # 5 and 4
		result = None
		if (left == None):
			return right
		if (right == None):
			return left
		if left.data <= right.data:
			result = left
			print (f"result left is {result.data}")
			result.next = self.getMerge(left.next, right)
		else:
			result = right #4
			print (f"result right is {result.data}")
			result.next = self.getMerge(left, right.next) #5,none
		return result #4->5
	def mergeSort (self,h):
		tmp = h
		slow = h
		first = h
		if (tmp == None or tmp.next == None):
			return h
		while (first.next != None and first.next.next != None):
			slow = slow.next
			first = first.next.next
		#5->4->2->1
		#5->4
		middle = slow #4 #5
		nextmiddle = slow.next #2 #4
		middle.next = None
		print (f"soura{middle.data}")
		
		#now recursion
		left = self.mergeSort(h) #5->4-/ #5-/
		right = self.mergeSort(nextmiddle) #2->1-/ #4-/
		
		sortedlist = self.getMerge(left, right)
		return sortedlist

	def append(self, lst):
		if (self.head == None):
				self.head = lst
				
		else:
			tmp = self.head
			while (tmp.next):
				tmp = tmp.next
			tmp.next = lst

	def blockReverse(self, k):
		if (self.head == None):
			return
		else:
			tmphead = self.head
			
			newlist = LinkedList()
			origin = tmphead
			while (tmphead and tmphead.next):
				count = 1
				tmp_head_newlst = tmphead
				
				while(count % k and tmp_head_newlst.next != None):
					tmp_head_newlst = tmp_head_newlst.next
					count = count+1
				
				tmphead = tmp_head_newlst.next
				tmp_head_newlst.next = None
				newlist.append(self.reverse(origin))
				
				origin = tmphead
			del self.head
			return  newlist

	def detectLoop(self):
		if (self.head == None):
			return False
		slow_ptr = self.head
		first_ptr = self.head
		
		while (first_ptr.next != None and first_ptr.next.next != None):
			
			slow_ptr = slow_ptr.next
			first_ptr = first_ptr.next.next
			if (slow_ptr == first_ptr):
				print (f"Loop!!! at {slow_ptr.data}")
				slow_ptr.next = None
				print ("Fixed")
				self.traverse()
				return True
		return False
	def sumList(self, head1, head2):
		result = LinkedList()
		if (head1 == None):
			result.head = head2
			return result
		if (head2 == None):
			result.head = head1
			return result
		tmp1 = head1
		tmp2 = head2
		carry = 0
		sum = 0
		start = None
		while (tmp1 != None and tmp2 != None):
			
			sum = (tmp1.data + tmp2.data) + carry
			
			print (f"tmp1.data {tmp1.data} + tmp2.data {tmp2.data} is sum {sum}")
			if sum > 10 :
				carry = int(sum / 10)
				sum = sum % 10
			tmp3 = Node(sum)
			if (result.head == None):
				
				result.head = tmp3
				start = result.head
				
			else:
			
				start.next = tmp3
				start = start.next
				
			tmp1 = tmp1.next
			tmp2 = tmp2.next
			tmp = result.head
			while (tmp):
				print(f"result is {tmp.data}")
				tmp = tmp.next
		if (tmp1 != None):
			'''
			while (start.next):
				start = start.next
				print (f"start.data 1 {start.data}")
			'''
			while (tmp1):
				sum = carry + tmp1.data
				carry = 0
				if sum > 10 :
					carry = sum / 10
					sum = sum % 10
				tmp3 = Node(sum)
				start.next = tmp3
				tmp1 = tmp1.next
				start = start.next
		
		if (tmp2 != None):
			
			print (f"start.data is {start.data}")
			'''
			while (start.next):
				
				print (f"start.data is {start.data}")
				start = start.next
			'''
			while (tmp2):
				sum = carry + tmp2.data
				carry = 0
				if sum > 10 :
					carry = sum / 10
					sum = sum % 10
				tmp3 = Node(sum)
				start.next = tmp3
				tmp2 = tmp2.next
				start = start.next
		if (carry):
			tmp3 = Node(carry)
			while (start.next):
				start = start.next
			start.next = tmp3
		return result

	def rotateList(self, k):
		if (self.head == None):
			return
		tmp = self.head
		tail = None
		while (tmp.next):
			tmp = tmp.next
		tail = tmp
		print (f"the tail is {tail.data}")
		count = 0
		while (count < k):
			tmp = self.head
			
			self.head = self.head.next
			tail.next = tmp
			tail = tail.next
			tail.next = None
			count = count+1
			

if __name__ == "__main__":
	llist = LinkedList()
	llist.insert(2)
	llist.insert(1)
	llist.insert(9)
	llist.insert(5)
	llist.traverse()
	newlist = LinkedList()
	newlist.head = llist.mergeSort(llist.head)
	newlist.traverse()
	mylist = newlist.blockReverse(2)
	mylist.traverse()
	looplist = LinkedList()
	first = Node(1)
	second = Node(2)
	third = Node(3)
	third.next = second
	looplist.head = first
	first.next = second
	second.next = third
	res = looplist.detectLoop()
	print(f"res is {res}")
	
	mylist.traverse()
	looplist.traverse()
	sumlist = llist.sumList(mylist.head,looplist.head)
	sumlist.traverse()
	sumlist.rotateList(6)
	sumlist.traverse()
