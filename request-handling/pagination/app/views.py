from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator

import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page_parameter = '?page='
    current_page = request.GET.get('page')
    if not current_page:
        current_page = 1

    with open(settings.BUS_STATION_CSV, encoding='cp1251', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        reader_list = list(reader)
        paginator = Paginator(reader_list, 10)

    if paginator.page(current_page).has_previous():
        previous_page = paginator.page(current_page).previous_page_number()
    else:
        previous_page = 1

    if paginator.page(current_page).has_next():
        next_page = paginator.page(current_page).next_page_number()
    else:
        next_page = current_page

    return render_to_response('index.html', context={
        'bus_stations': paginator.page(current_page),
        'current_page': current_page,
        'prev_page_url': f'{page_parameter}{previous_page}',
        'next_page_url': f'{page_parameter}{next_page}',
    })
