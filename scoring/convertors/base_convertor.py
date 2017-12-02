class BaseConvertor:
    @staticmethod
    def convert(parameter_value, convertor_params, category_name=None):
        return parameter_value

    @staticmethod
    def get_reason(value, pc):
        return pc + " " + str(value)
