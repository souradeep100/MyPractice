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
