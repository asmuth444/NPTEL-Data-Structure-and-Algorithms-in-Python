def insertion_sort(seq):
	for sliceEnd in range(len(seq)):
		pos = sliceEnd
		while pos > 0 and seq[pos] < seq[pos-1]:
			(seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
			pos -= 1

def main():
	seq = list(map(int,input("Enter some no. : ").split()))
	insertion_sort(seq)
	print(" ".join(map(str,seq)))

main()
