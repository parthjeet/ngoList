from django import template
import re
register = template.Library()
unique_benef = []

@register.filter (name='split')
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

@register.filter (name ='target_groups')
def target_groups(value, key):
    global unique_benef
    benef = value.split(key)
    for item in benef:
        item = item.lstrip()
        if item not in unique_benef:
            unique_benef.append(item)
    return unique_benef

@register.filter (name ='ans')
def ans(value):
    res = ''
    unique_benef.sort()
    for item in unique_benef:
        res = res + item + '<br>'
    return res