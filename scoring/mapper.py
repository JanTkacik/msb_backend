from .convertors import get_convertor
import json
from sklearn.preprocessing import MinMaxScaler
import numpy as np


class MapParamValue:
    def __init__(self):
        pass

    def map(self, products):
        category_name = products[0].getCategory().replace(" > ", "_")
        category_mappers = None
        with open('./data/categories/C_{}.json'.format(category_name, mode='r', encoding='utf-8')) as mapping_file:
            category_mappers = json.load(mapping_file)
        distinct_params = list(category_mappers.keys())
        final_features = [{} for _ in products]
        for param in distinct_params:
            for idx, product in enumerate(products):
                if product.hasParam(param):
                    # volanie custom convertoru
                    convertor = get_convertor(
                        category_mappers[param]['convertor'])
                    final_features[idx][param] = convertor.convert(
                        product.getParam(param), category_mappers[param]['params'])
                else:
                    final_features[idx][param] = 0
        for param in distinct_params:
            vals = np.array([x[param] for x in final_features])
            normalized_vals = MinMaxScaler().fit_transform(vals)
            for i in range(len(normalized_vals)):
                final_features[i][param] = normalized_vals[i]

        return final_features
