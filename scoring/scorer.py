import random
from sklearn.preprocessing import MinMaxScaler
import numpy as np


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
        self.mapper = None

    def getScore(self, products, userpreference):
        rawscores = self.mapper(products)
        for product in rawscores:
            for key in product:
                product[key] = product[key] * userpreference[key]
        unnormalized = np.array[sum(product.values()) for product in rawscores]
        normalized = MinMaxScaler((0, 100)).fit_transform(unnormalized)
        return normalized
