def recursive_insertion_sort(seq):
	isort(seq,len(seq))

def isort(seq,k):
	if k>1:
		isort(seq,k-1)
		insert(seq,k-1)

def insert(seq,k):
	pos = k
	while pos > 0 and seq[pos] < seq[pos-1]:
		(seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
		pos -= 1
	
def main():
	seq = list(map(int,input("Enter some no. : ").split()))
	recursive_insertion_sort(seq)
	print(" ".join(map(str,seq)))

main()
