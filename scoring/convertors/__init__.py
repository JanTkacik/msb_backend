from .base_convertor import BaseConvertor
from .convert_bool import ConvertBool
from .extract_text import ExtractText
from .extract_resolution import ExtractResolution


available_convertors = {
    'BaseConvertor': BaseConvertor,
    'ExtractText': ExtractText,
    'ConvertBool': ConvertBool,
    'ExtractResolution': ExtractResolution,
}


def get_convertor(convertor_name):
    if convertor_name in available_convertors:
        return available_convertors[convertor_name]
    else:
        return BaseConvertor
