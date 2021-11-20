import unittest
from collections import Counter
 
from servers_skeleton import ListServer, Product, Client, MapServer
 
server_types = (ListServer, MapServer)


class ProductTest(unittest.TestCase):

    def test_is_not_none(self):
        self.assertIsNotNone(Product('D12', 19))


class ProductValueErrorTest(unittest.TestCase):

    def test_only_letters_in_name(self):
        self.failUnlessRaises(ValueError, Product, 'DP', 1)

    def test_only_numbers_in_name(self):
        self.failUnlessRaises(ValueError, Product, '123', 1)

    def test_mixed_signes_in_name_1(self):
        self.failUnlessRaises(ValueError, Product, '1DP3', 1)

    def test_mixed_signes_in_name_2(self):
        self.failUnlessRaises(ValueError, Product, 'D1P3', 1)

    def test_wrong_signes_in_name_1(self):
        self.failUnlessRaises(ValueError, Product, 'AB@12', 1)

    def test_wrong_signes_in_name_2(self):
        self.failUnlessRaises(ValueError, Product, 'A 12', 1)

    def test_wrong_signes_in_name_3(self):
        self.failUnlessRaises(ValueError, Product, 'A{12', 1)

    def test_zero_value_error(self):
        self.failUnlessRaises(ValueError, Product, 'D12', 0)

    def test_negative_value_error(self):
        self.failUnlessRaises(ValueError, Product, 'D12', -1)


class ProductEqualityTest(unittest.TestCase):

    def test_equality(self):
        product_1 = Product('D12', 1)
        product_2 = Product('D12', 1)
        self.assertEqual(product_1, product_2)

    def test_different_letters(self):
        product_1 = Product('D12', 1)
        product_2 = Product('S12', 1)
        self.assertNotEqual(product_1, product_2)

    def test_case_sensitivity(self):
        product_1 = Product('D12', 1)
        product_2 = Product('d12', 1)
        self.assertNotEqual(product_1, product_2)

    def test_different_numbers(self):
        product_1 = Product('D12', 1)
        product_2 = Product('D21', 1)
        self.assertNotEqual(product_1, product_2)

    def test_different_value(self):
        product_1 = Product('D12', 19)
        product_2 = Product('D12', 9)
        self.assertNotEqual(product_1, product_2)

    def test_completely_different_products(self):
        product_1 = Product('D12', 19)
        product_2 = Product('S12', 9)
        self.assertNotEqual(product_1, product_2)

'''
class ServerTest(unittest.TestCase):
 
    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))
 
 
class ClientTest(unittest.TestCase):
    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))'''
 
 
if __name__ == '__main__':
    unittest.main()
