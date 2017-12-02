class ConvertBool(BaseConvertor):

    @staticmethod
    def convert(parameter_value, convertor_params):
        if 'offset' in convertor_params:
            return float(parameter_value[:-convertor_params['offset'].strip()])
        return int(parameter_value)
