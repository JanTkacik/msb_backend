from .base_convertor import BaseConvertor


class ConvertBool(BaseConvertor):
    @staticmethod
    def convert(parameter_value, convertor_params, category_name=None):
        return float(parameter_value == 'ano')
