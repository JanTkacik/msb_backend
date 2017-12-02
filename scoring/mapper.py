from .convertors import get_convertor
from .modifiers import get_modifier
import json
from sklearn.preprocessing import MinMaxScaler
import numpy as np


class MapParamValue:
    MAX_WEIGHT = 100
    MIN_WEIGHT = 0.01
    categories_params_modifiers = None

    def __init__(self):
        pass

    def weight_approximation(self, order):
        final_weight = (1 / pow(order, 3))* 100

        if final_weight > MapParamValue.MAX_WEIGHT:
            final_weight = MapParamValue.MAX_WEIGHT
        elif final_weight < MapParamValue.MIN_WEIGHT:
            final_weight = MapParamValue.MIN_WEIGHT

        return final_weight


    def _load_categories_params_modifiers(self):
        with open('./data/categories/collected_params.json', mode='r', encoding='utf-8') as file_json:
            MapParamValue.categories_params_modifiers = json.load(file_json)

    def map(self, products):
        if MapParamValue.categories_params_modifiers is None:
            self._load_categories_params_modifiers()

        category_name = products[0].getCategory().replace(" > ", "_")
        category_mappers = None
        with open('./data/categories/C_{}.json'.format(category_name), mode='r', encoding='utf-8') as mapping_file:
            category_mappers = json.load(mapping_file)
        distinct_params = list(category_mappers.keys())
        final_features = [{} for _ in products]
        for param in distinct_params:
            # volanie custom convertoru
            convertor = get_convertor(category_mappers[param]['convertor'])
            modifier = get_modifier(MapParamValue.categories_params_modifiers[products[0].getCategory()][param])
            for idx, product in enumerate(products):
                if product.hasParam(param):
                    final_features[idx][param] = convertor.convert(
                        product.getParam(param), category_mappers[param]['params'], category_name)
                else:
                    final_features[idx][param] = 0
                
                final_features[idx][param] = modifier.modify(final_features[idx][param]) * self.weight_approximation(category_mappers[params]['order'])

        for param in distinct_params:
            vals = np.array([x[param] for x in final_features])
            vals = vals.reshape(-1, 1)
            normalized_vals = MinMaxScaler().fit_transform(vals)
            normalized_vals = normalized_vals.reshape(-1)
            for i in range(len(normalized_vals)):
                final_features[i][param] = normalized_vals[i]

        return final_features
