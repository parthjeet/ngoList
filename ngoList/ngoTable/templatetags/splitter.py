from django import template
import re
register = template.Library()

@register.filter
def split(value, key):
    dict= {}
    regex = '[\s]*http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[#$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    texts = re.sub(regex, '~` ', value)
    texts = texts.split('~`')
    links = re.findall(regex, value)
    i = 0
    for text in texts:
        dict[text] = 'no'
        if i < len(links):
            dict[links[i]] = 'yes'
            i = i + 1
    return dict.items()