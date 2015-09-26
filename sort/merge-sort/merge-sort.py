# this progrma will implement the merge sort
# keep care of using python 3.5

def arraycopy(to, start, end, source):
    "copy the array"
    for index in range(start, end):
        to[index] = source[index]

def mergeparts(v, start, middle, end, work):
    "merge the two part into one in array v"
    ipart1 = start;
    ipart2 = middle;
    for index in range(start, end):
        if ipart1 < middle and (ipart2 >= end or v[ipart1] <= v[ipart2]):
            work[index] = v[ipart1]
            ipart1 += 1
        else:
            work[index] = v[ipart2]
            ipart2 += 1

def top2bottom(v, start, end, work):
    "top to bottom mode recursive"
    if(end - start >= 2):
        imiddle = (start + end)//2;
        # split the array
        top2bottom(v, start, imiddle, work)
        top2bottom(v, imiddle, end, work)
        # merge two part
        mergeparts(v, start, imiddle, end, work)
        # copy the sort array
        arraycopy(v, start, end, work)

def mergesort(v, n, work):
    "merge sort"
    top2bottom(v, 0, n, work)


print("""
    Merge sort
        implement using python 3.5
        top-bottom mode.
""")

# sort the list
array = [1, 4, 89, 67, 90, 34, 56, 23, 15, 48]
work = list(range(len(array)))

print("souce array: ", array)

# use the merge sort
mergesort(array, len(array), work)

print("after using merge sort: ", array)

input("\n\nPress enter to exit.")
