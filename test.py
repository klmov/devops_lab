import unittest
import task6


class TestPyInfo(unittest.TestCase):
    """Unittest Class"""
    def setUp(self):
        """Init"""
    def test_getData(self):
        self.assertTrue(type(task6.getData()) is dict)

    def test_Pyinfo(self):
        self.assertTrue(task6.jsonOut(task6.getData()) is None)
        self.assertTrue(task6.yamlOut(task6.getData()) is None)

    def tearDown(self):
        """Finish"""

if __name__ == '__main__':
    unittest.main()
