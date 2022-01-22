class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""
        
        # 삭제할 노드가 마지막 남은 노드인 경우
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        
        # 삭제할 노드가 head인 경우 
        elif node_to_delete is self.head:
            self.head = node_to_delete.next
            self.head.prev = None
            
        # 삭제할 노드가 tail인 경우
        elif node_to_delete is self.tail:
            self.tail = node_to_delete.prev
            self.tail.next = None
        
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
        
        return node_to_delete.data

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있는 경우
        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, previous_node, data):
        """링크드 리스트 삽입 연산 메소드"""
        # 코드를 쓰세요
        new_node = Node(data)
        
        # 마지막 노드에 삽입하는 경우
        if previous_node is self.tail:
            self.append(data)
        
        else:
            new_node.next = previous_node.next
            new_node.prev = previous_node
            
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)
        
        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def find_node_at(self, index) -> int:
        """링크드 리스트 접근 연산 메소드. 인덱스 리턴. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next
        
        return iterator

    def find_node_with_data(self, data) -> object:
        """링크드 리스트 데이터 탐색 메소드. 해당 노드가 없으면 None을 리턴"""
        iterator = self.head
        
        while iterator is not None:
            if iterator.data == data:
                break                
            iterator = iterator.next
        
        return iterator


    def __str__(self) -> str:
        """프린트했을 때 링크드 리스트의 내용을 잘 확인할 수 있도록"""
        res_str = '|'
        iterator = self.head

        while iterator is not None:
            res_str += f' {iterator.data} |'
            iterator = iterator.next
        
        return res_str


my_list = LinkedList()
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(142)

print(my_list)