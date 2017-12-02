from .base_convertor import BaseConvertor


class ExtractText(BaseConvertor):

    @staticmethod
    def convert(parameter_value, convertor_params):
        if 'offset' in convertor_params:
            offset = convertor_params['offset']
            if offset == 0:
                return float(parameter_value)
            return float(parameter_value[:-offset].strip())
        return float(parameter_value)
