from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("윤우")
queue.append("석희")
queue.append("민정")
queue.append("태범")
queue.append("경희")

print(queue)

# 큐의 맨 앞 데이터에 접근
print(queue[0])
print(queue[1])

# 큐의 맨 앞 데이터 삭제 및 리턴
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue)