import unittest

import calculartion

is_test = True

class CalTest(unittest.TestCase):
    def setUp(self):
        """
        lesson.164
        """
        print('setUp')
        self.cal = calculartion.Cal()

    def tearDown(self):
        """
        lesson.164
        """
        print('tearDown')
        del self.cal

    # @unittest.skip('skip!')
    @unittest.skipIf(not is_test, 'skip!')
    def test_add_num_and_double(self):
        """
        lesson.162
        """
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        """
        lesson.163
        
        test raise exception.
        """
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')

if __name__ == '__main__':
    unittest.main()