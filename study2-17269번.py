num = {
	'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4,
	'F': 3, 'G': 1, 'H': 3, 'I': 1, 'J': 1,
	'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1,
	'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2,
	'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2,
	'Z': 1
}

N, M = map(int, input().split())
A, B = input().split()
A = list(A)
B = list(B)

name = []
for i in range(N):
	name.append(A.pop(0))
	if len(B) != 0:
		name.append(B.pop(0))
if len(B) != 0:
	name.extend(B)

for i in range(len(name)):
	name[i] = num[name[i]]

while len(name) != 2:
	for i in range(len(name) - 1):
		name[i] = (name[i] + name[i + 1]) % 10#
	name.pop()

result = int(str(name[0])+str(name[1]))
print(str(result)+'%')
