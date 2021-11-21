import unittest

from servers_skeleton import ListServer, Product, Client, MapServer, TooManyProductsFoundError


class ProductTest(unittest.TestCase):

    def test_is_not_none(self):
        self.assertIsNotNone(Product('D12', 19))

    def test_product_works_properly_1(self):
        product = Product('D12', 19)
        self.assertEqual(product.n_letters, 1)
        self.assertEqual(product.price, 19)
        self.assertEqual(product.name, 'D12')

    def test_product_works_properly_2(self):
        product = Product('AAAAAA123456789', 40)
        self.assertEqual(product.n_letters, 6)
        self.assertEqual(product.price, 40)
        self.assertEqual(product.name, 'AAAAAA123456789')

    def test_product_works_properly_3(self):
        product = Product('DsPr1224', 124)
        self.assertEqual(product.n_letters, 4)
        self.assertEqual(product.price, 124)
        self.assertEqual(product.name, 'DsPr1224')


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


class ListServerTest(unittest.TestCase):

    def test_constructor(self):
        product_1 = Product('A123', 1)
        product_2 = Product('a123', 2)
        list_server = ListServer([product_1, product_2])

        self.assertEqual(list_server.products, [product_1, product_2])

    def test_get_entries(self):
        product_1 = Product('A123', 1)
        product_2 = Product('a123', 2)
        product_3 = Product('aA123', 3)
        product_4 = Product('A1', 4)
        product_5 = Product('a1', 5)
        product_6 = Product('aA1', 6)
        list_of_products = [product_1, product_2, product_3, product_4, product_5, product_6]
        list_server = ListServer(list_of_products)

        self.assertEqual(list_server.get_all_products(1), [product_1, product_2, product_4, product_5])
        self.assertEqual(list_server.get_all_products(2), [product_3, product_6])

    def test_too_many_products(self):
        # TODO: Ustaw wartość atrybutu n_max_returned_entries na 5 lub mniej
        product_1 = Product('A123', 1)
        product_2 = Product('a123', 2)
        product_3 = Product('B123', 3)
        product_4 = Product('A123', 4)
        product_5 = Product('a123', 5)
        product_6 = Product('B123', 6)
        list_of_products = [product_1, product_2, product_3, product_4, product_5, product_6]
        list_server = ListServer(list_of_products)

        self.failUnlessRaises(TooManyProductsFoundError, list_server.get_all_products)


class MapServerTest(unittest.TestCase):

    def test_constructor(self):
        product_1 = Product('A123', 1)
        product_2 = Product('a123', 2)
        list_server = MapServer([product_1, product_2])

        self.assertEqual(list_server.products, {"A123": product_1, "a123": product_2})

    def test_get_entries(self):
        product_1 = Product('A123', 1)
        product_2 = Product('a123', 2)
        product_3 = Product('aA123', 3)
        product_4 = Product('A1', 4)
        product_5 = Product('a1', 5)
        product_6 = Product('aA1', 6)
        list_of_products = [product_1, product_2, product_3, product_4, product_5, product_6]

        map_server = MapServer(list_of_products)
        self.assertEqual(map_server.get_all_products(1), [product_1, product_2, product_4, product_5])
        self.assertEqual(map_server.get_all_products(2), [product_3, product_6])

    def test_too_many_products(self):
        # TODO: Ustaw wartość atrybutu n_max_returned_entries na 5 lub mniej
        product_1 = Product('A123', 1)
        product_2 = Product('a123', 2)
        product_3 = Product('B123', 3)
        product_4 = Product('A1', 4)
        product_5 = Product('a1', 5)
        product_6 = Product('B1', 6)
        list_of_products = [product_1, product_2, product_3, product_4, product_5, product_6]
        map_server = MapServer(list_of_products)

        self.failUnlessRaises(TooManyProductsFoundError, map_server.get_all_products)
 
 
if __name__ == '__main__':
    unittest.main()
