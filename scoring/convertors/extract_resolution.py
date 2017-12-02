from .base_convertor import BaseConvertor


class ExtractResolution(BaseConvertor):

    @staticmethod
    def convert(parameter_value, convertor_params, category_name=None):
        pos_x = parameter_value.index('x')
        return float(parameter_value[:pos_x].strip())
