class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스

# 데이터 2, 3, 5, 7, 11을 담는 노드 생성

head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

# 노드들을 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

# 노드 순서대로 출력
iterator = head_node

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next


print('=======================================================')
print('링크드 리스트 클래스 만들기')

class LinkedList:
    """링크드 리스트 클래스"""
    
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 삽입 연산 메소드
        주어진 노드 뒤에 삽입되기 때문에 이 메소드로 head 앞에 삽입할 순 없다."""
        new_node = Node(data)
        
        # tail 노드 다음에 삽입하는 경우
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node
    
    def delete_after(self, previous_node):
        """링크드 리스트 삭제연산. 주어진 노드 뒤 노드 삭제하고, 그 뒤 노드를 연결"""
        
        data = previous_node.next.data

        # tail node를 지울 때
        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node

        # 두 노드 사이 노드를 지울 때
        else:
            # 끊어진 노드는 생각할 필요 없음
            previous_node.next = previous_node.next.next

        return data


    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정"""
        data = self.head.data
        
        # 링크드 리스트에 헤드만 있는 경우
        if self.head.next is None:
            self.head = None
            self.tail = None
            
        else:
            self.head = self.head.next
            
        return data

    
    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)
        
        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.tail = new_node
        
        else:
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
    
    def append(self, data):
        """링크드 리스트의 맨 끝(tail)에 값을 추가하는 operation"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # 링크드 리스트가 채워져 있는 경우
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self) -> str:
        """프린트했을 때 링크드 리스트의 내용을 잘 확인할 수 있도록"""
        res_str = '|'
        iterator = self.head

        while iterator is not None:
            res_str += f' {iterator.data} |'
            iterator = iterator.next
        
        return res_str

        

# 작동 확인
# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

# 링크드 리스트 출력
iterator = my_list.head

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

print(my_list)


print('=======================================================')
print('접근 메소드 작동 확인')
print(my_list.find_node_at(3).data)
my_list.find_node_at(2).data = 13
print(my_list)


print('=======================================================')
print('insert 메소드 작동 확인')
temp_node = my_list.find_node_at(3)
my_list.insert_after(temp_node, 100)
print(my_list)

print('=======================================================')
print('delete 메소드 작동 확인')
print('지워진 데이터 :', my_list.delete_after(my_list.find_node_at(3)))
print(my_list)