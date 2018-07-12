# coding=utf-8

import unittest


class Mydemo(unittest.TestCase):

    def test1(self):
        print("excute test1")

    def test2(self):
        if unittest.TestCase._resultForDoCleanups.failures or self._resultForDoCleanups.errors:
            raise unittest.SkipTest("{} do not excute because {} is failed".format(self._testMethodName,
                                                                                   self._resultForDoCleanups.failures[
                                                                                       0][0]._testMethodName))

        print("excute test2")
        raise AssertionError("test2 fail")

    def test3(self):
        if self._resultForDoCleanups.failures or self._resultForDoCleanups.errors:
            raise unittest.SkipTest("{} do not excute because {} is failed".format(self._testMethodName,
                                                                                   self._resultForDoCleanups.failures[
                                                                                       0][0]._testMethodName))

        print("excute test3")


if __name__ == '__main__':
    unittest.main()