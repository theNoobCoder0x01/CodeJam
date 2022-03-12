#CheatingDetection

T = int(input())
P = int(input())

for t in range(1, T + 1):
	answers = []
	for _ in range(100):
		answers.append(input())

	cheater = -1
	maxCorrect = -1
	i = 1

	for player_answers in answers:
		count = player_answers.count('1')
		if (count > maxCorrect):
			cheater = i
			maxCorrect = count
		i += 1

	print(f"Case #{t}: {cheater} --> {maxCorrect}")
