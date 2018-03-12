import unittest
import task6


class TestPyInfo(unittest.TestCase):
    """Unittest Class"""
    def setUp(self):
        """Init"""

    def Pytest(self):
        self.assertTrue(task6.jsonOut())
        self.assertTrue(task6.yamlOut())

    def tearDown(self):
        """Finish"""

if __name__ == '__main__':
    unittest.main()
