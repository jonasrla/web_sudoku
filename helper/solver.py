from random import randint, shuffle, choice
from time import clock
from _utils import InvalidTableException, copy_table

def solve(table):

    table = _check_table(table)

    if _is_done(table):
        return table
    else:
        coordinates = _get_minimum_array(table)
        
        trials = table[coordinates[0]][coordinates[1]]["possibilities"][:]

        shuffle(trials)

        for elem in trials:
            try:
                ctable = copy_table(table)
                ctable[coordinates[0]][coordinates[1]]["possibilities"] = [elem]
                # print_table(ctable)
                # print
                return solve(ctable)
            except InvalidTableException:
                pass
        # print "subiu"
        raise InvalidTableException("Nao ha solucao")

def _is_done(table):
    for line in table:
        for elem in line:
            if len(elem["possibilities"]) > 1:
                return False
            elif len(elem["possibilities"]) == 0:
                raise InvalidTableException("Celula Vazia")
    return True

def _check_table(table):
    #find unchecked
    #clean other possibilities
    #raise exception if some possibility becomes void

    while not _is_check_done(table):
        unchecked_set = _find_unchecked(table)
        for value,x,y in unchecked_set:
            _fix_house(table,value,x,y)
            _fix_column(table,value,x,y)
            _fix_line(table,value,x,y)
            table[y][x]["checked"] = True

    return table


def _is_check_done(table):
    for line in table:
        for elem in line:
            if len(elem["possibilities"]) == 1 and not elem["checked"]:
                return False
    return True


def _find_unchecked(table):
    result = set()
    for i, line in enumerate(table):
        for j, elem in enumerate(line):
            if len(elem["possibilities"]) == 1 and not elem["checked"]:
                result.add((elem["possibilities"][0],j,i))
    return result


def _fix_house(table,value,x,y):
    x0 = (x/3)*3 + 1
    y0 = (y/3)*3 + 1
    to_fix = [(x0-1,y0-1),(x0-1,y0),(x0-1,y0+1),(x0,y0-1),(x0,y0),(x0,y0+1),(x0+1,y0-1),(x0+1,y0),(x0+1,y0+1)]
    to_fix.remove((x,y))
    for i,j in to_fix:
        _fix(table,value,i,j)


def _fix_column(table,value,x,y):
    columns = range(len(table))
    columns.remove(y)
    for j in columns:
        _fix(table,value,x,j)


def _fix_line(table,value,x,y):
    lines = range(len(table))
    lines.remove(x)
    for i in lines:
        _fix(table,value,i,y)

def _fix(table, value, x, y):
    try:
        table[y][x]["possibilities"].remove(value)
    except ValueError:
        pass
    if len(table[y][x]["possibilities"]) < 1:
        raise InvalidTableException("Nao deu!")

def _get_minimum_array(table):
    result = list()
    size = len(table)
    for i, line in enumerate(table):
        for j, elem in enumerate(line):
            if not elem["checked"]:
                if not result:
                    result.append((i,j))
                    size = len(elem["possibilities"])
                elif len(elem["possibilities"]) == size:
                    result.append((i,j))
                elif len(elem["possibilities"]) < size:
                    result = list()
                    result.append((i,j))
                    size = len(elem["possibilities"])
    return choice(result)

