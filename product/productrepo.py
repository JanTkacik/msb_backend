from .product import Product
import json


class FileProductRepository:
    def __init__(self, path):
        self.products = []
        with open(path) as json_data:
            loaded = json.load(json_data)
            shop = loaded["SHOP"]["SHOPITEM"]
            for prod in shop:
                self.products.append(Product(prod))

    def getAllProducts(self):
        return self.products
