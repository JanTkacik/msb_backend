
class UserFilter:
    def __init__(self, categoryId, pricefrom=None, priceto=None):
        self.categoryId = categoryId
        self.pricefrom = pricefrom
        self.priceto = priceto

    def isOK(self, product):
        if product.getCategoryId() == self.categoryId:
            price = product.getPrice()
            if self.pricefrom is None or price >= self.pricefrom:
                if self.priceto is None or price <= self.priceto:
                    return True
        return False
