import sys
input = sys.stdin.readline

t = int(input()) #테스트 케이스 수 입력

for i in range(t): #각 테스트 케이스에 대해 반복
	n, m = map(int, input().split()) #n, m 입력 받기
	for j in range(m): # m개 간선에 대해 반복
		a, b = map(int, input().split()) # a,b 입력 받기
	print(n - 1) # 출력값
