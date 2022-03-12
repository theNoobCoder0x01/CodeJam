import sys

T, N, Q = map(int, input().split())
sys.stderr.write("T = {} N = {} Q = {}\n".format(T, N, Q))
for t in range(1, T + 1):
	arr = [i for i in range(1, N + 1)]
	# print(arr)
	qresults = []
	# qresultsr = []

	# i = 1
	s, e = 0, 3
	Q = [[arr[i] for i in range(s, e)]]
	while len(Q) > 0:
		q = Q.pop()
		print(" ".join(map(str, q)), flush=True)
		sys.stderr.write("{}\n".format(" ".join(map(str, q))))
		med = int(input())
		sys.stderr.write("med = {}\n".format(med))

		if med == q[0]:
			q[0], q[1] = q[1], q[0]
		elif med == q[2]:
			q[1], q[2] = q[2], q[1]

		qresults.append(q)
		# qresultsr.append(q[::-1])
		s, e = s + 1, e + 1
		if e < N + 1:
			Q.append([arr[i] for i in range(s, e)])

	# print(qresults)

	out = qresults.pop(0)
	while len(qresults) > 0:
		q = qresults.pop(0)
		# print("q =", q)
		if q[1] not in out:
			j = 0
			while out[j] not in q:
				j += 1
			else:
				temp = out[:j+1] + [q[1]] + out[j+1:]
				# print("qqq =", q)
				# print("out =", out)
				# print("temp =", temp)
				out = temp[:]
		else:
			j = 0
			while out[j] != q[0]:
				j += 1
			k = 0
			while out[k] != q[1]:
				k += 1
			if j > k:
				temp = out[:k] + [q[2]] + out[k:]
				# print("qqq(j>k) =", q)
				# print("out(j>k) =", out)
				# print("temp(j>k) =", temp)
				out = temp[:]
			else:
				out.append(q[2])

	print(" ".join(map(str, out)), flush=True)
	sys.stderr.write("{}\n".format(" ".join(map(str, out))))
	ans = int(input())
	sys.stderr.write("{}\n".format(ans))