print "achin"

def sqrt(x):
	""" inputs a non negative integer and returns the square root of it
	"""
	if x<0:
		print ("Give a non negative integer")
		return None
	else:
		i = 0
		while i**2 <= x:
			if i**2 == x:
				return i
			else:
				i += 1
		print (str(x) + " is not a perfect square")

x = int(input("Please enter a postitive integer : "))
# print (sqrt(x))
ans = sqrt(x)

if ans != None:
	pt = ("{} is the root of {}").format(ans, x)
	print (pt)
