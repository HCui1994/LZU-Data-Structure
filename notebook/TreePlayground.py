class nil(object):
    pass


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left, self.right, self.parent = nil, nil, nil


class BinaryTree(object):
    def __init__(self, vals):
        """
        initialize binary tree as a binary search tree
        """
        self.dummy_root = TreeNode(float("inf"))
        self.nodes_dict = {}
        for val in vals:
            new_node = TreeNode(val)
            parent = self.dummy_root
            node = parent
            while node != nil:
                if val < node.val:
                    parent, node = node, node.left
                    is_left = True
                else:
                    parent, node = node, node.right
                    is_left = False
            if is_left:
                parent.left = new_node
                self.nodes_ref_dict[new_node] = {"parent": parent, "ref": new_node, "isLeft": True}
            else:
                parent.right = new_node
                self.nodes_dict[new_node] = {"parent": parent, "ref": new_node, "isLeft": False}
        self.root = self.dummy_root

    def pretty_print_tree(self, node="default", prefix="", isLeft=True):
        if node == "default":
            node = self.root
        if node == nil:
            return
        if node.right:
            self.pretty_print_tree(node.right, prefix + ("│   " if isLeft else "    "), False)
        print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))
        if node.left:
            self.pretty_print_tree(node.left, prefix + ("    " if isLeft else "│   "), True)

    def get_nodes_dict(self):
        return self.nodes_dict


if __name__ == "__main__":
    bst = BinaryTree([5, 3, 8, 1, 4, 2, 6, 9, 7])
    bst.pretty_print_tree()
    print(bst.get_nodes_dict())
