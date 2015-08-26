# Introduction
>   Here we just look at the insertion sort using python.this algorithm is very efficient for small data set.
>
# Description
>   we just look at an example for this algorithm.
>   
>## Example
>>  List: [23, 45, 56, 2, 13, 89, 34, 14, 9, 1]
>>  
>>  the list above is an unsorted list here.
>> 
>>  but if we just look at the list only contain one element, like:
>>
>>  **List: [23]**, we can think this list is sorted. so we can divide the source list into two part, sorted subparticial and unsortedparticial.
>>  
>>  **SORTED:   [23]**
>>
>>  **UNSORT:   [45, 56, 2, 13, 89, 34, 14, 9, 1]**
>>
>>  *here we just sort the source array by decreasing order.*
>>
>## Details
>>>  **I**. choose 45 from unsorted sequence, compare it with the last one in the sorted list, here the element is 23.
>>
>>> here because 23<45, so you should to shift 23 right and make a hole for 45 to insert.
>>
>>> after first insert, you will get the sequence is:
>>>
>>> **List:**[45, 23, 56, 2, 13, 89, 34, 14, 9, 1]
>>>
>>> **SORTED:   [45, 23]**
>>>
>>> **UNSORT:   [56, 2, 13, 89, 34, 14, 9, 1]**
>>
>> ==========================================================
>>>  **II**. choose 56 from unsorted sequence, insert in into sorted sequence. 
>>
>>> because 56 is > 23 so shift 23 to right, because 45<56, so shift 45 to  right, then there should be a hole for 56 to insert.
>>>
>>> after insertion you will get the sequence:
>>>
>>> **List:**[56, 45, 23, 2, 13, 89, 34, 14, 9, 1]
>>>
>>> **SORTED:   [56, 45, 23]**
>>>
>>> **UNSORT:   [2, 13, 89, 34, 14, 9, 1]**
>>
>> ==========================================================
>>> **...**
>>
>> ==========================================================
>## Code Python
>>  Just look at the python implemention here:
>>
>>
        def(v, n):
            "insortion sort"
            indexes = range(1, n, 1)
            for index in indexes:
                itemforinsert = v[index]
                loopcounter = index     # start to shift
                while(loopcounter > 0) and (itemforinsert > v[loopcounter-1]):
                    # shift right
                    v[loopcounter] = v[loopcounter-1]
                    loopcounter = loopcounter - 1
                # insert
                v[loopcounter] = itemforinsert
                
>>
>>  we will use the code below to test the insertion func:
>>
        print "for ", index, "the list is: ", v
>>
>## Rusult:
>>
>>  start to test the insert sort: 
>>
>>> [23, 45, 56, 2, 13, 89, 34, 14, 9, 1]
>>
>>  test every index: 
>>
>>> for  1 the list is:  [45, 23, 56, 2, 13, 89, 34, 14, 9, 1]
>>
>>> for  2 the list is:  [56, 45, 23, 2, 13, 89, 34, 14, 9, 1]
>>
>>> for  3 the list is:  [56, 45, 23, 2, 13, 89, 34, 14, 9, 1]
>>
>>> for  4 the list is:  [56, 45, 23, 13, 2, 89, 34, 14, 9, 1]
>>
>>> for  5 the list is:  [89, 56, 45, 23, 13, 2, 34, 14, 9, 1]
>>
>>> for  6 the list is:  [89, 56, 45, 34, 23, 13, 2, 14, 9, 1]
>>
>>> for  7 the list is:  [89, 56, 45, 34, 23, 14, 13, 2, 9, 1]
>>
>>> for  8 the list is:  [89, 56, 45, 34, 23, 14, 13, 9, 2, 1]
>>
>>> for  9 the list is:  [89, 56, 45, 34, 23, 14, 13, 9, 2, 1]
>>
>>  after sort: 
>>
>>> [89, 56, 45, 34, 23, 14, 13, 9, 2, 1]
>>
>>  Good Bye.
>>
========================================================================================
