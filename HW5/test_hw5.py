# -*- coding: utf-8 -*-

from testing import ModuleTestBase, FunctionTestReturningFloat, StagedTest

class Homework5Test (ModuleTestBase):

    fun_name = "interpolate"

    s0_tests = (
        # integer x_test, not equal to any sample
        (((1, 3, 5), (1, 9, 25), 2), 5.0, 'closest values: x[0] == 1 < 2.0 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 5.0'),
        (((1, 3, 5), (1, 9, 25), 4), 17.0, 'closest values: x[1] == 3 < 4.0 < x[2] == 5; y[1] == 9 and y[2] == 25; a = 8.0, b = -15.0, answer = 17.0'),
        # non-integer x_test
        (((1, 3, 5), (1, 9, 25), 1.25), 2.0, 'closest values: x[0] == 1 < 1.25 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 2.0'),
        (((1, 3, 5), (1, 9, 25), 1.5), 3.0, 'closest values: x[0] == 1 < 1.5 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 3.0'),
        (((1, 3, 5), (1, 9, 25), 1.75), 4.0, 'closest values: x[0] == 1 < 1.75 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 4.0'),
        (((1, 3, 5), (1, 9, 25), 2.25), 6.0, 'closest values: x[0] == 1 < 2.25 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 6.0'),
        (((1, 3, 5), (1, 9, 25), 2.5), 7.0, 'closest values: x[0] == 1 < 2.5 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 7.0'),
        (((1, 3, 5), (1, 9, 25), 2.75), 8.0, 'closest values: x[0] == 1 < 2.75 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 8.0'),
        (((1, 3, 5), (1, 9, 25), 3.25), 11.0, 'closest values: x[1] == 3 < 3.25 < x[2] == 5; y[1] == 9 and y[2] == 25; a = 8.0, b = -15.0, answer = 11.0'),
        (((1, 3, 5), (1, 9, 25), 3.5), 13.0, 'closest values: x[1] == 3 < 3.5 < x[2] == 5; y[1] == 9 and y[2] == 25; a = 8.0, b = -15.0, answer = 13.0'),
        (((1, 3, 5), (1, 9, 25), 3.75), 15.0, 'closest values: x[1] == 3 < 3.75 < x[2] == 5; y[1] == 9 and y[2] == 25; a = 8.0, b = -15.0, answer = 15.0'),
        (((1, 3, 5), (1, 9, 25), 4.25), 19.0, 'closest values: x[1] == 3 < 4.25 < x[2] == 5; y[1] == 9 and y[2] == 25; a = 8.0, b = -15.0, answer = 19.0'),
        (((1, 3, 5), (1, 9, 25), 4.5), 21.0, 'closest values: x[1] == 3 < 4.5 < x[2] == 5; y[1] == 9 and y[2] == 25; a = 8.0, b = -15.0, answer = 21.0'),
        (((1, 3, 5), (1, 9, 25), 4.75), 23.0, 'closest values: x[1] == 3 < 4.75 < x[2] == 5; y[1] == 9 and y[2] == 25; a = 8.0, b = -15.0, answer = 23.0'),
        # x_test equal to a sample point
        (((1, 3, 5), (1, 9, 25), 1.0), 1, '1.0 == x[0], the answer is y[0] == 1'),
        (((1, 3, 5), (1, 9, 25), 3.0), 9, '3.0 == x[1], the answer is y[1] == 9'),
        (((1, 3, 5), (1, 9, 25), 5.0), 25, '5.0 == x[2], the answer is y[2] == 25'),
        # only two samples
        (((1, 3), (1, 9), 2), 5.0, 'closest values: x[0] == 1 < 2.0 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 5.0'),
        (((3, 5), (9, 25), 4), 17.0, 'closest values: x[1] == 3 < 4.0 < x[2] == 5; y[1] == 9 and y[2] == 25; a = 8.0, b = -15.0, answer = 17.0'),
        (((1, 3), (1, 9), 1.5), 3.0, 'closest values: x[0] == 1 < 1.5 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 3.0')
    )

    s1_tests = (
        (((-3.1415926535897931, -2.0943951023931957, -1.0471975511965979, 0.0, 1.0471975511965974, 2.0943951023931948, 3.1415926535897931), (-1.2246467991473532e-16, -0.86602540378443849, -0.86602540378443871, 0.0, 0.86602540378443849, 0.86602540378443893, 1.2246467991473532e-16), -2.6179938779914944), -0.4330127018922192, 'closest values: x[0] == -3.141592653589793 < -2.617994 < x[1] == -2.0943951023931957; y[0] == -1.2246467991473532e-16 and y[1] == -0.8660254037844385; a = -0.826993, b = -2.598076, answer = -0.433013'),
        (((-3.1415926535897931, -2.0943951023931957, -1.0471975511965979, 0.0, 1.0471975511965974, 2.0943951023931948, 3.1415926535897931), (-1.2246467991473532e-16, -0.86602540378443849, -0.86602540378443871, 0.0, 0.86602540378443849, 0.86602540378443893, 1.2246467991473532e-16), -1.570796326794897), -0.8660254037844386, 'closest values: x[1] == -2.0943951023931957 < -1.570796 < x[2] == -1.0471975511965979; y[1] == -0.8660254037844385 and y[2] == -0.8660254037844387; a = -0.000000, b = -0.866025, answer = -0.866025'),
        (((-3.1415926535897931, -2.0943951023931957, -1.0471975511965979, 0.0, 1.0471975511965974, 2.0943951023931948, 3.1415926535897931), (-1.2246467991473532e-16, -0.86602540378443849, -0.86602540378443871, 0.0, 0.86602540378443849, 0.86602540378443893, 1.2246467991473532e-16), -0.523598775598299), -0.4330127018922194, 'closest values: x[2] == -1.0471975511965979 < -0.523599 < x[3] == 0.0; y[2] == -0.8660254037844387 and y[3] == 0.0; a = 0.826993, b = 0.000000, answer = -0.433013'),
        (((-3.1415926535897931, -2.0943951023931957, -1.0471975511965979, 0.0, 1.0471975511965974, 2.0943951023931948, 3.1415926535897931), (-1.2246467991473532e-16, -0.86602540378443849, -0.86602540378443871, 0.0, 0.86602540378443849, 0.86602540378443893, 1.2246467991473532e-16), 0.5235987755982988), 0.43301270189221935, 'closest values: x[3] == 0.0 < 0.523599 < x[4] == 1.0471975511965974; y[3] == 0.0 and y[4] == 0.8660254037844385; a = 0.826993, b = 0.000000, answer = 0.433013'),
        (((-3.1415926535897931, -2.0943951023931957, -1.0471975511965979, 0.0, 1.0471975511965974, 2.0943951023931948, 3.1415926535897931), (-1.2246467991473532e-16, -0.86602540378443849, -0.86602540378443871, 0.0, 0.86602540378443849, 0.86602540378443893, 1.2246467991473532e-16), 1.5707963267948961), 0.8660254037844387, 'closest values: x[4] == 1.0471975511965974 < 1.570796 < x[5] == 2.094395102393195; y[4] == 0.8660254037844385 and y[5] == 0.8660254037844389; a = 0.000000, b = 0.866025, answer = 0.866025'),
        (((-3.1415926535897931, -2.0943951023931957, -1.0471975511965979, 0.0, 1.0471975511965974, 2.0943951023931948, 3.1415926535897931), (-1.2246467991473532e-16, -0.86602540378443849, -0.86602540378443871, 0.0, 0.86602540378443849, 0.86602540378443893, 1.2246467991473532e-16), 2.6179938779914935), 0.4330127018922201, 'closest values: x[5] == 2.094395102393195 < 2.617994 < x[6] == 3.141592653589793; y[5] == 0.8660254037844389 and y[6] == 1.2246467991473532e-16; a = -0.826993, b = 2.598076, answer = 0.433013')
    )
    
    def test_homework_5(self, _suppress_output = False):
        ok, fun, msg = self.find_function(self.fun_name)
        if not ok:
            return False, msg
        if fun is None:
            return False, msg
        ft0 = FunctionTestReturningFloat(fun, self.s0_tests,
                                         precision = 0.0001,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        ft1 = FunctionTestReturningFloat(fun, self.s1_tests,
                                         precision = 0.0001,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        st = StagedTest((ft0, ft1), self.verbose, self.raise_exceptions)
        ok, msg = st.run()
        return ok, msg


    def run(self):
        print("checking function " + self.fun_name +
              " in file " + self.filepath)
        print()
        ok, msg = self.test_homework_5(False)
        print(msg)

    ## end Homework5Test


## To produce less verbose output, change verbose from 3 to 2 or 1:

Homework5Test("homework5.py", verbose = 3).run()
