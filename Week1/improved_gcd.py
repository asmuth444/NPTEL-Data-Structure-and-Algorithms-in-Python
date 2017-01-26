def gcd(m,n):
	cf = 1
	for i in range(min(m,n)+1,1,-1):
		if m%i is 0 and n%i is 0:
			cf = i
			break
	return cf

m,n = map(int, raw_input("Enter two nos.:").split())
print gcd(m,n)	 
