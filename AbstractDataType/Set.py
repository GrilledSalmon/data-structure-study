finished_class = set()

# 데이터 저장
finished_class.add("자료 구조")
finished_class.add("알고리즘")
finished_class.add("프로그래밍 기초")
finished_class.add("머신 러닝")
finished_class.add("데이터 사이언스")

print(finished_class)


# 중복 데이터 저장 시도
finished_class.add("자료 구조")
finished_class.add("알고리즘")

print(finished_class)


# 데이터 탐색
print('자료 구조' in finished_class)
print('자바스크립트 기초' in finished_class)


# 데이터 삭제
finished_class.remove('자료 구조')
finished_class.remove('머신 러닝')

print(finished_class)