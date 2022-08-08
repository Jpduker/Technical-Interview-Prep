class binarySearchTree():
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key


def insertTree(root, key):
    if root is None:
        return binarySearchTree(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insertTree(root.right, key)
        else:
            root.left = insertTree(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


if __name__ == "__main__":
    bst = binarySearchTree(40)
    bst = insertTree(bst, 30)
    bst = insertTree(bst, 20)
    bst = insertTree(bst, 50)
    bst = insertTree(bst, 60)

    inorder(bst)
