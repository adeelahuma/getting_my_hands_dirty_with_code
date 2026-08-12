class Node:
    data: int = None
    next: Node

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)    


class LinkedList:

    head: Node
    tail: Node

    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def add_at_start(self, node: Node):
        node.next = self.head.next
        self.head.next = node
        if self.tail is self.head:
            self.tail = node

    def add_at_end(self, node: Node):
        node.next = None
        if self.head.next is None:
            self.head.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

                        


    # def delete(self):
    #     pass    

    def print(self):

        curr = self.head.next
        while (curr != None):
            print(f"{curr}")
            curr = curr.next



def main():
    print("Hello world!!")

    # ll = LinkedList()
   
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)

    # ll.add_at_start(node_1)
    # ll.add_at_start(node_2)
    # ll.add_at_start(node_3)
    # ll.add_at_start(node_4)
    # ll.add_at_start(node_5)
    # ll.add_at_start(node_6)

    # print(f"head: {ll.head.next} - tail: {ll.tail.next}")
    # ll.print()

    print("--------------------------")


    ll_1 = LinkedList()

    ll_1.add_at_end(node_1)
    ll_1.add_at_end(node_2)
    ll_1.add_at_end(node_3)
    ll_1.add_at_end(node_4)
    ll_1.add_at_end(node_5)
    ll_1.add_at_end(node_6)

    print(f"head: {ll_1.head} - tail: {ll_1.tail}")
    ll_1.print()



if __name__ == "__main__":
    main()