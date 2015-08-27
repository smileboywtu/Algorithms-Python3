#Introduction
>   quick sort algorithm almost the best sort algorithm because it save time and space.magically you need not to try to sort the array, it will done automatically if you just know about the key idea of this sort algorithm.

#Description
>   we start a example here to see more detail.

>## Example

>>  **Array: [23, 45, 67, 79, 1, 34, 2, 5, 89, 17].**

>## Details

>>  **I**.  firstly, find a pivot in the array, choose the first, middle, last element in the array is a good way.here we just choose last one 17.

>>  **II**. make the array into two part, one is bigger than 17, the other is smaller than 17.
>>
>>> part1>[23, 45, 67, 79, 34, 89]
>>>
>>> part2>[1, 2, 5]

>> **III**. just look up at the two part you will find between the two part is the final location of element 17, which is the pivot.

>>> part1->pivot(17)->part2

>> **IV**.  repeat the above steps for part1 and part2 respectively.

>## Code Python

>>  this is confusing, you may need some time to read carefully about it.

>>  look at the partition: 
>>  
        def partition(v, lo, hi)
            "divide the source list into two part."
            pivot = v[hi]   # set the pivot
            arrayindexes = range(0, hi, 1)
            biggersubarrayindex = lo
            for arrayindex in arrayindexes:
                if v[arrayindex] > pivot:
                    v[arrayindex], v[biggersubarrayindex] = v[biggersubarrayindex], v[arrayindex]
                    biggersubarrayindex += 1
            # final location of pivot
            v[hi], v[biggersubarrayindex] = v[biggersubarrayindex], v[hi]
            return biggersubarrayindex
            
>> quick sort:
>>
        def quicksort(v, lo, hi):
            "use recursive method"
            if lo < hi:
                partindex = partition(v, lo, hi)
                quicksort(v, lo, partindex-1)
                quicksort(v, partindex+1, hi)
                
>>  keep care of lo and hi, they are array index not the length.

>## Test

>>  use the following code to test:
>>
        print "partindex is: ", partindex, "the current list is: ", v
        
>## Result

>>  source array list is:  [23, 45, 67, 79, 1, 34, 2, 5, 89, 17]

>>  partindex is:  6 the current list is:  [23, 45, 67, 79, 34, 89, 17, 5, 1, 2]

>>  partindex is:  0 the current list is:  [89, 45, 67, 79, 34, 23, 17, 5, 1, 2]

>>  partindex is:  5 the current list is:  [89, 45, 67, 79, 34, 23, 17, 5, 1, 2]

>>  partindex is:  4 the current list is:  [89, 45, 67, 79, 34, 23, 17, 5, 1, 2]

>>  partindex is:  1 the current list is:  [89, 79, 67, 45, 34, 23, 17, 5, 1, 2]

>>  partindex is:  3 the current list is:  [89, 79, 67, 45, 34, 23, 17, 5, 1, 2]

>>  partindex is:  8 the current list is:  [89, 79, 67, 45, 34, 23, 17, 5, 2, 1]

>>  after using quick sort, the list is:  [89, 79, 67, 45, 34, 23, 17, 5, 2, 1]

>>  Good Bye.
    
                