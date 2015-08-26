# this program is the implemention of insert sort.

print """

insert sort.

"""

# use function
def insertsort(v, n):
	"insert sort implemention"
	indexes = range(1, n, 1)  # generate index from 1 to n-1
	for index in indexes:
		itemforinsert = v[index]	# the item will be insert
		loopcounter = index
		while (loopcounter > 0) and (itemforinsert > v[loopcounter-1]):
			# shift right
			v[loopcounter] = v[loopcounter-1]
			loopcounter = loopcounter - 1
		# insert after shift
		v[loopcounter] = itemforinsert
		# test
		print "for ", index, "the list is: ", v

# program body
print "start to test the insert sort: "

array = [23, 45, 56, 2, 13, 89, 34, 14, 9, 1]
print array

# call the insertion sort function
print "test every index: "
insertsort(array, len(array))

print "after sort: "
print array

# notify user good bye
print "Good Bye."	
