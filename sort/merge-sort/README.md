# Merge sort
> this algorithm implement the merge sort .

# Description

> Divide the unsorted list into n sublists, each contaioning 1 element.

> Repeatedly merge sublists to produce new sorted sublists until there is only one sublists remaining.

## Example

>> [1, 4, 89, 67, 90, 34, 56, 23, 15, 48]

>> **I**. Divide the unsorted list into sublists:

>>> [1], [4], [89], [67], [90], [34], [56], [23], [15], [48]

>> **II**. Merge the sublists:

>>> merge sublist: [1] and [4]: [1, 4]

>>> merge sublist: [89] and [67]: [67, 89]

>>> merge sublist: [90] and [34]: [34, 90]

>>> merge sublist: [56] and [33]: [33, 56]

>>> merge sublist: [15] and [48]: [15, 48]

>>> ***Next***

>>> merge sublist: [1, 4] and [67, 89]: [1, 4, 67, 89]

>>> **...**

### Code python

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

## Test
> Show the output

    smile@sumsung...merge-sort: python3 merge-sort.py

    Merge sort
        implement using python 3.5
        top-bottom mode.

    souce array:  [1, 4, 89, 67, 90, 34, 56, 23, 15, 48]
    after using merge sort:  [1, 4, 15, 23, 34, 48, 56, 67, 89, 90]
