#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict, Union


class Product:

    def __init__(self, name: str, price: float):
        # Pętla sprawdza warunki dla każdego znaku w nazwie produku
        for letter_iter in range(len(name)):
            # Jeśli znak jest literą, nic nie rób
            if 65 <= ord(name[letter_iter]) <= 122:
                pass
            # W przeciwnym wypadku...
            else:
                # ...sprawdź czy nie rozpoczął się już ciąg liczb w nazwie
                if 48 <= ord(name[letter_iter]) <= 57:

                    # Jeśli nazwa nie zaczyna się od litery, zwracany jest ValueError
                    if letter_iter == 0:
                        raise ValueError

                    # letter_iter określa teraz liczbę liter na początku nazwy
                    self.n_letters = letter_iter

                    # Pętla sprawdza dla każdego znaku po ciągu liter, czy jest to liczba
                    for number_iter in range(letter_iter, len(name)):
                        if 48 <= ord(name[number_iter]) <= 57:
                            pass

                        # Jeśli któryś znak nie jest liczbą, zwracany jest ValueError
                        else:
                            raise ValueError

                    # Po zakończeniu pomyślnie wewnętrznej pętli kończymy wszelkie iteracje po elementach
                    break

                else:
                    raise ValueError

            # Jeśli w nazwie nie ma żadnych liczb, zwróć ValueError
            if letter_iter == len(name) - 1:
                raise ValueError

        # Jeśli cena produktu jest nielogiczna, zwróć ValueError
        if price <= 0:
            raise ValueError

        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __hash__(self):
        return hash((self.name, self.price))


class TooManyProductsFoundError(Exception):
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass

class ListServer:
    def __init__(self, products: List[Product], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.products: List[Product] = products

    n_max_returned_entries = 5

    def get_all_products(self, n_letters=1) -> List[Product]:
        selected_products = []
        for article in self.products:
            if article.n_letters == n_letters:
                selected_products.append(article)
        if len(selected_products) > self.n_max_returned_entries:
            raise TooManyProductsFoundError
        return selected_products


class MapServer:
    def __init__(self, products: List[Product], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.products: Dict[str, Product] = {p.name: p for p in products}

    n_max_returned_entries = 5

    def get_all_products(self, n_letters=1) -> List[Product]:
        selected_products = []
        for article in self.products.values():
            if article.n_letters == n_letters:
                selected_products.append(article)
        if len(selected_products) > self.n_max_returned_entries:
            raise TooManyProductsFoundError
        return selected_products


class Client:
    def __init__(self, server: Union[MapServer, ListServer]):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            records = self.server.get_all_products(n_letters)
            sum = 0
            for i in records:
                sum += i.price
            if sum != 0:
                return sum
        except:
            return None
