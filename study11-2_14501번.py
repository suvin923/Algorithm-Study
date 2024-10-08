# DP(다이나믹 프로그래밍): 잎에서 계산한 식을 배열에 미리 저장하여 연산속도를 증가시키는 프로그래밍

#DP의  예: 피보나치 수열
#DP = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ]

#DP[2] == DP[0] + DP[1]
#2

#DP[3]==  DP[1] + DP[2] 
#3

# 뒤부터 계산하는 방식이 시간복잡도가 더 빠르다!!
n = int(input())
t = [0] * (n + 1) # 초기화
p = [0] * (n + 1) # 초기화

for i in range(n):
	a,b = map(int, input().split())
	t[i] = a # t[i]에 작업 시간 저장
	p[i] = b # p[i]에 수익 저장

dp = [0] * (n + 1) # 초기화

for i in range(len(t)-2, -1, -1): # 역순으로 이동하기
	if t[i]+i <= n: # 일할 수 있는 날을 초과하지 않을 경우
		dp[i] = max(p[i] + dp[i + t[i]], dp[i+1]) # 현재 일을 수행하고 그 일을 마친 후 남은 날들에 대해 얻을 수 있는 최대 수익을 더한 값
	else: # 일할 수 있는 날을 초과한 경우
		dp[i] = dp[i+1] # 다음 날의 최대 수익 가져오기
print(dp[0])
