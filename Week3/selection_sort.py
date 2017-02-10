def selection_sort(l):
	for start in range(len(l)):
		minpos = start
		for i in range(start,len(l)):
			if l[i] < l[minpos]:
				minpos = i
		(l[start], l[minpos]) = (l[minpos], l[start])
	

def main():
	l = list(map(int,input("Enter some no.: ").split()))
	selection_sort(l)
	print(" ".join(list(map(str,l))))

main()
