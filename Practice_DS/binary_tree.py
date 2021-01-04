class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None


def inorder(root):
    if root == None:
        return
    else:
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                print(root.data, end=" ")
                root = root.right
            else:
                break
def inorder2(root):
    if root == None:
        return
    else:
        stack = []
        while True:
            if (root):
                stack.append(root)
                root = root.left
            elif stack:
                current = stack.pop()
                print (current.data, end=" ")
                
                root = current.right
                
            else:
                break
        
def preorder(root):
    if root == None:
        return
    else:
        stack = [root]
        output = []
        while stack:
            current = stack.pop()
            if current:
                output.append(current)
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
        for vals in output:
            print(vals.data, end=" ")
def postorder(root):
    if root == None:
        return
    stack = [root]
    output = []
    while stack:
        current = stack.pop()
        output.append(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    for val in output[::-1]:
        print(val,end="//")   
    return output[::-1]
def levelorder(root):
    if root == None:
        return
    output_final = []
    output = []
    queue = [root]
    while queue:
        output = []
        for i in range(len(queue)):
            current = queue.pop(0)
            output.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        output_final.append(output)
    print (output_final)
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.right = Node(60)
    '''
            10
        20      30
     40    50      60
    '''
    inorder(root)
    preorder(root)
    postorder(root)
    levelorder(root)

'''

1)Maximum width of a binary tree
2)Print nodes at k distance from root
3)Print Ancestors of a given node in Binary Tree
4)Check if a binary tree is subtree of another binary tree
5)Connect nodes at same level
from geeksforgeek

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return None
        queue = [root]
        output = []
        while queue:
            current = queue.pop(0)
            print (current)
            if current == None :
                output.append("null")
                continue
            output.append(str(current.val))
            
            queue.append(current.left)
            
            queue.append(current.right)
        print(output)
        return ",".join(output)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data:
            data = data.split(',')
        else:
            return None
        count = 0
        val = data[count]
        queue = []
        if val != 'null':
            root = TreeNode(int(val))
            queue.append(root)
        else:
            return None
        while queue:
            node = queue.pop(0)
            count += 1
            if (count < len(data)):
                val = data[count]
            else:
                break
            if val != 'null':
                node.left = TreeNode(int(val))
                queue.append(node.left)
            else:
                node.left = None
            count += 1
            if (count < len(data)):
                val = data[count]
            else:
                break
            if val != 'null':
                node.right = TreeNode(int(val))
                queue.append(node.right)
            else:
                node.right = None
        return root
'''