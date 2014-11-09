##====================================================================
"""
    Strongest Connecting Components in a DIRECTED Graph using
    Kosaraju's 2 pass algorithm using DFS (Non recursive/Stack Based).
"""
##====================================================================

ELEMENTS = 9

"""
@class stack: A class that make list access as a stack
"""
class stack:
    def __init__(self):
        self.items = []
        
    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if len(l) == 0:
            return  False
        else:
            return True

"""
@declare : Declare global hash's
"""
visited = {}
leader = {}
finish_time = {}
stk = stack()

"""
@def init: Initialize global structures.
"""
def init():
    for i in range(1, ELEMENTS + 1):
        visited[i] = 0
        leader[i]  = 0
        finish_time[i] = 0


"""
@def makeGraph: Subroutine for creating graph structure from
                input text file.
"""
def makeGraph():
    file_name = "graph.txt"
    G = {}
    Grev = {}

    fd = open(file_name)
    file_lines = fd.readlines() # Read complete file in a single go.
    fd.close()

    ## initialize the graphs
    for i in range(1, ELEMENTS + 1):
        G[i] = []
        Grev[i] = []

    for line in file_lines:
        [a,b] = line.strip('\r\n').split(' ')
        G[int(a)].append(int(b))
        Grev[int(b)].append(int(a))

    return G, Grev

"""
@def dfs:
"""
def dfs(G, source):
    global t
    #global s
    print "source : ",source
    visited[source] = 1
    leader[source] = s
   
    for j in G[source]:
        if visited[j] == 0:
            dfs(G,j)

    t = t + 1
    finish_time[source] = t
    print "Finish,source : ",t," : ",source
    
        
    

"""
@def dfs_loop: 
"""
def dfs_loop(G):
    global t   ## For Fishing time
    global s   ## For leader
    t = 0
    s = 0
    edge = ELEMENTS
    while edge > 0:
        if visited[edge] == 0:
            s = edge
            dfs(G,edge)
        edge = edge - 1

"""
@main : Start of program
"""
if __name__ == "__main__":

    init()
    G , Grev = makeGraph()
    # Run DFS-loop on the reversed graph
    dfs_loop(Grev)

    print Grev

    # Now create the second graph, with the nodes
    # replaced by their finish times

    newGraph = {}
    for edge in range(1, ELEMENTS + 1):
        temp = []
        for x in G[edge]:
            temp.append(finish_time[x])
            
        newGraph[finish_time[edge]] = temp
    print finish_time
    print newGraph

    init()
    dfs_loop(newGraph) ## The second loop

    lst = sorted(leader.values())
    
    first = lst[0]
    scc = 0
    for i in range(1, ELEMENTS):
        if lst[i] == first:
            pass
        else:
            scc = scc + 1
            first = lst[i]

    print "Number of SCC : ", scc
            
    
