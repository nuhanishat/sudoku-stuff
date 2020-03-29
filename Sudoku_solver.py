# Author: Nuha Nishat

# This is sudoku solver

import numpy as np


class Sudoku():
    def __init__(self, board):
        self.board = board
        self.rows = range(9)
        self.columns = range(9)
        self.boxes = range(9)
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.backtracked = 0
        self.unassigned = []
        self.blanks = []
        
 
    # Find unassigned blanks
    def find_blanks(self, count): # count keeps track of the current cell location
        for i in self.rows:
            for j in self.columns:
                if self.board[i][j] == 0:
                    count[0] = i
                    count[1] = j
                    return True
        return False

    
    # Saves the location of blanks spaces
    def find_blank_loc(self):
        blanks = []
        for i in self.rows:
            for j in self.columns:
                if self.board[i][j] == 0:
                    blanks.append([i, j])

        return blanks


    # Returns domain after checking row constraints
    def check_rows_dom(self, row):
        values = self.values.copy()
        for i in self.columns:
            if self.board[row][i] in values:
                values.remove(self.board[row,i])
        return values

    # Checks if meets contraints and returns True or False
    def check_rows(self, row, value):
        for i in self.columns:
            if self.board[row][i] == value:
                return True
        return False

    # Returns domain after checking column constraints
    def check_columns_dom(self, column):
        values = self.values.copy()
        for i in self.rows:
            if self.board[i][column] in values:
                values.remove(self.board[i][column])
        return values

    
    # Checks if meets contraints and returns True or False
    def check_columns(self, column, value):
        for i in self.rows:
            if self.board[i][column] == value:
                return True
        return False

    # Checks if meets contraints and returns True or False
    def check_boxes(self, row, column, value):
        for i in range(3):
            for j in range(3):
                if self.board[row+i][column+j] == value:
                    return True
        return False

    # Returns domain after checking box constraints
    def check_boxes_dom(self, row, column):
        values = self.values.copy()
        for i in range(3):
            for j in range(3):
                if self.board[row+i][column+j] in values:
                    values.remove(self.board[row+i][column+j])
        return values


    # Return True or False based on constaints
    def check_constraints(self,row,column,value):
        if not self.check_rows(row,value) and not self.check_columns(column,value) and not self.check_boxes(row-row%3, column-column%3, value):
            return True
        return False
    
    
    # Find all the unassigned variables that meet the meets the constraints
    def find_constrained_dom(self, row, column):
        row_dom = self.check_rows_dom(row)
        col_dom = self.check_columns_dom(column)
        box_dom = self.check_boxes_dom(row-row%3, column-column%3)


        ordered_dom = set(row_dom).intersection(set(col_dom), set(box_dom))
        return list(ordered_dom)
    
    def update_unassigned(self):
        self.blanks = self.find_blank_loc()
        self.unassigned = []

        #print(blanks)

        for i in range(len(self.blanks)):
            cell_dom = self.find_constrained_dom(self.blanks[i][0], self.blanks[i][1])
            self.unassigned.append(cell_dom)

        # print(self.unassigned)


    # What is backtracking doing? 

        # It checks if a cell is blank, keeps the previous structure. Count is the starting cell
        # If blank:
            # Find possible values that could go in the cell (domain)
            # Update list of unassigned variables with the domain found (The idea is to reduce the search space)
            # For each value in domain, start searching.....
                # Do your usual backtracking stuff
    

    def backtracking(self, count):
        if not self.find_blanks(count):
            return True

        row = count[0]
        column = count[1]

        cell_dom = self.find_constrained_dom(row, column)


        index = self.blanks.index([row, column])

        self.unassigned[index] = cell_dom

        for j in range(len(cell_dom)):
            self.board[row][column] = cell_dom[j]

            if self.backtracking(count):
                return True

            self.board[row][column] = 0

            if self.board[row][column] == 0:
                self.backtracked += 1

        return False


    

if __name__ == '__main__':


    board1 = np.load('1_Easy.npy')

    board2 = np.load('2_Medium.npy')

    board3 = np.load('3_Hard.npy')

    board4 = np.load('4_Evil.npy')

    board_name = {'Easy':board1, 'Medium':board2, 'Hard':board3, 'Evil':board4}

    board = ['Easy', 'Medium', 'Hard', 'Evil']


    for item in board:
        sudoku = Sudoku(board_name[item])

        sudoku.update_unassigned()
        result = sudoku.backtracking([0, 0])
     
        
        if result == True:
            print(np.matrix(sudoku.board))
            print('Number of times backtracked: ', sudoku.backtracked)
        else:
            print('No solution')

