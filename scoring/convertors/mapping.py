import json


class Mapping(BaseConvertor):
    categories = {}

    @staticmethod
    def _load_mapping(category_name):
        with open('./available_mappings/{}.json'.format(category_name, mode='r', encoding='utf-8') as mapping_file:
            Mapping.categories[category_name] = json.load(mapping_file)

    @staticmethod
    def convert(parameter_value, convertor_params):
        if convertor_params['mapping'] not in Mapping.categories:
            Mapping._load_mapping(convertor_params['mapping'])

        return float(Mapping.categories[convertor_params['mapping']][convertor_params['parameter_name']][parameter_value].strip()])
