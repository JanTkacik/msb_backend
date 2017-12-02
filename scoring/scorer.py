import random
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from .mapper import MapParamValue
import math
from .convertors import get_convertor


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
        user_pref_scores = []
        for i, product in enumerate(rawscores):
            user_pref_scores.append({})
            for key in product:
                user_pref_scores[i][key] = product[key] * \
                    self.recalculate_user_preference(
                        userpreference.get(key, 0.5))
        baseproductid = None
        for i in range(len(products)):
            if products[i].getItemId() == baseproduct.getItemId():
                baseproductid = i
                break

        diffs = self.getProsCons(
            baseproductid, user_pref_scores, baseproduct.getCategory())

        unnormalized = np.array([sum(product.values())
                                 for product in user_pref_scores]).reshape(-1, 1)
        normalized = MinMaxScaler((0, 100)).fit_transform(unnormalized)
        return list(normalized.reshape(-1)), diffs

    def getProsCons(self, baseproductid, scores, category_name):
        category_mappers = self.mapper.get_category_mappers(category_name)
        relativescores = []
        for product in scores:
            res = []
            for key in product:
                ratio = 1
                if scores[baseproductid][key] - 0.001 > 0:
                    ratio = (product[key] - scores[baseproductid][key]) / scores[baseproductid][key]

                res.append((key, scores[baseproductid][key] - product[key], ratio))
            relativescores.append(res)
        res = []
        for product in relativescores:
            prodsorted = sorted(product, key=lambda x: x[1])
            best = prodsorted[:3]
            worst = prodsorted[-3:]
            subres = {"pros": [], "cons": []}
            for b in best:
                ratio = abs(round(b[2] * 100))
                if b[1] != 0.0:
                    convertor = get_convertor(category_mappers[b[0]]['convertor'])
                    reason = convertor.get_reason(ratio, category_mappers[b[0]]['reason']['pros'])
                    subres["pros"].append({"key": b[0], "reldiff": b[1], "reason": reason})
            for b in worst:
                ratio = abs(round(b[2] * 100))
                if b[1] != 0.0:
                    convertor = get_convertor(category_mappers[b[0]]['convertor'])
                    reason = convertor.get_reason(ratio, category_mappers[b[0]]['reason']['con'])
                    subres["cons"].append({"key": b[0], "reldiff": b[1], "reason": reason})
            res.append(subres)
        return res

    def recalculate_user_preference(self, userpref):
        if userpref <= 0.0:
            return 0

        final_weight = pow(10000, userpref - 0.5)
        if final_weight > 100:
            return 100

        return final_weight
