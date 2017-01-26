def gcd(m,n):
	mfactor=[]
	nfactor=[]
	cfactor=[]
	for i in range(1,m+1):
		if m%i is 0:
			mfactor.append(i)
	for i in range(1,n+1):
		if n%i is 0:
			nfactor.append(i)
	if len(mfactor)>=len(nfactor):
		sl = nfactor
		ll = mfactor
	else:
		ll = nfactor
		sl = mfactor
	for i in sl:
		if i in ll:
			cfactor.append(i)
	return max(cfactor)

m,n = map(int, raw_input("Enter two nos.: ").split())
print gcd(m,n)
