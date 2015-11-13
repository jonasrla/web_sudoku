from solver import *
from _utils import clear_table


def _new_table(size=9):
    return [[{"possibilities": range(1,size+1), "checked": False} for i in xrange(size)] for j in xrange(size)]

def get_solution():
    table = _new_table()
    
    table = solve(table)

    table = clear_table(table)
    return table