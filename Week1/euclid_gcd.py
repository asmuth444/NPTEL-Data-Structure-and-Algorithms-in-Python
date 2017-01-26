def gcd(m,n):
	if m<n:
		(m,n)=(n,m)
	if m%n is 0:
		return n
	else:
		diff = m-n
		return gcd(max(n,diff),min(n,diff))

m,n = map(int, raw_input("Enter two 2 nos.:").split())
print gcd(m,n)
