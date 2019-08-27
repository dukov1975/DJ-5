from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"

    form = CalcForm(request.GET)
    
    context = {
        'form': form
    }

    if form.is_valid():
        common_result = float(form.cleaned_data['initial_fee']) + \
                        float(form.cleaned_data['initial_fee']) * \
                        (float(form.cleaned_data['rate']) / 100)
        result = common_result / float(form.cleaned_data['months_count'])
        context['common_result'] = common_result
        context['result'] = result

    return render(request, template, context)
