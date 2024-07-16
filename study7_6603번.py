def lotto(arr, num, a): # arr: 선택한 번호 저장 배열, num: 가능한 숫자가 있는 리스트, a: 현재까지 선택된 숫자의 개수
	# 숫자가 6개이면 그대로 출력
	if a == 6:
		print(*arr[:6])
		return

	# 가능한 숫자들을 순회하면서 arr에 추가
	for i in range(len(num)):
		arr[a] = num[i] 
		lotto(arr, num[i+1:], a+1) # 선택된 숫자를 제외한 나머지 숫자로 다시 조합

while True: # 입력 계속 받기
	num = list(map(int, input().split())) # 입력한 숫자들을 공백으로 구분하여 리스트로 변환
	if num[0] == 0: # 입력한 첫 번째 숫자가 0이면 종료
		break
	arr = [0, 0, 0, 0, 0, 0, 0] # 배열 초기화
	lotto(arr, num[1:], 0) # 첫 번째 숫자를 제외하고 나머지 숫자들로 lotto함수 호출
	print() #각 테이트 케이스 사이에 빈 줄 하나 출력
