import random
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from .mapper import MapParamValue


class RandomScorer:
    def __init__(self):
        pass

    def getScore(self, baseproduct, products, userpreference):
        result = []
        for _ in products:
            result.append(random.uniform(0, 100))
        return result


class CategoryScorer:
    def __init__(self):
        self.mapper = MapParamValue()

    def getScore(self, baseproduct, products, userpreference):
        rawscores = self.mapper.map(products)
        for product in rawscores:
            for key in product:
                product[key] = product[key] * userpreference.get(key, 0.5)
        baseproductid = None
        for i in range(len(products)):
            if products[i].getItemId() == baseproduct.getItemId():
                baseproductid = i
                break

        diffs = self.getProsCons(baseproductid, rawscores)

        unnormalized = np.array([sum(product.values())
                                 for product in rawscores]).reshape(-1, 1)
        normalized = MinMaxScaler((0, 100)).fit_transform(unnormalized)
        return list(normalized.reshape(-1)), diffs

    def getProsCons(self, baseproductid, scores):
        relativescores = []
        for product in scores:
            res = []
            for key in product:
                res.append((key, scores[baseproductid][key] - product[key]))
            relativescores.append(res)
        res = []
        for product in relativescores:
            prodsorted = sorted(product, key=lambda x: x[1])
            best = prodsorted[:3]
            worst = prodsorted[-3:]
            subres = {"pros": [], "cons": []}
            for b in best:
                if b[1] != 0.0:
                    subres["pros"].append({"key": b[0], "reldiff": b[1]})

            for b in worst:
                if b[1] != 0.0:
                    subres["cons"].append({"key": b[0], "reldiff": b[1]})
            res.append(subres)
        return res
