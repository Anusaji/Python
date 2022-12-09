def rangeSum():

	from math import sqrt	

	for number in range(1000, 10000):

		s1, s2 = list(str(number)), ''			

		for i in s1:

			if int(i) % 2 != 0:			

				break

			s2+=i

		if len(s2) == 4:

			if int(str(sqrt(int(s2))).split('.')[1]) == 0:

				print(s2)

rangeSum()
