# this program show you the selection sort
print """

	selection sort.

"""

# function for selection sort.
def selectionsort(v, n):
	" selection sort"
	indexes = range(0, n, 1)
	for index in indexes:
		j = index				# this is the start index to search
		while j < n:
			if v[index] < v[j]:
				# swap
				v[index], v[j] = v[j], v[index]
			j = j + 1
		print "for index ", index, "the current list is: ", v

# program body
array = [1, 4, 7, 5, 8, 3]
print "source list: ", array

selectionsort(array, len(array))

print "after sort: ", array

# notify the user
print "Good Bye."
