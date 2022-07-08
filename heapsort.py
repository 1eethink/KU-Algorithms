def max_heapify(A, i):
    l = 2*(i+1)-1
    r = 2*(i+1)+1-1

    largest = i
    if l <= heap_size-1:
        if A[l] > A[i]:
            largest = l
        else:
            largest = i

    if r <= heap_size-1:
        if A[r] > A[largest]:
            largest = r

    if largest != i:
        temp = A[largest]
        A[largest] = A[i]
        A[i] = temp
        max_heapify(A, largest)

def build_max_heap(A):
    global heap_size
    heap_size = len(A)
    for i in range(int(len(A)/2)-1, -1, -1):
        max_heapify(A, i)


def heapsort(A):
    build_max_heap(A)
    for i in range(len(A)-1, 0, -1):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        global heap_size
        heap_size = heap_size - 1
        max_heapify(A, 0)



A = []
n = int(input())
for i in range(n):
    A.append(int(input()))

heapsort(A)

for i in A:
    print(i)

