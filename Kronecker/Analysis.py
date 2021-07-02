import matplotlib.pyplot as plt
import numpy as np
import random

class Analysis:
    def __init__(self, adj, fileName) -> None:
        ############## #TODO: Complete the function ##################
        # Store adjacency matrix (estimated)
        ########################################################################
        self.adj = adj
        self.degrees = self.degree_dist(adj)
        self.fileName = fileName        
	######################### Implementation end ###########################


    ########################################################################
    # You may add additional functions for convenience                        #
    ########################################################################
    def degree_dist(self, adj):
        row_sum = np.array(adj.sum(axis=0)).reshape(-1)
        u, counts = np.unique(row_sum, return_counts=True)
        degrees = dict(zip(u, counts))
        return degrees
    
    def plotHeatMap(self):
        plt.imshow(self.adj.toarray())
        plt.savefig('heatmap of '+ self.fileName)
        plt.close()
    ######################### Implementation end ###########################

    def plotDegDist(self):
        plt.scatter(self.degrees.keys(), self.degrees.values())
        plt.xlabel('Degree')
        plt.ylabel('Count')
        plt.xscale('log')
        plt.yscale('log')
        plt.xlim([max(min(self.degrees.keys()) - 10, 0.5), max(self.degrees.keys()) + 100])
        plt.savefig(self.fileName)
        plt.close()
