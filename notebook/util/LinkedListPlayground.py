class ListNode(object):
    def __init__(self, x, next=None):
        self.val, self.next = x, next
        

class DoubleListNode(object):
    def __init__(self, x, left=None, right=None):
        self.val, self.left, self.right = x, left, right

        
class SingleLinkedList(object):
    def __init__(self, nodes):
        dummy_head = ListNode("dummy")
        curr = dummy_head
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next
        self.head = dummy_head  # 不再是 self.head = dummy_head.next
    
    def display(self):
        if not self.head:
            print("empty linked list")
            return
        curr = self.head
        while curr:
            print(curr.val, "-> " if curr.next else "", end="")
            curr = curr.next
        print("")
        
    def get_head(self):
        return self.head


class SingleLinkedListCyclic(object):
    def __init__(self, nodes):
        dummy_head = ListNode("dummy")
        curr = dummy_head
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next
        self.head = dummy_head  # 不再是 self.head = dummy_head.next
        curr.next = dummy_head  # 形成循环
    
    def display(self):
        if not self.head:
            print("empty linked list")
            return
        curr = self.head
        while curr.next != self.head:  # 判断条件始终为 curr.next，防止越界
            print(curr.val, "-> ", end="")
            curr = curr.next
        print(curr.val, "-> ", end="")  # 当前 curr 指向最后一个节点
        print("")
        
    def insert(self, dummy_head: ListNode, a: int, b: int):
        new_node = ListNode(b)
        dummy_head.val = a  # 将dummy head 赋值为 a，在循环一轮而未找到 a 的情况下，形成终止条件
        prev, curr = dummy_head, dummy_head.next 
        while curr.val != a:  # 新的循环条件，无需异常处理
            prev, curr = curr, curr.next
        prev.next, new_node.next = new_node, curr
        dummy_head.val = "dummy"  # 还原 dummy head
    
    def delete(self, dummy_head: ListNode, a: int):
        prev, curr = dummy_head, dummy_head.next
        while curr.val != a and curr.next.val != "dummy":
            prev, curr = curr, curr.next
        if curr.val == a:  # 找到 a 节点
            prev.next = curr.next
        # else: ...  未找到 a 节点，不作任何处理
        
    def get_head(self):
        return self.head
        

class DoubleLinkedList(object):
    def __init__(self, nodes):
        dummy_head = DoubleListNode("dummy")
        node = dummy_head
        for x in nodes:
            new_node = DoubleListNode(x)
            node.right, new_node.left = new_node, node
            node = node.right
        node.right, dummy_head.left = dummy_head, node
        self.head = dummy_head
    
    def display(self):
        if not self.head:
            print("empty linked list")
            return
        curr = self.head
        while curr.right != self.head:  # 判断条件始终为 curr.next，防止越界
            print(curr.val, "<-> ", end="")
            curr = curr.right
        print(curr.val, "<-> ", end="")  # 当前 curr 指向最后一个节点
        print("")
        
    def get_head(self):
        return self.head

        
def display(head):
    if not head:
        print("empty linked list")
        return
    if type(head) == DoubleListNode:
        curr = head
        while curr.right != head:  # 判断条件始终为 curr.next，防止越界
            print(curr.val, "<-> ", end="")
            curr = curr.right
        print(curr.val, "<-> ", end="")  # 当前 curr 指向最后一个节点
        print("")
    elif type(head) == ListNode:
        curr = head
        while curr:
            print(curr.val, "-> " if curr.next else "", end="")
            curr = curr.next
        print("")
    

if __name__ == "__main__":
    single = SingleLinkedList([1, 2, 3, 4, 5, 6, 7])
    single.reverse_iterative()
    single.traverse_linked_list()
