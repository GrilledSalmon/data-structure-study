# 파이썬의 '리스트' 추상자료형 사용해보기
trending = []

# 특정 위치에 데이터 삽입
trending.insert(0, "연예인 A씨")
trending.insert(1, "잠실 콘서트")
trending.insert(2, "한국 휴일 수")
trending.insert(3, "추석 음식")
print(trending)

# 리스트 접근 연산
print(trending[0])
print(trending[1])
trending[2] = 4
print(trending)

# in 을 사용한 탐색
print("연예인 A씨" in trending)
print("연예인 B씨" in trending)

# del을 이용한 삭제
del trending[0]
print(trending)