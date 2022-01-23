import os
from collections import deque
from subway_graph import *

# self.visited -> 한 번도 본적 없을 때: 0, 스택에 있을 때: 1, 발견된 상태: 2

def dfs(graph, start_node):
    """dfs 함수"""
    stack = deque()  # 빈 스택 생성

    # 모든 노드를 처음 보는 노드로 초기화
    for station_node in graph.values():
        station_node.visited = 0

    # 코드를 쓰세요
    stack.append(start_node)
    start_node.visited = 1 # 스택에 들어갔다 표시
    
    while stack: # stack에 무언가 들어있는 동안
        now_node = stack.pop() # 스택의 맨 위 노드 꺼내기
        now_node.visited = 2 # 노드 방문했다 표시
        for adj_node in now_node.adjacent_stations:
            if not adj_node.visited: # 방문한 적도 없고 stack에 들어간 적도 없다면
                stack.append(adj_node) # stack에 새로운 노드 넣기
                adj_node.visited = 1 # stack에 들어가본 노드를 1이라 표시


stations = create_station_graph(os.path.join(os.path.dirname(os.path.realpath(__file__)), "new_stations.txt"))  # stations.txt 파일로 그래프를 만든다


gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
dfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)

