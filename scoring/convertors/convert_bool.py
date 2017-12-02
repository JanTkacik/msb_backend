class ConvertBool(BaseConvertor):

    @staticmethod
    def convert(parameter_value, convertor_params):
        return int(parameter_value == 'ano')
