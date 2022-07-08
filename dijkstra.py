import copy

class vertice(object):
    def __init__(self, data):
        self.name = None
        self.d = data
        self.pre = None

vertices_in = raw_input()
vertices = vertices_in.split(',')

# initialization
vertice_set = []
temp = 0
#vertices[len(vertices)-1] = vertices[len(vertices)-1][0:-1]

for i in vertices:
    if i == 'A':
        temp_vertice = vertice(0)
        vertice_set.append(temp_vertice)
        vertice_set[temp].name = 'A'
        temp = temp + 1
    else:
        temp_vertice = vertice(float("inf"))
        vertice_set.append(temp_vertice)
        vertice_set[temp].name = i
        temp = temp + 1


num_edges = int(input())
edges = []
for i in range(num_edges):
    edges.append(raw_input())



nextedges = []
for i in range(len(edges)):
    nextedges.append(edges[i].split(','))



def min_heapify(A):
    A.sort(key=lambda x: x.d)
    count = -1
    for i in range(len(A)):
        if A[i].d == A[0].d:
            count=count+1

    for i in range(count+1):
        if A[0].name > A[i].name:
            A[0], A[i] = A[i], A[0]



def extract_min(A):
    if len(A) < 0:
        print("heap underflow")

    min = A[0]
    A[0] = A[len(A)-1]

    del A[-1]

    return min

def relax(u, v, w):
    idx = None

    for i in range(len(vertice_set)):
        if vertice_set[i].name == v:
            idx = i

    if idx != None:
        if vertice_set[idx].d > u.d + w:
            vertice_set[idx].d = u.d + w


S = []
temp_nextedges = []
def dijkstra():
    # min-priority Queue
    global nextedges
    global temp_nextedges
    while len(vertice_set) > 0:
        u = extract_min(vertice_set)
        S.append(u)
        temp_nextedges = copy.deepcopy(nextedges)
        count = 0
        if len(vertice_set) > 0:
            for i in range(len(nextedges)):
                if nextedges[i][0] == u.name:
                    relax(u, nextedges[i][1], int(nextedges[i][2]))
                    del temp_nextedges[i-count]
                    count = count + 1
            nextedges = temp_nextedges
        min_heapify(vertice_set)


dijkstra()

S.sort(key=lambda x: x.name)
for i in range(len(S)):
    print(S[i].d)
