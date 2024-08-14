# deque(데크)는 양방향으로 추가나 삭제할 수 있는 양방향 큐이다.

from collections import deque

n = int(input())

def find_card(n):
	cards = deque(range(1, n+1)) # 1~n까지 숫자를 가지는 리스트를 만들고 데크로 변환
	
	while len(cards) > 1: # 카드 하나 남을 때까지 반복
		cards.popleft() # 첫 번째 숫자 버리기
		cards.append(cards.popleft()) # 첫 번째 숫자 제거 후 맨 뒤에 추가 
	return cards[0] # 남은 카드 하나 반환

print(find_card(n))
