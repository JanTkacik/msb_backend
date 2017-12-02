from .product import Product
import json


class FileProductRepository:
    def __init__(self, path):
        self.products = []
        with open(path) as json_data:
            loaded = json.load(json_data)
            for prod in loaded:
                self.products.append(Product(prod))

    def getAllProducts(self):
        return self.products

    def getProductByItemId(self, itemId):
        for product in self.products:
            if product.getItemId() == itemId:
                return product
        return None

    def getProductsByUserFilter(self, userfilter):
        returnlist = []
        for product in self.products:
            if userfilter.isOK(product):
                returnlist.append(product)
        return returnlist
