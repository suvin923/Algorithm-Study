n = int(input()) # 컴퓨터 개수
v = int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] # 각 컴퓨터가 연결된 다른 컴퓨터들을 저장하기 위한 리스트 생성

for i in range(v): # 그래프 생성
	a, b = map(int, input().split())
	graph[a].append(b) # a에 b 연결
	graph[b].append(a) # b에 a 연결 -> 양방향
visited = [False] * (n+1) # 방문한 컴퓨터인지 표시, 초기값을 모두 False로 설정

def dfs(x):
	visited[x] = True # 현재 x 컴퓨터 방문함
	for y in graph[x]: # x와 연결된 모든 컴퓨터 y에 대해
		if visited[y] == 0: # 아직 방문하지 않은 컴퓨터가 있으면
			dfs(y) # 해당 컴퓨터를 방문

dfs(1) # 1번 컴퓨터에서부터 DFS를 시작
print(sum(visited)-1) # 방문한 컴퓨터의 개수 - 1번 컴퓨터
