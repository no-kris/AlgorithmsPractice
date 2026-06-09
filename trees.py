from typing import Any, Optional, Self


class TreeNode:
    def __init__(
        self,
        data: Any,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def tree_search(self, value: Any, node: TreeNode) -> Optional[TreeNode]:
        if node.data == value:
            return node
        elif value < node.data and node.left:
            return self.tree_search(value, node.left)
        elif value > node.data and node.right:
            return self.tree_search(value, node.right)
        else:
            return None

    def tree_insert(self, value: Any, node: TreeNode) -> Self:
        if value < node.data:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self.tree_insert(value, node.left)
        elif value > node.data:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self.tree_insert(value, node.right)
        return self

    def delete_node(self, node: Optional[TreeNode], value: Any) -> Optional[TreeNode]:
        if not node:
            return None

        if value < node.data:
            node.left = self.delete_node(node.left, value)
        elif value > node.data:
            node.right = self.delete_node(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self.delete_node(node.right, min_node.data)
        return node

    def _find_min(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left:
            current = current.left
        return current

    def _find_max(self, node: TreeNode) -> TreeNode:
        current = node
        while current.right:
            current = current.right
        return current

    def inorder_traverse(self, node: Optional[TreeNode]):
        if not node:
            return
        self.inorder_traverse(node.left)
        print(node.data)
        self.inorder_traverse(node.right)

    def preorder_traversal(self, node: Optional[TreeNode]):
        if not node:
            return
        print(node.data)
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)

    def postorder_traversal(self, node: Optional[TreeNode]):
        if not node:
            return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.data)


def test_search_success(bst: BinarySearchTree, values: list, start_node: TreeNode):
    assert bst.tree_search(values[0], start_node) is not None
    assert bst.tree_search(values[1], start_node) is not None
    print("All successfull tests passed.")


def test_search_fail(bst: BinarySearchTree, values: list, start_node: TreeNode):
    assert bst.tree_search(values[0], start_node) is None
    assert bst.tree_search(values[1], start_node) is None
    print("All failed tests passed.")


def main():
    node1 = TreeNode(25)
    node2 = TreeNode(75)
    root = TreeNode(50, node1, node2)
    bst = BinarySearchTree(root)

    test_search_success(bst, [25, 75], root)
    test_search_fail(bst, [32, 44], root)


if __name__ == "__main__":
    main()
