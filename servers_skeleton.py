#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from typing import Optional
 
 
class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)
    
    def __init__(self,name:str,price:float):
        if len(name)<2:
            raise ValueError

        if not(65<=int(name[0])<=122): # sprawdza czy występuje co najmniej jedna litera
            raise ValueError
        if not(48<=int(name[-1])<=57): # sprawdza czy wsytępuje co najmnije jedna cyfra
            raise ValueError
        if price<0:
            raise ValueError
        self.name=name 
        self.price=price


    def __eq__(self, other):
        return None  # FIXME: zwróć odpowiednią wartość
 
    def __hash__(self):
        return hash((self.name, self.price))
 
 
class TooManyProductsFoundError:
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass
 
 
# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania
 
class ListServer:
    pass
 
 
class MapServer:
    pass
 
 
class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
 
    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()