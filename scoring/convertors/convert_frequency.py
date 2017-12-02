from .base_convertor import BaseConvertor


class ConvertFrequency(BaseConvertor):

    @staticmethod
    def convert(parameter_value, convertor_params):
        notvalidfreq = float(parameter_value[:-3].strip())
        if notvalidfreq < 10.0:
            notvalidfreq = notvalidfreq * 1000
        return notvalidfreq