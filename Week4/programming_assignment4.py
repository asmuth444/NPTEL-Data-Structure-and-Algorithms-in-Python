def orangecap(d):
	players = list(set([j for i in d.keys() for j in list(d[i].keys())]))
	total = []
	for i in players:
		total_score = 0
		for j in list(d.keys()):
			if i in d[j]:
				total_score += d[j][i]
		total.append((total_score,i))
	total.sort()
	return((total[-1][1],total[-1][0]))

def addpoly(p1,p2):
	poly = p1+p2
	exp = list(set([i[1] for i in poly]))
	exp.sort()
	exp.reverse()
	res = []
	for i in exp:
		total = 0
		for j in poly:
			if j[1] == i:
				total += j[0]
		res.append((total,i))
	for i in res:
		if i[0] == 0:
			res.remove(i)
	return res

def multpoly(p1,p2):
	poly = [[(i[0]*j[0],i[1]+j[1]) for j in p2] for i in p1]
	res = []
	for i in poly:
		res = addpoly(res,i)
	for i in res:
		if i[0] == 0:
			res.remove(i)

	return res
