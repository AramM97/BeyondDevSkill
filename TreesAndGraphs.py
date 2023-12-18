from _collections import deque
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def findPath(root, path, k):
    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return True

    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True

    path.pop()
    return False


def lca(root, num1, num2):
    path1 = []
    path2 = []

    if (not findPath(root, path1, num1) or not findPath(root, path2, num2)):
        return -1

    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]

def shortest_path(root, target1, target2):
    if not root:
        return None

    queue = deque([(root, [])])

    while queue:
        current_node, current_path = queue.popleft()

        if current_node.val == target1:
            # Found the first target node
            return current_path + [target1]

        if current_node.val == target2:
            # Found the second target node
            return current_path + [target2]

        if current_node.left:
            queue.append((current_node.left, current_path + [current_node.val]))

        if current_node.right:
            queue.append((current_node.right, current_path + [current_node.val]))

    return None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return TreeNode(value)
        if value < root.val:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)
        return root

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, root, value):
        if root is None:
            return root

        if value < root.val:
            root.left = self._delete(root.left, value)
        elif value > root.val:
            root.right = self._delete(root.right, value)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            root.val = self._min_value_node(root.right).val
            root.right = self._delete(root.right, root.val)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, root, value):
        if root is None or root.val == value:
            return root
        if value < root.val:
            return self._search(root.left, value)
        return self._search(root.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.val)
            self._inorder_traversal(root.right, result)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    target1 = 4
    target2 = 7

    path = shortest_path(root, target1, target2)

    if path:
        print(f"Shortest path between {target1} and {target2}: {path}")
    else:
        print(f"No path found between {target1} and {target2}")

    bst = BinarySearchTree()
    elements = [50, 30, 20, 40, 70, 60, 80]

    for element in elements:
        bst.insert(element)

    print("Inorder traversal:", bst.inorder_traversal())

    search_value = 40
    search_result = bst.search(search_value)
    print(f"Search for {search_value}: {'Found' if search_result else 'Not Found'}")

    delete_value = 30
    bst.delete(delete_value)
    print(f"Deleted node with value {delete_value}. Inorder traversal:", bst.inorder_traversal())
    