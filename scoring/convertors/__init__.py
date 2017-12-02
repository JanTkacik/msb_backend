from .base_convertor import BaseConvertor


available_convertors = {
    'BaseConvertor': BaseConvertor,
}

def get_convertor(convertor_name):
    if convertor_name in available_convertors:
        return available_convertors[convertor_name]
    else:
        return BaseConvertor
