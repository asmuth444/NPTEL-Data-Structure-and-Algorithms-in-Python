def merge(l1,l2):
	(l3, m, n) = ([], len(l1), len(l2))
	(i, j) = (0, 0)
	while i+j < m+n:
		if i == m:
			l3.append(l2[j])
			j += 1
		elif j == n:
			l3.append(l1[i])
			i += 1
		elif l1[i] <= l2[j]:
			l3.append(l1[i])
			i += 1
		elif l1[i] > l2[j]:
			l3.append(l2[j])
			j += 1
	return(l3)

def mergesort(seq, l, r):
	if r-l <= 1:
		return(seq[l:r])
	if r-l > 1:
		mid = (l+r)//2
		l = mergesort(seq, l, mid)
		r = mergesort(seq, mid, r)
		return(merge(l, r))
	

def main():
	seq = list(map(int,input("Enter some nos: ").split()))
	print("Your merged sorted list: "+" ".join(map(str,mergesort(seq, 0, len(seq)))))

main()
