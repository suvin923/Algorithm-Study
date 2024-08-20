name = input()

count = {} # 문자의 개수를 저장할 딕셔너리 초기화 # 딕셔너리는 키(key)와 값(value)의 쌍으로 이루어진 자료 구조
keys = sorted(set(name))
arr = [] # 홀수 개수의 문자를 저장할 리스트 초기화
for key in keys:
	cnt = name.count(key) # name에서 현재 문자 key개수 세기
	count[key] = cnt # 문자 개수 count에 저장
	if cnt % 2: # 문자의 개수가 홀수일때
		arr.append(key) # arr 리스트에 추가

if len(arr) > 1: # arr리스트에 있는 문자의 개수가 1개 초과일 때 ex) AAAABC, ABC
	print("I'm Sorry Hansoo")
else:
	result = '' # 결과를 저장할 빈 문자열 초기화
	
	for key in keys:
		result += key * (count[key] // 2) # 문자의 절반만 앞부분만 추가하기
		
	if arr: # arr리스트가 비어 있지 않은 경우 == 홀수 개 문자가 하나 있는 경우
		result += arr[0] + result[::-1] # 중간에 홀수 개 문자 넣고 팰린드롬 만들기
	else: # arr리스트가 비어 있는 경우 == 모든 문자가 짝수개인 경우
		result += result[::-1] # 팰린드롬 만들기
		
	print(result)
