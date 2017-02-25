def quicksort(seq,l,r):
	if r-l<=1:
		return()
	yellow = l+1
	for green in range(l+1,r):
		if seq[green] <= seq[l]:
			(seq[yellow], seq[green]) = (seq[green],seq[yellow])
			yellow += 1
	
	(seq[l], seq[yellow-1]) = (seq[yellow-1], seq[l])
	quicksort(seq, l, yellow-1)
	quicksort(seq, yellow, r)

def main():
	seq = list(map(int, input("Enter some nos. : ").split()))
	quicksort(seq, 0, len(seq))
	print("The sorted list is "+" ".join(map(str, seq)))

main()
