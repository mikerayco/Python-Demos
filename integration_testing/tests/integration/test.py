import unittest

import requests

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_sum_api_call(self):
        """
        Test the sum api call
        """
        url = 'http://127.0.0.1:5000/sum'
        query_str = {'num1': 1, 'num2': 2}
        r = requests.get(url, params=query_str)
        result = int(r.text)
        self.assertEqual(result,3)

    if __name__ == '__main__':
        unittest.main()