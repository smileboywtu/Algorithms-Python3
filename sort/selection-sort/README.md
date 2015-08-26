# Introduction
>   selection is a good way to get the first serval data sequence in order, it's more prefer to use than bubble sort.

# Description
>   Here we just look at a real example for this sort algorithm.
>>## Example

>>> there is a number which contains less than 100 digits. how to get the several digit out of the source number to make the number the rest of the biggest, for example:
>>>
>>> number = {1, 4, 7, 5, 8, 3}, the number contains 6 digits, how you get the smallest number when deleting 4 digits from it. As a result we know the minimum number is 13. here we get the details about this problem.

>>## Details

>>> **I**. you should get the biggest digit from souce number which is 8,
then delete 8 from the source number. you will get 14753. according to the principle you need to delete another 3 digits from it.

>>> **II**. we already know 7 is the bigger digit in 14753, so delete 7 from the source number, after that you will get 1453, you now need to delete 2 digits.

>> **...**

>>## But How?

>>> A good idea is to sort the digits in the number firstly.

>>> if you know the sequence [8, 7, 5, 4, 1, 3], you can quickly get the rest but smallest one, 13, but how to sort part of the number and remain the rest normally.

>>> *selection sort is really a good way to do this.*

=============================================================

>>## selection sort idea

>>> the selection sort each time will get the right data in the right position, it will not need to change the original sequence of the source list.

>>> as the list of [1, 4, 7, 5, 8, 3]

>>> the sort list need 6 turns to get the list in order

>>> 1. select the biggest data in source list, which is 8, and swap index zero with index 5.

>>> 2. select biggest data in the rest array([4, 7, 5, 1, 3]), which is 7, then swap index 1 with index 2.

>>> 3. select the biggest data in array [4, 5, 1, 3], which is 5, then swap index 2 with index 3.

>>> 4. **...**

>>> after 4 turns, you will get [8, 7, 5, 4, 1, 3], just delete the first four digits from the list.

>>## Code Python
        def selectionsort(v, n):
            "selection sort"
            indexes = range(0, n, 1)
            for index in indexes:
                j = index
                while j<n:
                    if v[index] < v[j]:
                        temp = v[index]
                        v[index] = v[j]
                        v[j] = temp
                    j = j + 1
                    
>>## Test
        
>>> we will use the below code to test the result
>>>
       print "for index ", index, "the current list is: ", v
       
>>## Result

>>>source list:  [1, 4, 7, 5, 8, 3]

>>> for index  0 the current list is:  [8, 1, 4, 5, 7, 3]

>>> for index  1 the current list is:  [8, 7, 1, 4, 5, 3]

>>> for index  2 the current list is:  [8, 7, 5, 1, 4, 3]

>>> for index  3 the current list is:  [8, 7, 5, 4, 1, 3]

>>> for index  4 the current list is:  [8, 7, 5, 4, 3, 1]

>>> for index  5 the current list is:  [8, 7, 5, 4, 3, 1]

>>> after sort:  [8, 7, 5, 4, 3, 1]

>>> Good Bye.
   