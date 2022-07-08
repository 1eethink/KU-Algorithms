class Node(object):
    def __init__(self, data):
        self.freq = data
        self.left = None
        self.right = None
        self.rightup = None
        self.leftup = None


A = []
B = {}
order = []

n = int(input())
for i in range(n):
    temp = int(input())
    A.append(Node(temp))
    order.append((i, temp))
    B[i] = []




def min_heapify(A, i):
    l = 2*(i+1)-1
    r = 2*(i+1)+1-1

    min = i
    if l <= heap_size-1:
        if A[l].freq < A[i].freq:
            min = l
        else:
            min = i

    if r <= heap_size-1:
        if A[r].freq < A[min].freq:
            min = r

    if min != i:
        temp = A[min]
        A[min] = A[i]
        A[i] = temp
        min_heapify(A, min)

def build_min_heap(A):
    global heap_size
    heap_size = len(A)
    for i in range(int(len(A)/2)-1, -1, -1):
        min_heapify(A, i)

def extract_min(A):
    global heap_size
    if heap_size < 0:
        print("heap underflow")
    min = A[0]
    A[0] = A[heap_size-1]
    heap_size = heap_size-1
    min_heapify(A,0)

    return min

def heap_decrease_key(A, i, key):
    if key.freq > A[i].freq:
        print("new key is bigger than current key")
    A[i] = key
    while i>0 and A[int((i+1)/2)-1].freq > A[i].freq:
        temp = A[i]
        A[i] = A[int((i+1)/2)-1]
        A[int((i+1)/2)-1] = temp
        i = int((i+1)/2)-1

def min_heap_insert(A, key):
    global heap_size
    heap_size = heap_size + 1
    A[heap_size-1] = Node(float("inf"))

    heap_decrease_key(A, heap_size-1, key)

tempnodes = []

def huffman(C):
    n = len(C)
    build_min_heap(C)

    global tempnodes

    for i in range(0, n-1):
            x = extract_min(C)
            #print("x: ", x.freq)
            if x.right == None and x.left == None:
                tempnodes.append(x)

            y = extract_min(C)
            #print("y: ", y.freq)
            if y.right == None and y.left == None:
                tempnodes.append(y)

            z = Node(x.freq+y.freq)
            z.left = x
            x.rightup = z
            z.right = y
            y.leftup = z
            #for j in range(len(C)):
            #    print("before insert in C", C[j].freq, "heapsize", heap_size)
            min_heap_insert(C, z)
            #for j in range(len(C)):
            #    print("after insert in C", C[j].freq, "heapsize", heap_size)

    return extract_min(C)


x = huffman(A)

j=-1
#print(tempnodes)
for i in tempnodes:
    j=j+1
    while True:
        if(i.rightup != None or i.leftup != None):
            if i.rightup != None:
                B[j].append('0')
                i = i.rightup

            if i.leftup != None:
                B[j].append('1')
                i = i.leftup

        else:
            break



order.sort(key = lambda x : x[1])



for j in B:
    B[j].reverse()
    #print("B: ", B)
    #print(''.join(e for e in B[j]))

D = {}
for i in range(len(order)):
    D[order[i][0]] = B[i]

#print(D)

if len(D) == 1:
    print('0')
else:
    for k in range(len(D)):
        #print(": ", D)
        print(''.join(e for e in D[k]))
