from count_influence import *
from seed_selection import *
import time

file = 'soc-Epinions.txt'
graph = np.loadtxt(file, dtype='int')
node = np.unique(graph)
    
def main(policy_list, percent_list, threshold_list):
    for policy in policy_list:
        for percent in percent_list:
            for threshold in threshold_list:
                n = int(len(node) * percent * 0.01)    
                seeds = seed_selection(graph, policy, n)
                num_active = count_influence(graph, seeds, threshold)
                print(policy, percent, threshold, num_active)

if __name__ == '__main__':
    tic = time.time()
    
    for idx in range(10):
        #task1
        print('number of intial active node check')
        main(['degree','random'], [0.1, 0.25, 0.5, 1.0, 2.5, 5.0], [1.0])
        #task2
        print('threshold check')
        main(['degree','random'], [1.0], [0.2, 0.4, 0.6, 0.8, 1.0])
        #task3
        print('custom policy check')
        main(['custom'], [1.0], [1.0])
    
        toc = time.time()
    
        mon, sec = divmod(toc-tic, 60)
        hr, mon = divmod(mon, 60)
        print('total wall-clock time is ', int(hr),':',int(mon),':',int(sec))
    
    