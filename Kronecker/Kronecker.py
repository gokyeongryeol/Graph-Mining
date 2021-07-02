import numpy as np
from scipy.sparse import lil_matrix
import time

class KProds:
    def __init__(self,  k: int, filePath: str) -> None:
        self.k = k # The number of Kronecker products
        ############## #TODO: Complete the function ##################
        # Load the inital matrix from the file
        
        # You may declare any class variables if needed                        #
        ########################################################################
        self.initiator = np.loadtxt(filePath) # k x k matrix
        self.length = self.initiator.shape[0]
        (self.index1, self.index2) = lil_matrix(self.initiator).nonzero()
        ######################### Implementation end ###########################

    def produceGraph(self) -> lil_matrix:
        ############## #TODO: Complete the function ##################
        # Compute the k-th Kronecker power of the inital matrix
        ########################################################################
        previous = self.initiator
        for itr in range(self.k-1):
            post = power_upgrade(previous, self.length, self.index1, self.index2)
            previous = post
            
        adj = post
        return adj         
        ######################### Implementation end ###########################

########################################################################
# You may add additional functions for convenience                        #
########################################################################
def power_upgrade(previous, length, index1, index2):
    previous_length = previous.shape[0]
    post_length = previous_length * length
    post = lil_matrix(np.zeros(shape=(post_length, post_length)))
    for idx1, idx2 in zip(index1, index2):
        row_start = previous_length * idx1
        row_end = previous_length * (idx1 + 1)
        col_start = previous_length * idx2
        col_end = previous_length * (idx2 + 1)
        post[row_start:row_end, col_start:col_end] = previous
    return post
        
######################### Implementation end ###########################
