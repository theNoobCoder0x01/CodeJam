T = int(input())
t = 0
while t < T:
	N = int(input())
	n = 0
	d = dict()
	while (n + 1) < N:
		s = list(map(int, input().split()))
		d[s[0]] = d.get(s[0], []) + [s]
		n += 1

	for i in d.keys():
		d[i].sort(key=lambda x: x[-1])

	l = []
	visited = set()
	ex = 0
	p = 0

	for s in d[1]:
		if s[1] not in visited:
			visited.add(s[1])
			l.append((s[1], s[2]))
		ex += s[2] * s[3]
		p += s[2]

	print(l)
	while len(l) != 0:
		#te = 
		k, np = l.pop(0)#te[0], te[1]
		# print("-_-_-_-", k)
		if k not in d.keys():
			continue
		for s in d[k]:
			tp = min(np, s[2])
			ex += tp * s[3]
			np -= tp
			if s[1] not in visited:
				visited.add(s[1])
				l.append((s[1], np))

	print(d, "--", ex, "--", "**", p, "**")
	t += 1
