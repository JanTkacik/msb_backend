import json
from .base_convertor import BaseConvertor


class Mapping(BaseConvertor):
    categories = {}

    @staticmethod
    def _load_mapping(category_name):
        with open('./data/categories/AV_{}.json'.format(category_name, mode='r', encoding='utf-8')) as mapping_file:
            Mapping.categories[category_name] = json.load(mapping_file)

    @staticmethod
    def convert(parameter_value, convertor_params):
        cn = convertor_params['category_name']
        if cn not in Mapping.categories:
            Mapping._load_mapping(cn)
        return float(Mapping.categories[cn][convertor_params['parameter_name']][parameter_value])
