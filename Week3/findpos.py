def findpos(l,v):
	(found,i) = (False,0)
	while i < len(l):
		if l[i] == v:
			(found,pos) = (True,i)
		i+=1
	if not found:
		pos = -1
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
