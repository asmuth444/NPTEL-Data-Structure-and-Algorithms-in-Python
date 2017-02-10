def descending(seq):
	if seq == []:
		return(True)
	for i in range(len(seq)-1):
		if seq[i] < seq[i+1]:
			return(False)
	else:
		return(True)

def alternating(seq):
	if seq == []:
		return(True)
	flag = True
	if seq[0]<seq[1]:
		flag = False
	for i in range(1,len(seq)-1,2):
		if (flag and seq[i]>=seq[i+1])or(not flag and seq[i]<=seq[i+1]):
			return(False)
	else:
		return(True)

def matmult(mat1,mat2):
	(temp,mat) = ([],[])
	for i in range(len(mat1)):
		for j in range(len(mat2[0])):
			total = 0
			for k in range(len(mat2)):
				total += mat1[i][k]*mat2[k][j]
			temp.append(total)
		mat.append(temp)
		temp = []
	return(mat)
