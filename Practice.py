class Node:
    def __init__(self, data):
        self.data = data

        self.prev = None

        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)

    # 先頭に追加
    def preappend(self, newNode):
        self.head.prev = newNode
        newNode.next = self.head
        newNode.prev = None
        self.head = newNode

    # 最後に追加
    def append(self, newNode):
        self.tail.next = newNode
        newNode.next = None
        newNode.prev = self.tail
        self.tail = newNode

    # 先頭から要素をpop
    def popFront(self):
        self.head = self.head.next
        self.head.prev = None

    # 末尾から要素をpop
    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = None

    # 与えられたノードをO(1)で削除します。
    def deleteNode(self, node):

        if node is self.tail: return self.pop()

        if node is self.head: return self.popFront()

        node.prev.next = node.next
        node.next.prev = node.prev

class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.dict={}
        self.list=DoublyLinkedList()

    def get(self,key):
        if key not in self.list:
            return "null"
        else:
            node=self.dict[key]
            self.list.deleteNode(node)
            self.list.preappend(node)

            return node.data

    # dataをキャッシュに追加
    def put(self,key,data):
        if key in self.dict:
            node=self.dict[key]
            node.data=data
            self.list.deleteNode(node)
            self.list.preappend(node)
        else:
            if len(self.dict)==self.capacity:
                self.list.pop()
                self.dict.pop(key)
            node=Node(data)
            self.dict[key]=node
            self.list.preappend(node)


