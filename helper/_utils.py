class InvalidTableException(Exception):
    pass

class DoubledSolutionPuzzleException(Exception):
    pass

def new_table():
    return [[{"possibilities": range(1,10), "checked": False} for i in xrange(9)] for j in xrange(9)]

def print_table(table, coloured=True):
    green = "\033[92m"
    red = "\033[91m"
    end = "\033[0m"
    size = len(table)
    try:
        for line in table:
            print  " ".join([(green if i["checked"] else red) + "%s" + end for i in line]) % tuple([elem["possibilities"] for elem in line])
    except Exception:
        for line in table:
            print "%s "*9 % tuple(line)

def copy_table(table):
    size = len(table)
    return [[{"possibilities": table[j][i]["possibilities"][:], "checked": table[j][i]["checked"]} for i in xrange(size)] for j in xrange(size)]

def clear_table(table):
    size = len(table)
    return [{i:table[j][i]["possibilities"][0] for i in xrange(size)} for j in xrange(size)]