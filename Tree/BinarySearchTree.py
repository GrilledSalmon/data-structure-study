# 이진 탐색 트리

class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None


def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        # 코드를 쓰세요
        temp_node = self.root # root 노드부터 검색 시작
        while True:
            # 비교 대상 노드보다 삽입하려는 노드가 더 작은 경우
            if temp_node.data > data: 
                if temp_node.left_child: # temp_node의 left child가 있는 경우
                    temp_node = temp_node.left_child # 다음 노드로 내려감
                else: # temp_node의 left child가 없는 경우 
                    temp_node.left_child = new_node # 삽입한 데이터 저장
                    new_node.parent = temp_node
                    break
            
            # 삽입하려는 노드가 더 크거나 같은 경우
            else:
                if temp_node.right_child: # right child가 있는 경우
                    temp_node = temp_node.right_child # 다음 노드로 내려감
                else: # right child가 없는 경우
                    temp_node.right_child = new_node # 삽입한 데이터 저장
                    new_node.parent = temp_node
                    break


    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        # 코드를 쓰세요
        temp_node = self.root
        
        while temp_node: # temp_node가 None이 아닐 동안 동작
            if temp_node.data == data: # data를 찾은 경우
                return temp_node
            elif temp_node.data > data: # data가 더 작은 경우
                temp_node = temp_node.left_child
            else: # data가 더 큰 경우
                temp_node = temp_node.right_child
        
        # data를 찾지 못해서 while 문이 끝남
        return None

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 경우 1: 지우려는 노드가 leaf 노드일 때
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if parent_node is None: # node_to_delete가 root 노드인 경우
                self.root = None
            else: # node_to_delete가 root node가 아닌 경우
                if parent_node.left_child: # left_child가 leaf 노드인 경우
                    parent_node.left_child = None
                else: # right_child가 leaf 노드인 경우
                    parent_node.right_child = None

        # 경우 2: 지우려는 노드가 자식이 하나인 노드일 때:
        elif node_to_delete.left_child is None or node_to_delete.right_child is None:
            if node_to_delete is self.root: # 삭제하려는 게 root 노드라면
                if node_to_delete.right_child: # 오른쪽 자식이 살아 있는 경우
                    self.root = node_to_delete.right_child
                    node_to_delete.right_child.parent = None
                else: # 왼쪽 자식이 살아 있는 경우
                    self.root = node_to_delete.left_child
                    node_to_delete.left_child.parent = None
                    
            # 삭제하려는 노드가 left_child가 있는 경우
            elif node_to_delete.left_child:
                # 삭제하려는 노드가 parent_node의 왼쪽 자식인 경우
                if parent_node.left_child is node_to_delete:
                    parent_node.left_child = node_to_delete.left_child
                    node_to_delete.left_child.parent = parent_node
                # 삭제하려는 노드가 parent_node의 오른쪽 자식인 경우
                else:
                    parent_node.right_child = node_to_delete.left_child
                    node_to_delete.left_child.parent = parent_node
            
            # 삭제하려는 노드가 right_child가 있는 경우
            else:
                # 삭제하려는 노드가 parent_node의 왼쪽 자식인 경우
                if parent_node.left_child is node_to_delete:
                    parent_node.left_child = node_to_delete.right_child
                    node_to_delete.right_child.parent = parent_node
                # 삭제하려는 노드가 parent_node의 오른쪽 자식인 경우
                else:
                    parent_node.right_child = node_to_delete.right_child
                    node_to_delete.right_child.parent = parent_node

        # 경우 3: 지우려는 노드가 2개의 자식이 있을 때
        else:
            successor = self.find_min(node_to_delete.right_child) # staticmethod 이렇게 쓰는 거 맞나..?
            node_to_delete.data = successor.data
            
            # successor 부모 노드의 자식 새로 지정하기(successor의 right_child가 있는지 없는지는 여기서 신경쓰지 않아도 된다.)
            # successor가 부모 노드의 right_child인 경우
            if successor.parent.right_child is successor:
                successor.parent.right_child = successor.right_child
            # successor가 부모 노드의 left_child인 경우
            else:
                successor.parent.left_child = successor.right_child
            
            # successor의 right_child가 존재하는 경우
            if successor.right_child:
                successor.right_child.parent = successor.parent
        

    @staticmethod # 정적메소드(인스턴스 없이 사용 가능한 메소드에서 self 없음)
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        # 코드를 쓰세요
        temp_node = node
        while temp_node.left_child: # temp_node의 left_child가 None이 되기 전까지
            temp_node = temp_node.left_child
            
        # while문이 끝났다는 것은 왼쪽 끝(최소)에 도달했다는 얘기
        return temp_node
    

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다


# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
bst.print_sorted_tree()

print(bst.find_min(bst.root).data)  # 전체 이진 탐색 트리에서 가장 작은 노드
print(bst.find_min(bst.root.right_child).data)  # root 노드의 오른쪽 부분 트리에서 가장 작은 노드

print(bst.find_min(bst.root).data)  # 전체 이진 탐색 트리에서 가장 작은 노드
print(bst.find_min(bst.root.right_child).data)  # root 노드의 오른쪽 부분 트리에서 가장 작은 노드