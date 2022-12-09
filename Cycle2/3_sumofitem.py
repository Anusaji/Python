def listSum(l):

	s = 0

	for i in l:

		s+=i

	return s

l = [int(x) for x in input("Enter the Elements :").split(" ")]

print(listSum(l))

	
