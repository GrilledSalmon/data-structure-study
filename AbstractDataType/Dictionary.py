grades = {}

# key-value 데이터 삽입
grades["윤우"] = 100
grades["석희"] = 95
grades["경희"] = 100
grades["도나"] = 94
grades["창민"] = 80

print(grades)


# 한 key에 여러 value 저장 시도 -> 수정이 된다.
grades["창민"] = 85

print(grades)


# key를 이용해서 value 탐색
print(grades["윤우"])
print(grades["석희"])


# key를 이용한 삭제
print(grades.pop("창민"))
print(grades.pop("도나"))

print(grades)
