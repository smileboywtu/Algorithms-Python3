# Heap Sort
Simple example here:

![Alt Text][1]

Although heap sort somewhat slower in practice on most machines than a well-implemented quicksort, it has the advantage of a more favorable worst-case O(n log n) runtime.[wiki][2]

# Description

Let's start with an unsorted array:

    [6, 5, 3, 1, 8, 7, 2, 4]

  **I**. **firstly you need to build the head.**

  + assuming 6 is the parent(root) and this array is the result of the breath first of the binary tree, so if the parent gets index i in the array and the  indexes of the children are:

    - left child: 2*i + 1
    - right child: 2*i + 2

  build the tree to make all the parent bigger than it's child. then the heap is built correctly.

  1. add 6 to the heap

  ![Alt text](http://g.gravizo.com/g?
    digraph A1 {
      6
    }
  )

  2. add 5, 3 to the heap

  ![Alt text](http://g.gravizo.com/g?
    digraph A2 {
      6 -> 5;
      6 -> 3;
    }
  )

  3. add 1, 8 to the heap

  ![Alt text](http://g.gravizo.com/g?
    digraph A3 {
      6 -> 5
      6 -> 3
      5 -> 1
      5 -> 8
    }
  )
  ![Alt text](http://g.gravizo.com/g?
    digraph A4 {
      6 -> 8
      6 -> 3
      8 -> 1
      8 -> 5
    }
  )
  ![Alt text](http://g.gravizo.com/g?
    digraph A4 {
      8 -> 6
      8 -> 3
      6 -> 1
      6 -> 5
    }
  )

  4. add the rest and reverse the binary heap, at last you will get

  ![Alt text](http://g.gravizo.com/g?
    digraph A4 {
      8 -> 6
      8 -> 7
      6 -> 4
      6 -> 5
      7 -> 3
      7 -> 2
      4 -> 1
    }
  )

  5. with all the data in the array, we build the heap. From the heap we know the root is always the largest number in the array, so we can save the root and build the heap again and get the largest number in the rest heap.


  **II**. **sort the heap**

  1. save the root in the sorted array
  2. build the heap again
  3. repeat the step one and two

# Code Python

  ```Python
    def max_heapify(heap, heap_size, index):
        "max the heap of root index"
        parent = index
        left = (parent << 1) + 1
        right = (parent + 1) << 1

        # compare left child
        if left < heap_size and heap[left] > heap[parent]:
            parent = left

        # compare right child
        if right < heap_size and heap[right] > heap[parent]:
            parent = right

        # get the largest and heapify the changed
        if parent != index:
            heap[index], heap[parent] = heap[parent], heap[index]
            max_heapify(heap, heap_size, parent)

    def build_heap(data):
        "use the list to build the heap"
        heap_size = len(data)

        # here you need to think why use (sizeof array - 2) / 2
        for index in range((heap_size-2) // 2, -1, -1):
            max_heapify(data, heap_size, index)

        return data

    def heap_sort(data):

        heap = build_heap(data)

        heap_size = len(heap)

        while heap_size > 1:

            # swap the root with last one
            heap[0], heap[heap_size - 1] = heap[heap_size - 1], heap[0]
            heap_size -= 1

            # heap sort the root
            max_heapify(heap, heap_size, 0)
  ```

# Contact

  + email: 294101042@qq.com

[1]: https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif   "heap sort(comes from wiki)"
[2]: https://en.wikipedia.org/wiki/Heapsort "wiki"
