from .product import Product
import json


class FileProductRepository:

    categories = {}

    def __init__(self, path):
        self.products = []
        with open(path, encoding='utf-8') as json_data:
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
        key = userfilter.key()
        if key in FileProductRepository.categories:
            return FileProductRepository.categories[key]
        returnlist = []
        for product in self.products:
            if userfilter.isOK(product):
                product.raw.pop('DESCRIPTION')
                product.raw.pop('DELIVERY')
                returnlist.append(product)
        
        FileProductRepository.categories[key] = returnlist
        return FileProductRepository.categories[key]
