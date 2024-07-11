def dfs(v):
	visited[v] = 1 #방문함
	next = arr[v] #순열 저장 리스트 arr, 다음 방문할 노드 배열에서 가져오기
	if visited[next] == 0: #방문하지 않음
		dfs(next)
	return

t = int(input())
arr = [0]
for i in range(t):
	cycle = 0
	n = int(input())
	visited = [0] * (n + 1) #방문 여부 기록
	arr = list(map(int, input().split())) #순열 입력받고 리스트에 저장
	arr.insert(0, 0) #순열 리스트의 인덱스를 1부터 시작하기 위해 리스트 첫번째에 0을 삽입
	for j in range(1, n + 1): #각 노드 방분하기 위한 반복문
		if visited[j] == 0: #방문하지 않음
				dfs(j) 
				cycle += 1 
	print(cycle)


(참고)
https://velog.io/@since-1994/%EA%B7%B8%EB%9E%98%ED%94%84-Detection-cycle-%EC%82%AC%EC%9D%B4%ED%81%B4-%EC%B0%BE%EA%B8%B0
DFS(깊이우선탐색)
