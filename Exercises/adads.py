#!/bin/python3

import math
import os
import random
import re
import sys



class Item:
    # Implement the Item here
    def __init__(self, name ,price):
        self.name = name
        self.price = price

class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self, items_list = []):
        self.items_list = items_list
    def total(self):
        x = 0
        if(len(self.items_list) == 0):
            return x
        for i in self.items_list:
            x += i.price
        return x
    def add(self, item_to_add):
        self.items_list.append(item_to_add)
    def __len__(self):
        return len(self.items_list)
if __name__ == '__main__':

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            print("OUT ----- LEN = " + str(len(cart)) + "\n")
        elif command == "total":
            print("OUT ----- TOTAL = " + str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
