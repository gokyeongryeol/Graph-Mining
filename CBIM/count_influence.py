# No external imports are allowed other than numpy
import numpy as np

def count_influence(graph, seeds, threshold):
    """
    Implement the function that counts the ultimate number of active nodes.

    Inputs:
        graph: directed input graph in the edge list format.
            That is, graph is a list of tuples of the form (u, v),
            which indicates that there is an edge u to v.
            You can assume that both u and v are integers, while you cannot
            assume that the integers are within a specific range.
        seeds: a list of initial active nodes.
        threshold: the propagation threshold of the Independent Cascade Model.

    Output: the number of active nodes at time infinity.
    """

    node = np.unique(graph)    
    num_total = int(max(node)-min(node))+1
    
    adjacency = np.zeros((num_total, num_total), dtype='int')
    for idx in range(len(graph)):
        src_idx = graph[idx][0]
        des_idx = graph[idx][1]
        adjacency[src_idx, des_idx] = 1
    
    in_degree = adjacency.sum(0)

    active_node = seeds
    curr = seeds
    while True:
        count = adjacency[curr].sum(0)
        neighbors = count > 0
        if sum(neighbors) < 1:
            break
        remaining = np.setdiff1d(np.arange(num_total)[neighbors], active_node)
        binary = np.random.binomial(1, p=np.clip(threshold/in_degree[remaining]*count[remaining], 0.0, 1.0))
        active_node = np.append(active_node, remaining[binary==1])
        curr = remaining[binary == 1]
    return len(active_node)
