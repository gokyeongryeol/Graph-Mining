"""This file contains an incomplete implementation of the CitationNetwork class and HITS algorithm.
Your tasks are as follows:
    1. Complete the CitationNetwork class
    2. Complete the hits method
    3. Complete the print_top_k method
"""

from __future__ import absolute_import
from typing import Dict, Tuple

############################################################################
# You may import additional python standard libraries, numpy and scipy.
# Other libraries are not allowed.
import numpy as np
from scipy.sparse import lil_matrix
############################################################################


class CitationNetwork:
    """Graph structure for the analysis of the citation network
    """

    def __init__(self, file_path: str) -> None:
        """The constructor of the CitationNetwork class.
        It parses the input file and generates a graph.

        Args:
            file_path (str): The path of the input file which contains papers and citations
        """

        ######### Task 1. Complete the constructor of CitationNetwork ##########
        # Load the input file and process it to a graph
        # You may declare any class variable or method if needed
        f = open(file_path, 'r')
        self.num_nodes = int(f.readline())
        lines = f.readlines()
        self.nodes = self.separate_nodes(lines)
        self.adj = self.construct_adj(self.nodes)
        ########################################################################

        #raise NotImplementedError("CitationNetwork class is not implemented")

    ############################################################################
    # You may add additional functions for convenience                         #
    
    def separate_nodes(self, lines):
        block, nodes = [], []
        for line in lines:
            if line == '\n':
                nodes.append(block)
                block = []
            else:
                block.append(line)
        return nodes
    
    def construct_adj(self, nodes):
        adj = lil_matrix((self.num_nodes, self.num_nodes))
        for block in nodes:
            for description in block:
                if '#index' in description:
                    from_index = int(description.lstrip('#index').rstrip('\n'))
                if '#%' in description:
                    try:
                        to_index = int(description.lstrip('#%').rstrip('\n'))
                        adj[from_index, to_index] = 1
                    except ValueError:
                        pass
        return adj

def hits(
    graph: CitationNetwork, max_iter: int, tol: float
) -> Tuple[Dict[int, float], Dict[int, float]]:
    """An implementation of HITS algorithm.
    It uses the power iteration method to compute hub and authority scores.
    It returns the hub and authority scores of each node.

    Args:
        graph (CitationNetwork): A CitationNetwork
        max_iter (int): Maximum number of iterations in the power iteration method
        tol (float): Error tolerance to check convergence in the power iteration method

    Returns:
        (hubs, authorities) (Tuple[Dict[int, float], Dict[int, float]]): Two-tuple of dictionaries.
            For each dictionary, the key is the paper index (int) and the value is its score (float)
    """

    ################# Task2. Complete the hits function ########################
    # Compute hub and authority scores of each node using the power iteration method
    num_nodes = graph.num_nodes
    h = np.array([1/np.sqrt(num_nodes) for i in range(num_nodes)])
    a = np.array([1/np.sqrt(num_nodes) for i in range(num_nodes)])
    
    curr_iter = 0
    end_condition = False
    while not end_condition:
        curr_iter += 1
        
        upd_h = graph.adj.dot(a)
        upd_a = graph.adj.transpose().dot(upd_h)
    
        h_norm = np.linalg.norm(upd_h)
        a_norm = np.linalg.norm(upd_a)
        
        upd_h /= h_norm
        upd_a /= a_norm
        
        condition1 = curr_iter > max_iter
        condition2 = np.linalg.norm(h-upd_h) < tol
        end_condition = condition1 or condition2 
        
        h, a = upd_h, upd_a
    return (dict(enumerate(h)), dict(enumerate(a)))
    ############################################################################

    #raise NotImplementedError("hits method is not implemented")


def print_top_k(scores: Dict[int, float], k: int) -> None:
    """Print top-k scores in the decreasing order and the corresponding indices.
    The printing format should be as follows:
        <Index 1>\t<score>
        <Index 2>\t<score>
        ...
        <Index k>\t<score>

    Args:
        scores (Dict[int, float]): Hub or Authority scores.
            For each dictionary, the key is the paper index (int) and the value is its score (float)
        k (int): The number of top scores to print.
    """

    ############## Task3. Complete the print_top_k function ####################
    # Print top-k scores in the decreasing order
    
    ordering = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    topk = ordering[:k]
    for i in range(k):
        print(topk[i][0], '\t', topk[i][1])
    ############################################################################

    #raise NotImplementedError("print_top_k method is not implemented")
