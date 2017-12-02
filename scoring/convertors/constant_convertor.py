from .base_convertor import BaseConvertor


class ConstantConvertor(BaseConvertor):
    @staticmethod
    def convert(parameter_value, convertor_params, category_name=None):
        return 0.0
