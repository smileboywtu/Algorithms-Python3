# shell sort

print """
    shell sort. if you want to know more details about the shell sort
please read the README.md.
"""

# shell sort
def shellsort(a, n):
    " shell sort"
    # this gaps from the bater choose.
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        i = gap
        while(i < n):
            temp = a[i]     # save current
            j = i
            while(j > gap and a[j-gap] > temp):
                a[j] = a[j-gap]
                j = j-gap   # swap
            a[j] = temp     # fill the data
            i = i+1


# main fun
l = [1, 34, 23, 56, 87, 2, 67, 45, 5, 21]

# show list
print 'source: '
print l

# sort
shellsort(l, len(l))

#show new list
print 'sort: '
print l
        
