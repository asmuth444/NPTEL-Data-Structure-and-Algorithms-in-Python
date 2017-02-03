def divides(m,n):
	if m%n==0:
		return True
	else:
		return False

m,n = map(int, raw_input("Enter Two Nos.:").split())
print divides(m,n)
