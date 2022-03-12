import itertools as it

def rev(a, i, j):
	c = j - i + 1
	l = ((j - i) // 2) if (j - i) % 2 == 0 else ((j - i) // 2) + 1

	for k in range(l):
		a[i + k], a[j - k] = a[j - k], a[i + k]

	return c, a

N = int(input("Enter name :- "))
arr = [i for i in range(1, N + 1)]
for i in range(N - 1, 0, -1):
	rev(arr, 0, i)

print(arr)

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

li = []

def toString(t):
	return "{} --> {}".format(t[0], t[1])

for per in it.permutations(arr):
	per = list(per)
	cost = revsort(per[:])
	# print(per, "-->", cost)

	li.append((cost, per))

print()
li.sort()
for ppp in li:
	print(toString(ppp))
print()

arr.sort()
print()
print(arr)
new = [0 for i in arr]
end = len(arr) - 1
start = 0
for i in arr:
	if i % 2 == 1:
		new[end] = i
		end -= 1
	else:
		new[start] = i
		start += 1

print(revsort(new[:]), "-->", new)

# print(revsort(arr))

# T = int(input())

# for t in range(1, T + 1):
# 	N, C = map(int, input().split())

# 	p = it.permutations([n for n in range(1, N + 1)])
# 	# parr = [per for per in p]
# 	ans = ""
	
# 	for per in p:
# 		per = list(per)
# 		if C == revsort(per[:]):
# 			ans = per
# 			break

# 	print("Case #{}: {}".format(t, "IMPOSSIBLE" if ans == "" else " ".join(map(str, ans))))
