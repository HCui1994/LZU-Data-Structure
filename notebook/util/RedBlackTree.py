class nil(object):
    pass


class RBNode(object):
    def __init__(self, x):
        self.val = x
        self.left, self.right, self.parent = nil, nil, nil


class RedBlackTree(object):
    def __init__(self, vals):
        """
        initialize binary search tree
        """
        self.root = nil
        for val in vals:
            self.insert(val)

    def reset(self, vals):
        self.root = nil
        for val in vals:
            self.insert(val)

    def insert(self, node):
        new_node = RBNode(node) if type(node) == int else node
        if self.root == nil:
            self.root = new_node
            return
        node = self.root
        while node != nil:
            parent = node
            if new_node.val < node.val:
                node = node.left
            else:
                node = node.right
        if new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent

    # def delete(self, node):

    def pretty_print_tree_bst(self, node="default", prefix="", isLeft=True):
        if node == "default":
            node = self.root
        if node == nil:
            return
        if node.right:
            self.pretty_print_tree(node.right, prefix + ("│   " if isLeft else "    "), False)
        print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))
        if node.left:
            self.pretty_print_tree(node.left, prefix + ("    " if isLeft else "│   "), True)

    def get_min(self, node):
        if node == nil:
            return node
        while node.left != nil:
            node = node.left
        return node

    def get_max(self, node):
        if node == nil:
            return node
        while node.right != nil:
            node = node.right
        return node

    def get_predecessor(self, node):
        if type(node) == int:
            node = self.search(node)
        if node == nil:
            return node
        if node.left != nil:
            return self.get_max(node.left)
        parent = node.parent
        while parent != nil and parent.left == node:
            node, parent = parent, parent.parent
        return parent

    def get_successor(self, node):
        if type(node) == int:
            node = self.search(node)
        if node == nil:
            return node
        if node.right != nil:
            return self.get_min(node.right)
        parent = node.parent
        while parent != nil and parent.right == node:
            node, parent = parent, parent.parent
        return parent

    def set_root(self, new_root):
        self.root = new_root

    def search(self, target):
        node = self.root
        while node != nil:
            if node.val == target:
                return node
            if node.val < target:
                node = node.right
            else:
                node = node.left
        print("not found")
        return node

    def rotate_left(self, pivot):
        """
        以 pivot 为轴，进行左旋
        左旋将轴的右子上升，轴下降
        轴成为原右子的左子，原右子的原左子成为轴的右子
        """
        pivot_parent, pivot_right = pivot.parent, pivot.right
        pivot.right = pivot_right.left  # 轴接管原右子的左子
        if pivot.right != nil:         # 若新右子非空
            pivot.right.parent = pivot  # 建立新右子到轴的链接
        if pivot_parent != nil:        # 若轴非根
            if pivot == pivot_parent.left:  # 原右子上升
                pivot_parent.left = pivot_right
            else:
                pivot_parent.right = pivot_right
        else:
            self.root = pivot_right
        pivot_right.parent = pivot_parent
        pivot_right.left = pivot       # 轴下降
        pivot.parent = pivot_right

    def rotate_right(self, pivot):
        """
        以 pivot 为轴，进行右旋
        右旋将轴的左子上升，轴下降
        轴成为原左子的右子，原左子的右子成为轴的左子
        """
        pivot_parent, pivot_left = pivot.parent, pivot.left
        pivot.left = pivot_left.right
        if pivot.left != nil:
            pivot.left.parent = pivot
        if pivot_parent != nil:            # 若轴非根
            if pivot == pivot_parent.left:  # 原左子上升
                pivot_parent.left = pivot_left
            else:
                pivot_parent.right = pivot_left
        else:
            self.root = pivot_left
        pivot_left.parent = pivot_parent
        pivot_left.right = pivot            # 轴下降
        pivot.parent = pivot_left


if __name__ == "__main__":
    rbtree = RedBlackTree([5, 3, 8, 1, 4, 2, 6, 9, 7])
    rbtree.pretty_print_tree()
    node = rbtree.search(5)
    print(node.val)
    print(rbtree.get_predecessor(node).val)
