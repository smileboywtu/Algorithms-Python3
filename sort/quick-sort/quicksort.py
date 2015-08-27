# show title
print """

quicksort

"""
# using func to apply this
def partition(v, lo, hi):
	"partition for quick sort"
	pivot = v[hi]
	arrayindexes = range(lo, hi, 1)
	biggersubarrayindex = lo
	for arrayindex in arrayindexes:
		if v[arrayindex] > pivot:
			v[arrayindex], v[biggersubarrayindex] = v[biggersubarrayindex], v[arrayindex]
			# move forward
			biggersubarrayindex += 1

	# proper location for pivot
	v[hi], v[biggersubarrayindex] = v[biggersubarrayindex], v[hi]
	return biggersubarrayindex

# quick sort
def quicksort(v, lo, hi):
	"quick sort recursively"
	if lo < hi:
		partindex = partition(v, lo, hi)
		print "partindex is: ", partindex, "the current list is: ", v
		quicksort(v, lo, partindex-1)
		quicksort(v, partindex+1, hi)

# program body
array = [23, 45, 67, 79, 1, 34, 2, 5, 89, 17]
print "source array list is: ", array

quicksort(array, 0, len(array)-1)
print "after using quick sort, the list is: ", array

# notify the user
print "Good Bye."


