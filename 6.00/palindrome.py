
def isPalindrome(x):
	if len(x) <=1:
		return True
	elif x[0] == x[-1]:
		return isPalindrome(x[1:-1])
	else:
		return False

x = input("Give a String to check if it's a Palindrome or not : ")

ans = isPalindrome(x)
if ans == True:
	print (str(x) +  " is a Palindrome")
else:	
	print (str(x) + " is not a Palindrome")


