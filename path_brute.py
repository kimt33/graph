import numpy as np

def shortest_path(Adj, from_node):
    #print 'we are at{0}'.format(0)
    to_search = np.ones(Adj.shape[0], dtype=bool)
    #print to_search
    output = Adj[from_node]
    #print output
    to_search[from_node] = False
    count=1
    a=1
    while np.any(to_search):
        #first non False index
        i = np.where(to_search)[0][0]
        #print 'we are at {0}'.format(i)
        #print to_search
        #NOTE: there must be at least one True in to_search
        temp = Adj[i]
        temp[temp!=0] += output[i]
        temp[from_node] = 0
        # assign to output if it is less than output value that isn't 0
        # FUCKING HAMMER
        indices1 = np.logical_and(output>temp, temp!=0)
        indices2 = np.logical_and(output==0, temp>0)
        indices = np.logical_or(indices1, indices2)
        indices[from_node] = False
        indices[i] = False
        output[indices] = temp[indices]
        #print output
        to_search[indices] = True
        to_search[i] = False
    return output

def shortest_path_noweights(Adj, from_node):
    to_search = np.ones(Adj.shape[0], dtype=bool)
    output = Adj[from_node]
    def follow_indices(output, n):
        indices_on = np.where(output==n)[0]
        if np.any(indices_on):
            indices_off = np.where(output==0)[0]
            for i in indices_on:
                # i want to check if any of the Adj[i][indices_off] are 1
                temp = np.where(Adj[i][indices_off]==1)[0] # indices of the indices
                if temp.size>0:
                    output[indices_off[temp]] = n+1
        else:
            return False
    n = 1
    while n<Adj.shape[0]:
        if follow_indices(output, n)==False:
            break
        n += 1
    output[from_node] = 0
    return output

f = open('test.txt' ,'r')
num_test = int(f.readline())
for i in range(num_test):
    numbers = f.readline().split(' ')
    num_nodes, num_edges = (int(j) for j in numbers)
    print num_nodes
    Adj = np.zeros((num_nodes, num_nodes))
    for j in range(num_edges):
        numbers = f.readline().split(' ')
        row, column = (int(k) for k in numbers)
        row -= 1
        column -=1
        Adj[row, column] = 1
        Adj[column, row] = 1
    print Adj
    node_sel = int(f.readline())-1
    print node_sel
    costs = shortest_path_noweights(Adj, node_sel)
    costs = [str(int(i)) if i!= 0 else str(-1) for i in costs]
    costs.pop(node_sel)
    print ' '.join(costs)
'''
a=np.array([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]])
print shortest_path_noweights(a,0)
'''
