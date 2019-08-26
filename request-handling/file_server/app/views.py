from datetime import datetime

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

import os


def file_list(request, date=None):
    template_name = 'index.html'
    files = []

    try:
        filter_date = datetime.strptime(date, '%Y-%m-%d').date()
    except TypeError:
        pass

    for file in os.listdir(settings.FILES_PATH):

        file_path = os.path.join(settings.FILES_PATH, file)
        create_time = datetime.fromtimestamp(os.stat(file_path).st_ctime)
        change_time = datetime.fromtimestamp(os.stat(file_path).st_mtime)

        if date and filter_date != create_time.date():
            continue

        file_info = {
            'name': file,
            'ctime': create_time,
            'mtime': change_time
        }
        files.append(file_info)
    return render(request, template_name, context={'files': files, 'date': filter_date if date else ''})


def file_content(request, name):
    if name in os.listdir(settings.FILES_PATH):
        file_name = os.path.join(settings.FILES_PATH, name)
        with open(file_name) as f:
            content = f.read()
    else:
        return HttpResponse(f'Файл {name} не найден!')

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )
