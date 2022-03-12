import itertools as it

def rev(a, i, j):
	c = j - i + 1
	l = ((j - i) // 2) if (j - i) % 2 == 0 else ((j - i) // 2) + 1

	for k in range(l):
		a[i + k], a[j - k] = a[j - k], a[i + k]

	return c, a

def revsort(a):
	n = len(a)
	count = 0
	for i in range(n - 1):
		j = i
		for k in range(i, n):
			if a[k] < a[j]:
				j = k
		a = rev(a, i, j)
		count += a[0]
		a = a[1]
	# print("revsort() returned", count, "for", a)
	return count

T = int(input())

for t in range(1, T + 1):
	N, C = map(int, input().split())

	p = it.permutations([n for n in range(1, N + 1)])
	# parr = [per for per in p]
	ans = ""
	
	for per in p:
		per = list(per)
		if C == revsort(per[:]):
			ans = per
			break

	print("Case #{}: {}".format(t, "IMPOSSIBLE" if ans == "" else " ".join(map(str, ans))))
