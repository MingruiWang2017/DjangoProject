# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2019/9/29 14:59
"""

from django import template

register = template.Library()


@register.filter
def field_type(bound_field):
    """返回字段类型"""
    return bound_field.field.widget.__class__.__name__


@register.filter
def input_class(bound_field):
    """返回输入字段的类型"""
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)
