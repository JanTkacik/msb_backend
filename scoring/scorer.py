import random
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from .mapper import MapParamValue


class RandomScorer:
    def __init__(self):
        pass

    def getScore(self, products, userpreference):
        result = []
        for _ in products:
            result.append(random.uniform(0, 100))
        return result


class CategoryScorer:
    def __init__(self):
        self.mapper = MapParamValue()

    def getScore(self, products, userpreference):
        rawscores = self.mapper.map(products)
        for product in rawscores:
            for key in product:
                product[key] = product[key] * userpreference.get(key, 0.5)

        unnormalized = np.array([sum(product.values())
                                 for product in rawscores]).reshape(-1, 1)
        normalized = MinMaxScaler((0, 100)).fit_transform(unnormalized)
        return list(normalized.reshape(-1))
