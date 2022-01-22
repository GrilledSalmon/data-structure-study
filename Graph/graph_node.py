# 노드 구현하기 211213

class StationNode:
    """지하철 역 노드를 나타내는 클래스"""
    def __init__(self, name, num_exits):
        self.name = name
        self.num_exits = num_exits

# 지하철 역 노드 인스턴스 생성
# head node, root node, 그래프에서는 모든 노드가 공평한 위치
station_0 = StationNode("교대역", 14)
station_1 = StationNode("사당역", 14)
station_2 = StationNode("종로3가역", 16)
station_3 = StationNode("서울역", 16)

# 노드들을 파이썬 리스트에 저장
# 얘를 통해 각 노드에 고유한 index가 배정되기 때문에 각 노드에 바로 접근 가능
stations = [station_0, station_1, station_2, station_3]

# 딕셔너리를 이용해 역 이름을 가지고 바로 노드에 접근 가능
# but, key가 겹치지 않도록 주의해야 함.
stations2 = {
    "교대역" : station_0,
    "사당역" : station_1,
    "종로3가역" : station_2,
    "서울역" : station_3
}

node_1 = stations["교대역"]
node_2 = stations["서울역"]