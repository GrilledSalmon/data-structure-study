# Breadth First Search 예시
import os
from collections import deque
from subway_graph import create_station_graph

def bfs(graph, start_node):
    """시작 노드에서 bfs를 실행하는 함수"""
    queue = deque()  # 빈 큐 생성

    # 일단 모든 노드를 방문하지 않은 노드로 표시
    for station_node in graph.values():
        station_node.visited = False
    
    start_node.visited = True
    queue.append(start_node) # 시작 노드를 큐에 넣어줌

    while queue: # 큐가 비어있을 때까지
        now_search_node = queue.popleft() # 이번에 확인할 노드를 큐에서 꺼내줌
        for adjacent_station in now_search_node.adjacent_stations:
            if not adjacent_station.visited: # 방문하지 않았다면
                queue.append(adjacent_station) # 큐에 방문하지 않은 노드 추가
                adjacent_station.visited = True # visited로 바꿔줌

# print(__file__)
# print(os.getcwd())
# print(os.path.realpath(__file__))
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))

stations = create_station_graph(os.path.join(os.path.dirname(os.path.realpath(__file__)), "new_stations.txt"))  # stations.txt 파일로 그래프를 만든다
# stations = create_station_graph(os.path.dirname(os.path.realpath(__file__)) + "/new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
bfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들이 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들이 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)