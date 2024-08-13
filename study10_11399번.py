# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하려면 인출 시간이 적은 순으로 정렬하면 된다.

n = int(input()) # 대기하는 사람 수
peoples = list(map(int, input().split())) # 각 사람이 기다려야하는 시간을 리스트 형태로 입력 받기

peoples.sort() #대기 시간 오름차순으로 정렬

result = 0 # 초기화

for i in range(1, n+1): # 1~n
	result += sum(peoples[0:i]) # 첫번째 사람부터 i번째 사람까지 현재 대기 시간 합계를 result에 더하기
print(result)
