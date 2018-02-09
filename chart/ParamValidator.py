import sys

if 2 > len(sys.argv): # validate file name if user has not entered display error message
	print("Please enter file name")	
	exit()
elif 3 > len(sys.argv):  # validate file size if user has not entered display error message(A4,A3)
	print("Please enter file size")
	exit()
