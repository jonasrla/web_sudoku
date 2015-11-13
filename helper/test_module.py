import unittest
import _utils
import solution_creator
# from puzzle_creator import *
import digger
import solver

class test_solver_functions(unittest.TestCase):
    def setUp():
        self.table = solution_creator._new_table()
        
        self.pseudo_solved_table = [[{"possibilities":[randint(1,9)] "checked": True} for i in xrange(9)] for j in xrange(9)]
        
        self.invalid_table = [[{"possibilities":[randint(1,9)] "checked": True} for i in xrange(9)] for j in xrange(9)]
        self.invalid_table[randint(0,8)][randint(0,8)]["possibilities"] = []
        
        self.unchecked_table = solution_creator._new_table()
        self.unchecked_table[randint(0,8)][randint(0,8)]["possibilities"].remove(randint(1,9))
        
        self.dead_end_table = solution_creator._new_table()
        column = randint(0,8)
        value = randint(1,9)
        self.dead_end_table[randint(0,3)][column]["possibilities"] = [value]
        self.dead_end_table[randint(4,8)][column]["possibilities"] = [value]
    
    def test_is_done(self):
        self.assertFalse(self.table)
        self.assertTrue(self.pseudo_solved_table)
        with self.assertRaises():
            _is_done(self.invalid_table)
        simple_table = solution_creator._new_table(3)
        # print _is_done(simple_table)
        # simple_table[0][0]["possibilities"] = [1]
        # simple_table[0][1]["possibilities"] = [2]
        # simple_table[0][2]["possibilities"] = [3]
        # simple_table[1][0]["possibilities"] = [2]
        # simple_table[1][1]["possibilities"] = [3]
        # simple_table[1][2]["possibilities"] = [1]
        # simple_table[2][0]["possibilities"] = [3]
        # simple_table[2][1]["possibilities"] = [1]
        # simple_table[2][2]["possibilities"] = [2]
        # print _is_done(simple_table)

    def test_check_table(self):
        with self.assertRaises():
            check_table(self.dead_end_table)

        # simple_table = solution_creator._new_table(3)
        # simple_table[0][0]["possibilities"] = [1]
        # check_table(simple_table)
        # _utils.print_table(simple_table)
        # simple_table[0][2]["possibilities"] = [1]
        # try:
        #     check_table(simple_table)
        # except InvalidTableException:
        #     print "Exception Successifully Raised"

    def test_fix(self):
        simple_table = solution_creator._new_table(3)
        solver._fix(simple_table,1,0,0)
        _utils.print_table(simple_table)
        simple_table[0][0]={"possibilities": [1], "checked": False}
        solver._fix(simple_table,1,0,0)
        _utils.print_table(simple_table)

    def test_fix_line(self):
        simple_table = solution_creator._new_table(3)
        solver._fix_line(simple_table,1,0,0)
        _utils.print_table(simple_table)

    def test_fix_column(self):
        simple_table = solution_creator._new_table(3)
        solver._fix_column(simple_table,1,0,0)
        _utils.print_table(simple_table)

    def test_fix_house(self):
        simple_table = solution_creator._new_table(6)
        solver._fix_house(simple_table,1,0,0)
        _utils.print_table(simple_table)

    def test_find_unchecked(self):
        simple_table = solution_creator._new_table(3)
        simple_table[0][0]["possibilities"] = [1]
        simple_table[1][0]["possibilities"] = [3]
        simple_table[1][0]["checked"] = True
        unchecked_set = find_unchecked(simple_table)
        for elem in unchecked_set:
            print "value: %s\nx: %s\ny: %s" % elem

    def test_get_minimum_array(self):
        simple_table = solution_creator._new_table(3)
        fix(simple_table, 2,1,2)
        fix(simple_table, 3,1,1)
        simple_table[1][1]["checked"] = True
        coordinates = get_minimum_array(simple_table)
        print "x: %s\ny: %s" % (coordinates[1],coordinates[0])

    def test_is_check_done(self):
        simple_table = solution_creator._new_table(3)
        print is_check_done(simple_table)
        simple_table[0][0]["possibilities"] = [1]
        print is_check_done(simple_table)


class test_solution_creator_functions(unittest.TestCase):
    def setUp():
        pass

    def test_new_table(self):
        table = solution_creator._new_table()
        result = recursive_solution(table)
        _utils.print_table(result)

    def test_get_solution(self):
        pass

    def test_create_solution(self):
        pass


class test_utils_functions(unittest.TestCase):
    def setUp():
        pass

    def test_print_table(self):
        _utils.print_table(create_solution())

    def test_copy_table(self):
        pass

    def test_clear_table(self):
        pass

class test_puzzle_creator_functions(unittest.TestCase):
    def setUp():
        pass

    def test_create_solution(self):
        pass

    def test_get_parameters(self):
        pass
