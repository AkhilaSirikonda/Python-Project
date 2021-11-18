class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:  # since BST doesn't take duplicates it just return the BST
            return
        if data < self.data:  # implies adding data in the left subtree
            if self.left:  # checks if it already has left node i.e. checks if it is a leaf node
                self.left.add_child(
                    data)  # this itself a small bst which calls addchild function to add child recursively
            else:
                self.left = BinarySearchTreeNode(data)  # as bst is recursive you keep on calling class BST to
        else:  # add data in the right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        # left
        if self.left: # check for left sub tree, if it is there add elements to this left subtree
            elements += self.left.in_order_traversal()
        # Root
        elements.append(self.data)
        # right
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        #Root
        elements.append(self.data)
        #Left
        if self.left:
            elements += self.left.pre_order_traversal()
        #Right
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        #Left
        if self.left:
            elements += self.left.post_order_traversal()
        #Right
        if self.right:
            elements += self.right.post_order_traversal()
        # Root
        elements.append(self.data)

        return elements


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    numbers = [23, 3, 14, 5, 34, 76]
    l1 = build_tree(numbers)
    print(l1.in_order_traversal())
    print(l1.pre_order_traversal())
    print(l1.post_order_traversal())
    