# Binary Search

> Binary search is really a good, easy, simple method to find the data in an array.

> Here are the tips when you apply the Binary search method:

>>  1. make sure the array in sorted in increasing order.
>>  2. the search method use index as argument
>>  3. the result is the index in the array
>>  4. do not forget to use the recursive method to handle this

# Description

>##Sample

>>  Array: [23, 45, 67, 78, 89, 123, 234, 345, 456, 789]
>>    (*increasing order.*)

>##Steps

>> Here we will find 67 as example.

>>  1. compare 67 with the middle elements in array which is 89, you can just calculate the index by 0+9=9/2=4, keep care that the index is an integer.
>>  2. just search the array [23, 45, 67, 78], because we find that the 67 in the lower part of the array.
>>  3. do step 1 and step 2 repeatedly until you find the element and return.

# Code Python

    # binary search module
    def binsearch(array, find, low, high):
      "low and high are index here."
      if(low < high):
        mid = int((low + high) / 2)
        if(array[mid] == find):
          return mid
        elif(array[mid] > find):
          return binsearch(array, find, low, mid - 1)
        else:
          return binsearch(array, find, mid + 1, high)

# Test result

    Binary Search


    67  is the  2  index of array [23, 45, 67, 78, 89, 123, 234, 345, 456, 789]
    
    Good Bye.
