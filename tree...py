def inorder(self,node):
    if node:
        self.inorder(node.left)
        print(node.value,end=" ")
        self.inorder(node.right)
def preorder(self,node):
    if node:
        print(node.value,end=" ")
        self.preorder(node.right)
        print(node.value,end=" ")
def postorder(self,node):
    if node:
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value,end=" ")


tree=BinaryTree(5)
tree.insert(tree.root, 8)
tree.insert(tree.root, 4)
tree.insert(tree.root, 9)
tree.insert(tree.root, 6)

print("In-order traversal:")
tree.inorder(tree.root)

print
