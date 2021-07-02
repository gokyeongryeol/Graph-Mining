# No external imports are allowed other than numpy
import numpy as np

def seed_selection(graph, policy, n):
    """
    Implement the function that chooses n initial active nodes.

    Inputs:
        graph: directed input graph in the edge list format.
            That is, graph is a list of tuples of the form (u, v),
            which indicates that there is an edge u to v.
            You can assume that both u and v are integers, while you cannot
            assume that the integers are within a specific range.
        policy: policy for selecting initial active nodes. ('degree', 'random', or 'custom')
            if policy == 'degree', n nodes with highest degrees are chosen
            if policy == 'random', n nodes are randomly chosen
            if policy == 'custom', n nodes are chosen based on your own policy
        n: number of initial active nodes you should choose

    Outputs: a list of n integers, corresponding to n nodes.
    """
    
    
    node = np.unique(graph)
    num_total = int(max(node)-min(node))+1    
    
    if policy == 'degree': 
        out_index, out_degree = np.unique(graph[:,0], return_counts=True)
        in_index, in_degree = np.unique(graph[:,1], return_counts=True)
        
        out_degree_array = np.zeros(num_total, dtype='int')
        in_degree_array = np.zeros(num_total, dtype='int')
        degree = np.zeros(num_total, dtype='int')
        
        out_degree_array[out_index] = out_degree
        in_degree_array[in_index] = in_degree
        degree = out_degree_array + in_degree_array
        
        degree_ordering = np.argsort(degree)
        selection = degree_ordering[-n:]
            
    elif policy == 'random':
        selection = np.random.choice(node, n)
    
    elif policy == 'custom':
        adjacency = np.zeros((num_total, num_total), dtype='int')
        for idx in range(len(graph)):
            src_idx = graph[idx][0]
            des_idx = graph[idx][1]
            adjacency[src_idx, des_idx] = 1
        
        in_degree = adjacency.sum(0)
        out_degree = adjacency.sum(1)
        degree = in_degree + out_degree
        degree_ordering = np.argsort(degree)
        
        selection = degree_ordering[-n+40:]
        for i in range(40):
            max_value = -9999
            for j in np.setdiff1d(node, selection):
                selection_prime = np.append(selection, j)
                count = adjacency[j:j+1].sum(0)
                neighbors = count > 0
                remaining = np.setdiff1d(np.arange(num_total)[neighbors], selection_prime)
                value = sum(np.clip(1.0/in_degree[remaining]*count[remaining], 0.0, 1.0))
                if value > max_value:
                    max_value = value
                    tmp_node = j
            selection = np.append(selection, tmp_node)
    return list(selection)

    