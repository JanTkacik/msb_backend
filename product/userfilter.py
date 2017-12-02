
class UserFilter:
    def __init__(self, categoryTree, matchlevel, pricefrom=None, priceto=None):
        self.matchlevel = matchlevel
        self.categoryTree = categoryTree
        self.pricefrom = pricefrom
        self.priceto = priceto

    def isOK(self, product):
        categoryTree = product.getCategoryTree()
        if len(categoryTree) == len(self.categoryTree):
            for i in range(len(categoryTree)):
                if categoryTree[i] != self.categoryTree[i]:
                    return False
        else:
            return False
        
        price = product.getPrice()
        if self.pricefrom is None or price >= self.pricefrom:
            if self.priceto is None or price <= self.priceto:
                return True
        return False
