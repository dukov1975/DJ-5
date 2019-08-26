from datetime import datetime
from django import template

register = template.Library()


@register.filter
def format_date(value):
    date = datetime.fromtimestamp(value)
    current_date = datetime.now()
    delta = (current_date - date).seconds // 60

    if delta <= 10:
        value = 'Только что'
    elif 10 < delta <= 1440:
        value = f'{delta // 60} часов назад'
    else:
        value = date

    return value


@register.filter
def format_score(value):
    if value:
        score = int(value)

        if score < -5:
            value = 'все плохо'
        elif -5 <= score <= 5:
            value = 'нейтрально'
        else:
            value = 'хорошо'

    return value


@register.filter
def format_num_comments(value):
    comments = int(value)

    if comments == 0:
        value = 'Оставьте комментарий'
    elif comments > 50:
        value = '50+'

    return value


@register.filter
def format_selftext(value, arg):
    if value:
        words = value.split()
        if len(words) > int(arg):
            filter = int(arg)
            value = f'{" ".join(words[:filter])} ... {" ".join(words[-filter:])}'

    return value
