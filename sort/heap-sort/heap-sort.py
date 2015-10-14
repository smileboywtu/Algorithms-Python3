# heap sort
# use the python 3.5

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

def main():

    print("""

        Heap Sort Method

    """)

    array = [6, 5, 3, 1, 8, 7, 2, 4]

    print("source list is: ", array)

    heap_sort(array)

    print("after sort: ", array)


if __name__ == '__main__':
    main()
