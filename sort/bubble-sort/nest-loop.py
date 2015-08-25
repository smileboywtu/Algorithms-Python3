# use the nest loop
# here we will use the bubble sort algorithm

# show the title
print """

using the nest class in python

tips:
    1. You always need to deal with the code block.
    2. Know more about the bubble sort.

"""

# program body
print """
    here we will test the source list:
        [1, 5, 9, 20, 4, 89, 56, 80, 23, 14, 25]

"""
numbers = [1, 5, 9, 20, 4, 89, 56, 80, 23, 14, 25]
lens = len(numbers)
indexs = range(lens)
counter = 0;        # use this counter to record the times

for i in indexs:
    for j in range(lens - i - 1) :
        # here we will test index j with index j+1
        if numbers[j] > numbers[j+1]:   # this means we need to swap the data
            # try to use the bit operator
            numbers[j] = numbers[j] ^ numbers[j+1]
            numbers[j+1] = numbers[j] ^ numbers[j+1]
            numbers[j] = numbers[j] ^ numbers[j+1]
    else:
        counter += 1
        print "this is the ", counter, " times."
        print "the processed list is: ", numbers
    # here you need to check if need to sort again
    # you may not to sort it when the number is very large
    if all(numbers[k] <= numbers[k+1] for k in range(lens - 1)):
        # just break
        break;

# give some information to the user
print "\n"
print "use ", counter, " times to sort the list."
print "sorted done.\n"

# show the result
print "The sorted list is: ", numbers

##################################################################
## this is the output

##using the nest class in python
##
##tips:
##    1. You always need to deal with the code block.
##    2. Know more about the bubble sort.
##
##
##
##    here we will test the source list:
##        [1, 5, 9, 20, 4, 89, 56, 80, 23, 14, 25]
##
##
##this is the  1  times.
##the processed list is:  [1, 5, 9, 4, 20, 56, 80, 23, 14, 25, 89]
##this is the  2  times.
##the processed list is:  [1, 5, 4, 9, 20, 56, 23, 14, 25, 80, 89]
##this is the  3  times.
##the processed list is:  [1, 4, 5, 9, 20, 23, 14, 25, 56, 80, 89]
##this is the  4  times.
##the processed list is:  [1, 4, 5, 9, 20, 14, 23, 25, 56, 80, 89]
##this is the  5  times.
##the processed list is:  [1, 4, 5, 9, 14, 20, 23, 25, 56, 80, 89]
##
##
##use  5  times to sort the list.
##sorted done.
##
##The sorted list is:  [1, 4, 5, 9, 14, 20, 23, 25, 56, 80, 89]