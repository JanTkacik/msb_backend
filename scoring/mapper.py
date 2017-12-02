from .convertors import get_convertor

class MapParamValue:
    
    def __init__(self, category_name):
        pass

    def _get_distinct_params(self, products):
        return ['Procesor']

    def map(self, products):
        distinct_params = self._get_distinct_params(products)
        final_features = [{} for _ in products]
        for param in distinct_params:
            min_value = 0
            max_value = 1000
            for idx, product in enumerate(products):
                if param in product['PARAMS']:
                    final_features[idx][param] = 0.5
                    # volanie custom convertoru
                    convertor = get_convertor('convertor_name')
                    final_features[idx][param] = convertor.convert(final_features[idx][param])                    
                else:
                    final_features[idx][param] = 0
            
            # normalize values
        return final_features
