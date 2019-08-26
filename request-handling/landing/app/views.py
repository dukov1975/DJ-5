from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    landing_param = request.GET.get('from-landing')
    counter_click[landing_param] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    ab_test_arg = request.GET.get('ab-test-arg')
    counter_show[ab_test_arg] += 1

    return_landing = 'landing.html'

    if ab_test_arg == 'test':
        return_landing = 'landing_alternate.html'
    return render_to_response(return_landing)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:

    if counter_show['test'] > 0:
        test_conversion = counter_click['test'] / counter_show['test']
    else:
        test_conversion = counter_click['test']

    if counter_show['original'] > 0:
        original_conversion = counter_click['original'] / counter_show['original']
    else:
        original_conversion = counter_click['original']

    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
