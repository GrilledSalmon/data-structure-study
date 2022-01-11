# Chaining을 이용한 hash table

class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def find_node_with_key(self, key):
        """입력받은 key를 가지고 링크드 리스트 중에 해당 key를 가지고 있는 노드를 찾아 리턴. 만약 만족하는 노드가 없다면 None 리턴 """
        iterator = self.head

        while iterator is not None:
            if iterator.key == key:
                return iterator

            iterator = iterator.next

        return None

    def append(self, key, value):
        """링크드 리스트 추가 연산 메소드. 맨 뒤에 노드 추가"""
        new_node = Node(key, value)

        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, node_to_delete):
        """삭제할 노드를 받아 해당 노드 삭제"""

        # node_to_delete가 마지막 남은 노드일 경우
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None

        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    def __str__(self) -> str:
        res_str = ''

        iterator = self.head

        while iterator is not None:
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next
        
        return res_str


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.append('윤우', 28)
    my_list.append('석희', 26)
    my_list.append('경희', 31)

    print(my_list)
