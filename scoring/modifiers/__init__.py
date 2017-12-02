from .base_modifier import BaseModifier
from .bigger_better import BiggerBetter
from .having_better import HavingBetter
from .smaller_better import SmallerBetter
from .user_preferences import UserPreferences

available_modifiers = {
    'BaseModifier': BaseModifier,
    'BB': BiggerBetter,
    'HB': HavingBetter,
    'SB': SmallerBetter,
    'UP': UserPreferences,
}


def get_modifier(modifier_name):
    if modifier_name in available_modifiers:
        return available_modifiers[modifier_name]
    else:
        return BaseModifier
