def factors(n):
	factor_list = []
	for i in range(1,n+1):
		if n%i is 0:
			factor_list.append(i)
	return(factor_list)

def isprime(n):
	if len(factors(n)) is 2: return True
	else: return False

def nprimes(n):
	(count,i,plist) = (0,1,[])
	while count<n:
		if isprime(i):
			(count,plist) = (count+1,plist+[i])
		i+=1
	return(plist) 


n = int(input("Enter a no.: "))
print("Factors for "+str(n)+" are: "+" ".join(map(str,factors(n))))
print("Is prime? "+str(isprime(n)))
print("List of "+str(n)+" prime nos.: "+" ".join(map(str,nprimes(n))))

