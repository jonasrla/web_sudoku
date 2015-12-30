from random import randint
from _utils import *
from solver import *

def create_puzzle(level):
    puzzle = get_solution()

    (min_given, lower_bound, dig_interator) = _get_parameters(level)


    for i,j in dig_interator:
        if _given(puzzle) - 1 >= min_given:
            if (_count_column(puzzle, j) - 1) >= lower_bound and (_count_line(puzzle, i) - 1) >= lower_bound:
                try:
                    puzzle = _dig(puzzle,i,j)
                except UnsolvablePuzzleException:
                    pass
            else:
                pass
        else:
            break
    puzzle = _propagate([{j: puzzle[i][j] if j in puzzle[i] else None for j in xrange(9)} for i in xrange(9)])
    return puzzle

def _get_parameters(level):
    table = [[(j,i) for i in xrange(9)] for j in xrange(9)]
    if level == 1:
        sequence = reduce(lambda x,y: x+y, table)
        shuffle(sequence)
        return (randint(50,65),5, iter(sequence))
    elif level == 2:
        sequence = reduce(lambda x,y: x+y, table)
        shuffle(sequence)
        return (randint(36,49),4, iter(sequence))
    elif level == 3:
        map(lambda x: x.reverse(), filter(lambda x: x[0][0]%2, table))
        sequence = filter(lambda x: not (x[0]+x[1])%2, reduce(lambda x, y: x+y, table))
        return (randint(32,35),3, iter(sequence))
    elif level == 4:
        map(lambda x: x.reverse(), filter(lambda x: x[0][0]%2, table))
        sequence = reduce(lambda x,y: x+y, table)
        return (randint(28,31),2, iter(sequence))
    else:
        sequence = reduce(lambda x,y: x+y, table)
        return (randint(22,27),0, iter(sequence))

def _propagate(puzzle):
    for i in xrange(1000):
        puzzle = _rotate(puzzle, randint(0,3))
        puzzle = _exchange_digit(puzzle, (randint(1,9), randint(1,9)))
        puzzle = _exchange_column(puzzle, (randint(0,2), randint(0,2)), randint(0,2))
        puzzle = _exchange_block(puzzle, (randint(0,2), randint(0,2)))
    return puzzle

def _given(puzzle):
    return reduce( lambda x, y: x + len(y), puzzle, 0 )

def _count_column(puzzle, j):
    return reduce ( lambda x, y: x + (1 if j in y else 0), puzzle, 0)

def _count_line(puzzle, i):
    return len(puzzle[i])

def _rotate(puzzle, angle):
    if angle == 0:
        return puzzle
    else:
        if angle == 1:
            return [{j: puzzle[8-j][i] for j in xrange(9)} for i in xrange(9)]
        
        elif angle == 2:
            return [{j: puzzle[8-i][8-j] for j in xrange(9)} for i in xrange(9)]

        elif angle == 3:
            return [{j: puzzle[j][8-i] for j in xrange(9)} for i in xrange(9)]
            

def _exchange_digit(puzzle, (dig1, dig2)):
    if dig1 == dig2:
        return puzzle
    return [{j: (dig1 if puzzle[i][j] == dig2 else dig2)                      \
                      if puzzle[i][j] in (dig1, dig2) else puzzle[i][j]       \
                      for j in xrange(9)} for i in xrange(9)]

def _exchange_column(puzzle, (colu1, colu2), block):
    if colu1 == colu2:
        return puzzle
    c1 = colu1 + 3*block
    c2 = colu2 + 3*block
    return [{j: (puzzle[i][c1] if j == c2 else puzzle[i][c2])                 \
                             if j in (c1,c2) else puzzle[i][j]                \
                             for j in xrange(9)} for i in xrange(9)]

def _exchange_block(puzzle, (b1,b2)):
    if b1 == b2:
        return puzzle
    return [{j: (puzzle[i][b1*3+j%3] if j/3 == b2 else puzzle[i][b2*3+j%3])   \
                    if j/3 in (b1,b2) else puzzle[i][j]                       \
                    for j in xrange(9)} for i in xrange(9)]

def _dig(puzzle, i, j):
    possible_values = range(1,10)
    possible_values.remove(puzzle[i][j])
    puzzle_formated = [[{"possibilities": [puzzle[x][y]] if y in puzzle[x] else range(1,10), \
                         "checked": False} for y in xrange(9)] for x in xrange(9)]
    for x in possible_values:
        puzzle_formated[i][j]["possibilities"] = [x]
        try:
            solve(puzzle_formated)
            raise UnsolvablePuzzleException("Try another")
        except InvalidTableException:
            pass
    puzzle[i].pop(j)
    return puzzle