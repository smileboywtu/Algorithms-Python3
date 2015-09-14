
# Binary Search

# show title
print """

	Binary Search

"""

# binary search module
def binsearch(array, find, low, high):
	"low and high are index here."
	if(low < high):
		mid = int((low + high) / 2)
		if(array[mid] == find):
			return mid
		elif(array[mid] > find):
			return binsearch(array, find, low, mid - 1)
		else:
			return binsearch(array, find, mid + 1, high)


# program main body

array = [23, 45, 67, 78, 89, 123, 234, 345, 456, 789]
find = 67

# here we want to find 67
result = binsearch(array, find, 0, len(array)-1)

# show result
print find, " is the ", result, " index of array", array 

# notify user
print "Good Bye."



