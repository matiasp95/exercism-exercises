class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'
class BinarySearchTree:
    def __init__(self, tree_data):
        self._head = TreeNode(tree_data[0])
        for item in tree_data[1:]:
            self._head = mutate_tree(self._head, item)
    def data(self):
        return self._head
    def sorted_data(self):
        return read_tree(self._head)
def mutate_tree(tree: TreeNode, value: str):
    if tree is None:
        return TreeNode(value)
    if value > tree.data:
        tree.right = mutate_tree(tree.right, value)
    else:
        tree.left = mutate_tree(tree.left, value)
    return tree
def read_tree(tree: TreeNode | None) -> list[str]:
    if tree is None:
        return []
    return read_tree(tree.left) + [tree.data] + read_tree(tree.right)