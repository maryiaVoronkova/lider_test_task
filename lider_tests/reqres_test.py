import unittest
import requests

from data.reqres_data import *
from utils.reqres_utils import get_all_names


class ReqresTestCases(unittest.TestCase):

    def test_single_user(self):
        expected_status_code = 200
        expected_name = "Janet"

        response = requests.get(ENDPOINT)
        status_code = response.status_code
        assert status_code == expected_status_code, \
            f"Actual status code is not {expected_status_code}, but {status_code}"

        result = response.json()
        names = get_all_names(result)
        assert expected_name not in names, f"Response names contains {expected_name}"


if __name__ == '__main__':
    unittest.main()
