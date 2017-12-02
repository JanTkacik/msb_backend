from .base_modifier import BaseModifier


class SmallerBetter(BaseModifier):

    @staticmethod
    def modify(parameter_value):
        return -parameter_value
