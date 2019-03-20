# 以下是模組(module) ( report.py )
def get_description(): #see the docstring below?
    """Return random weather, just like the pros"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
