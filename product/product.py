
class Product:
    def __init__(self, jsonprod):
        self.raw = jsonprod
        self.categoryTree = [c.strip() for c in self.raw["CATEGORYTEXT"].split('>')]

    def getItemId(self):
        return self.raw["ITEM_ID"]

    def getProductNo(self):
        return self.raw["PRODUCTNO"]

    def getManufacturer(self):
        return self.raw["MANUFACTURER"]

    def getProductName(self):
        return self.raw["PRODUCTNAME"]

    def getProduct(self):
        return self.raw["PRODUCT"]

    def getDescription(self):
        return self.raw["DESCRIPTION"]

    def getUrl(self):
        return self.raw["URL"]

    def getImgUrl(self):
        return self.raw["IMGURL"]

    def getPrice(self):
        return int(self.raw["PRICE_VAT"])

    def getCategory(self):
        return self.raw["CATEGORYTEXT"]

    def getDeliveryDate(self):
        return int(self.raw["DELIVERY_DATE"])

    def getCategoryId(self):
        return self.raw["ITEMGROUP_ID"]

    def getCategoryTree(self):
        return self.categoryTree
