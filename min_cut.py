##=============================================================
"""
    Karger's minimum cut graph algorithm.
    Procedure:
    1) Convert the graph from text to an adjacency list.
    2) Get a random edge from the adjacency list.
    3) Append the list of the second vertex to the list
       of first vertex.
    4) In the elements of the list of the second vertex, replace all
       occurences of the second vertex with first vertex.
    5) Remove self loops.
    6) Repest the process until only 2 adjacent list remains.

    7) Carry out the above process for many times to get the correct result.
"""
##=============================================================

import random
import copy
import re

def getRandomEdge(G):
    v1= G.keys() [random.randint(0,len(G)-1)]
    v2= G[v1] [random.randint(0,len(G[v1])-1)]
    return v1, v2
    

def kargerContra(Graph):
    
    v1,v2 = getRandomEdge(Graph)

    #1. Attach v2's list to v1.
    Graph[v1].extend(Graph[v2])

    #2. Replace all appearances of v2 as v1

    for elem in Graph[v2]:
        lst = Graph[elem]
        for i in range(0,len(lst)):
            if lst[i] == v2:
                lst[i] = v1

    #3. remove self loop
    while v1 in Graph[v1]:
        Graph[v1].remove(v1)

    #4. Delete v2's list
    del Graph[v2]

def karger(Graph):
    while len(Graph) > 2 :
        kargerContra(Graph)
    return len(Graph[Graph.keys()[0]])
    

if __name__ == "__main__":

    Graph = {} # A dict that will be representing a adjacency list

    ## Read from file
    fd = open("kargerAdj.txt",'r')
    data = fd.readlines()

    ## Store data as adjacency list
    for line in data:
        lst = []
        line.strip('\r\n')
        n_line = re.sub(r'\t',' ',line)
        n_line = re.sub(r' +', ' ', n_line)
        n_line = re.sub(r'^ ','',n_line)

        lst_1 = n_line.split(' ')
        for elem in lst_1:
            if len(re.sub(r'\r\n','',elem)) != 0:
                lst.append(int(re.sub(r'\r\n','',elem)))

        Graph[lst[0]] = lst[1:]

    ## Run Karger Algo.

    mini = karger(copy.deepcopy(Graph))

    for i in range(0,1000):
        res = karger(copy.deepcopy(Graph))
        if res < mini:
            mini = res

    print "Answer : ",mini
        


    
    
