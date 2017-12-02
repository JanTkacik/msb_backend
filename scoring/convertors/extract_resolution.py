from .base_convertor import BaseConvertor


class ExtractResolution(BaseConvertor):

    @staticmethod
    def convert(parameter_value, convertor_params, category_name=None):
        vals = [float(x.strip()) for x in parameter_value.split("x")]
        return vals[0] * vals[1]
