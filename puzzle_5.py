#!/usr/bin/env python

#Each queen is represented by a 2 tuple indicating their
#(col, row) position
def check_conflicts(queen, queen_list):
    for other_queen in queen_list:
        #Are the queens in the same colunm
        if queen[0] == other_queen[0]:
            return True
        #Are the queens in the same row
        if queen[1] == other_queen[1]:
            return True
        #Are the queens in the same diagnal of each other
        delta_column = abs(queen[0]-other_queen[0])
        delta_row = abs(queen[1] - other_queen[1])
        if delta_column == delta_row:
            return True
    #All checks pass no conflict found
    return False
