n = int(input())
user = [] #빈 리스트
for i in range(n):
	age, name = input().split() # 나이와 이름 입력받기
	user.append([int(age),name]) # [나이, 이름] 리스트로 만들어 user에 추가
	
user.sort(key=lambda x:int(x[0])) #리스트를 나이 순으로 정렬, x[0]은 나이를 의미
	
for i in range(n):
	print(user[i][0], user[i][1]) 
  
<Tip>
sort는 원래 리스트를 정렬하고, sorted는 새로운 정렬된 리스트를 반환
