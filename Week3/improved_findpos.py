def findpos(l,v):
	if v not in l:
		return(-1)
	pos = 0
	for i in l:
		if i == v:
			break
		pos+=1
	"""
	else: #You can have a else for a loop too!!!
		pos = -1
	"""
	return(pos) 

def main():
	l = list(map(int,input("Enter some numbers: ").split()))
	v = int(input("Enter no. to be found: "))
	pos  = findpos(l,v)
	if pos == -1:
		print(str(v)+" Not found")
	else:
		print(str(v)+" is at index position "+str(pos+1))

main()
