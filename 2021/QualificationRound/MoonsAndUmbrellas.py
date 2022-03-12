T = int(input())

for t in range(1, T + 1):
	x, y, s = input().split()
	x, y = int(x), int(y)
	sc = list(s)

	i, l = 0, len(sc)
	while i < l:
		j = i
		while i < l and sc[i] == '?':
			i += 1
		k = i
		if k == l:
			j -= 1
			k -= 1
			while j < k:
				# print("--", j, k, ".", sc, "--")
				sc[k] = sc[j]
				k -= 1
		else:
			while k > j:
				sc[j] = sc[k]
				j += 1
		i += 1

	i, l, cost = 1, len(sc), 0
	while i < l:
		if sc[i] == 'J' and sc[i - 1] == 'C':
			cost += x
		elif sc[i] == 'C' and sc[i - 1] == 'J':
			cost += y
		i += 1

	print("Case #{}: {}".format(t, cost))