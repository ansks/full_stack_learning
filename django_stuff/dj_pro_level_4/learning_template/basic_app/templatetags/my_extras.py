from  django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This replace all the values of "arg" from the string!
    """

    # return value.replace(arg, '')
    return value + ', ' + arg

# register.filter('cut', cut) Another way of register a function is using decorators.
