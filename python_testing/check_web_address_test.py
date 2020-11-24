from main import check_web_address
import unittest

# Unit Test
class TestCheckWebAddress(unittest.TestCase): 
    def test_basic(self):
        testcase = "www.isolveit.herokuapp.com"
        expected = True
        self.assertEqual(check_web_address(testcase), expected)

    def test_empty_str(self):
        testcase = ""
        expected = False
        self.assertEqual(check_web_address(testcase), expected)

    def test_domain_with_path(self):
        testcase = "google.com/maps/accra"
        expected = False
        self.assertEqual(check_web_address(testcase), expected)

    def test_domain_with_at(self):
        testcase = "www@google"
        expected = False
        self.assertEqual(check_web_address(testcase), expected)

    def test_domain_with_underscore_dash(self):
        testcase = "My_Favorite-Blog.US"
        expected = True
        self.assertEqual(check_web_address(testcase), expected)

    def test_url_with_protocol(self):
        testcase = "https://isolveit.herokuapp.com"
        expected = False
        self.assertEqual(check_web_address(testcase), expected)


unittest.main()

# assert type(username) == str, "username must be string"