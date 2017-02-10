def binary_search(s,v,l,r):
	if r-l==0:
		return(False)
	
	mid = (l+r)//2
	if v == s[mid]:
		return(True)
	elif v > s[mid]:
		return(binary_search(s,v,mid,r))
	else:
		return(binary_search(s,v,l,mid))
			

def main():
	l = list(map(int,input("Enter some numbers: ").split()))
	v = int(input("Enter no. to be found: "))
	l.sort()
	res = binary_search(l,v,0,len(l))
	print("Found "+str(v) if res else "Not Found "+str(v))


main()
