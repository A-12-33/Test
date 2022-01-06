class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}

    def vertex(self, v):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(v)
        self.vertices[v] = vert
    # def get_vertex(self, key):
    #     """Return vertex object with the corresponding key."""
    #     return self.vertices[key]

    def __contains__(self, v):
        return v in self.vertices

    def e(self, vertex1, vertex2, w=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[vertex1].vertex_2(self.vertices[vertex2], w)

    # def exist(self, vertex1, vertex2):
    #     """Return True if there is an edge from src_key to dest_key."""
    #     return self.vertices[vertex1].does_it_point_to(self.vertices[vertex2])

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, v):
        self.v = v
        self.points_to = {}

    def retvertex(self):
        """Return key corresponding to this vertex object."""
        return self.v

    def vertex_2(self, vertex1, w):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[vertex1] = w

    def Verticies(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()

    # def get_weight(self, dest):
    #     """Get weight of edge from this vertex to dest."""
    #     return self.points_to[dest]

    # def does_it_point_to(self, dest):
    #     """Return True if this vertex points to dest."""
    #     return dest in self.points_to


class Queue:
    def __init__(self):
        self.entities = []

    def empty(self):
        return self.entities == []

    def Add(self, data):
        self.entities.append(data)

    def remove(self):
        return self.entities.pop(0)


def Marked(V, comp, Mark):
    """Set component[v] = label for all v in the component containing vertex."""
    visited_set = set()
    Que= Queue()
    Que.Add(V)
    visited_set.add(V)
    while not Que.empty():
        current = Que.remove()
        comp[current] = Mark
        for vertex2 in current.Verticies():
            if vertex2 not in visited_set:
                visited_set.add(vertex2)
                Que.Add(vertex2)
grph = Graph()
print("This is the Algorithm to check number of connected components")
print("To add an vertex type - 'add an vertex' followed by the name of the vertex ")
print("To add an edge type - 'add an edge' followed by the end points of the edge ")
print("To find the number of components type -'number of components' ")
print("To end the program type - 'end' ")
while True:
    user=input("Enter:...").lower()
    userin=user.split()
    # do = input('Add edges,Add vertices and type components to know the component:   ').split()


    word1 = userin[0]
    if word1 == 'add':
        word2 = userin[2]
        if word2 == 'vertex':
            key = (userin[3])
            if key not in grph:
                grph.vertex(key)
            else:
                print('The Vertex already exists add another vertex')
        elif word2 == 'edge':
            V1 = (userin[3])
            V2 = (userin[4])
            if V1 not in grph:
                error="Vertex {} does not exist add another edge"
                print(error.format(V1))
                # print('Vertex {} does not exist add another edge '.format(V1))
            elif V2 not in grph:
                error2 = "Vertex {} does not exist add another edge"
                print(error2.format(V2))
                # print('Vertex {} does not exist add another edge'.format(V2))
            else:
                grph.e(V1,V2)
            # else:
            #     if not g.exist(src, dest):
            #         g.edge(src, dest)
            #     else:
            #         print('This Edge already exists.')
    elif word1 == 'comp':
        component = dict.fromkeys(grph, None)
        mark = 1
        for vertex in grph:
            if component[vertex] is None:
                Marked(vertex, component, mark)
                mark += 1

        max_label = mark
        for mark in range(1, max_label):
            component_vertices = [vertex.retvertex() for vertex in component
                                  if component[vertex] == mark]
            print('Component {} contains:'.format(mark), component_vertices)


    elif word1 == 'quit':
        break