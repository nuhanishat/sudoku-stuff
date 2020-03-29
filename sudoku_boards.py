#!/usr/bin/env python

#Author: Nuha Nishat

# This creates the boards to solve as numpy array

import numpy as np 


board1_easy = [[8, 0, 0, 5, 1, 0, 0, 0, 2],
               [0, 0, 6, 9, 8, 0, 4, 5, 0],
               [0, 0, 0, 0, 0, 6, 0, 0, 0],
               [3, 5, 0, 7, 0, 0, 6, 1, 0],
               [0, 0, 9, 6, 2, 5, 7, 0, 0], 
               [0, 7, 4, 0, 0, 3, 0, 8, 5], 
               [0, 0, 0, 3, 0, 0, 0, 0, 0], 
               [0, 2, 3, 0, 7, 9, 1, 0, 0], 
               [7, 0, 0, 0, 5, 2, 0, 0, 3]]

np.save('1_Easy', np.array(board1_easy))
print(np.array(board1_easy))


board2_medium = [ [7, 2, 1, 0, 8, 0, 0, 6, 0],
				[0, 0, 0, 7, 0, 0, 8, 0, 0], 
				[0, 0, 0, 1, 0, 0, 0, 9, 5],
				[0, 0, 8, 3, 0, 6, 0, 0, 9], 
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[9, 0, 0, 2, 0, 5, 1, 0, 0], 
				[6, 9, 0, 0, 0, 1, 0, 0, 0], 
				[0, 0, 5, 0, 0, 2, 0, 0, 0], 
				[0, 1, 0, 0, 7, 0, 6, 5, 3]]

np.save('2_Medium', np.array(board2_medium))

board3_hard = [[0, 0, 0, 0, 1, 0, 0, 9, 0],
			  [0, 0, 0, 0, 0, 2, 7, 0, 0],
			  [6, 3, 1, 5, 0, 0, 4, 2, 0],
			  [0, 0, 4, 0, 0, 0, 2, 0, 7], 
			  [0, 0, 0, 0, 4, 0, 0, 0, 0], 
			  [3, 0, 5, 0, 0, 0, 6, 0, 0],
			  [0, 8, 7, 0, 0, 4, 9, 3, 1], 
			  [0, 0, 6, 9, 0, 0, 0, 0, 0],
			  [0, 5, 0, 0, 7, 0, 0, 0, 0]]

np.save('3_Hard', np.array(board3_hard))

board4_evil = [[4, 0, 0, 0, 0, 3, 0, 6, 0],
			 [0, 0, 0, 9, 2, 0, 0, 0, 0],
			 [0, 5, 0, 0, 0, 6, 0, 9, 8],
			 [7, 0, 0, 0, 0, 5, 0, 0, 0],
			 [8, 0, 1, 0, 0, 0, 3, 0, 4],
			 [0, 0, 0, 6, 0, 0, 0, 0, 7],
			 [2, 4, 0, 3, 0, 0, 0, 1, 0],
			 [0, 0, 0, 0, 1, 4, 0, 0, 0],
			 [0, 3, 0, 7, 0, 0, 0, 0, 9]]

np.save('4_Evil', np.array(board4_evil))






























































            