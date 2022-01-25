# BFS를 활용한 최단경로

from collections import deque
from subway_graph import *
import os

def bfs(graph, start_node):
    """최단 경로용 bfs 함수"""
    queue = deque()  # 빈 큐 생성

    # 모든 노드를 방문하지 않은 노드로 표시, 모든 predecessor는 None으로 초기화
    for station_node in graph.values():
        station_node.visited = False
        station_node.predecessor = None

    # 시작점 노드를 방문 표시한 후 큐에 넣어준다
    start_node.visited = True
    queue.append(start_node)
    
    while queue:  # 큐에 노드가 있을 때까지
        current_station = queue.popleft()  # 큐의 가장 앞 데이터를 갖고 온다
        for neighbor in current_station.adjacent_stations:  # 인접한 노드를 돌면서
            if not neighbor.visited:  # 방문하지 않은 노드면
                neighbor.visited = True  # 방문 표시를 하고
                queue.append(neighbor)  # 큐에 넣는다
                neighbor.predecessor = current_station


def back_track(destination_node):
    """최단 경로를 찾기 위한 back tracking 함수"""
    res = deque()
    now_node = destination_node
    while now_node: # predecessor가 없어서 None이 할당되면 끝
        res.appendleft(now_node.station_name)
        now_node = now_node.predecessor
    return ' '.join(res)


stations = create_station_graph(os.path.join(os.path.dirname(os.path.realpath(__file__)), "new_stations.txt"))  # stations.txt 파일로 그래프를 만든다

bfs(stations, stations["을지로3가"])  # 지하철 그래프에서 을지로3가역을 시작 노드로 bfs 실행
print(back_track(stations["강동구청"]))  # 을지로3가에서 강동구청역까지 최단 경로 출력
