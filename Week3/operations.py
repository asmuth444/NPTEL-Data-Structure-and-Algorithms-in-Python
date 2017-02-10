def factorial(n):
	if n==0:
		return(1)
	else:
		return(n * factorial(n-1))

def multiply(m,n):
	if n==1:
		return(m)
	else:
		return(m + multiply(m,n-1))

def length(l):
	if l == []:
		return(0)
	else:
		return(1 + length(l[1:]))

def sumlist(l):
	if l == []:
		return(0)
	else:
		return(l[0] + sumlist(l[1:]) )
