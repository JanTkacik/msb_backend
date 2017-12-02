class BaseConvertor:
    @staticmethod
    def convert(parameter_value, convertor_params, category_name=None):
        return parameter_value

    @staticmethod
    def get_reason(final_value, pc):
        return pc.format(value=final_value)
