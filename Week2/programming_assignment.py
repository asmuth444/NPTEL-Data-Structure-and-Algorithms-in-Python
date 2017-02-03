def intreverse(n):
	sum = 0
	while n>0:
		sum = sum*10 + n%10
		n = n//10
	return(sum)
			

def matched(s):
	count1 = 0
	count2 = 0
	for i in xrange(len(s)):
		if s[i]=='(':
			count1+=1
		elif s[i]==')':
			count2+=1
		if count2>count1:
			return(False)
	if count1 == count2:
		return(True)
	else:
		return(False)

def sumprimes(l):
	sum = 0
	for i in l:
		if i>0 and isPrime(i):
			sum += i
	return(sum)

def isPrime(n):
	if n is 1:
		return(False)
	for i in range(2,n):
		if n%i == 0: return(False)
	return(True)	
