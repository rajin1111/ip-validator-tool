import unittest
from src.ip_validator import is_valid_IPv4, is_valid_IPv6, get_ip_type

class TestIPValidator(unittest.TestCase):

    def test_ipv4_valid(self):
        self.assertTrue(is_valid_IPv4("192.168.1.1"))
        self.assertEqual(get_ip_type("192.168.1.1"), "IPv4")

    def test_ipv4_invalid(self):
        self.assertFalse(is_valid_IPv4("256.0.0.1"))
        self.assertEqual(get_ip_type("256.0.0.1"), "Invalid")

    def test_ipv6_valid(self):
        self.assertTrue(is_valid_IPv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
        self.assertEqual(get_ip_type("2001:0db8:85a3:0000:0000:8a2e:0370:7334"), "IPv6")

    def test_ipv6_invalid(self):
        self.assertFalse(is_valid_IPv6("2001:xyz:123"))
        self.assertEqual(get_ip_type("2001:xyz:123"), "Invalid")

if __name__ == '__main__':
    unittest.main()