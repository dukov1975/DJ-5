import csv
from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv', encoding='utf-8', newline='') as file_csv:
        data = csv.reader(file_csv, delimiter=';')
        header = next(data)
        inflation_stats = []
        for row in data:
            data_row = []
            year = {'data': row.pop(0), 'style': ''}
            data_row.append(year)
            for cell in row:
                cell_dict = {}
                if not cell:
                    cell_dict['data'] = '-'
                    cell_dict['style'] = ''
                    data_row.append(cell_dict)
                    continue
                cell_dict['data'] = cell
                if float(cell) <= 0:
                    cell_dict['style'] = 'negative-inflation'
                elif 0 < float(cell) < 1:
                    cell_dict['style'] = ''
                elif 1 <= float(cell) < 2:
                    cell_dict['style'] = 'positive-normal'
                elif 2 <= float(cell) < 5:
                    cell_dict['style'] = 'positive-bad'
                else:
                    cell_dict['style'] = 'positive-very-bad'
                    data_row.append(cell_dict)
            inflation_stats.append(data_row)
    context = {
        'header': header,
        'inflation_stats': inflation_stats
    }
    return render(request, template_name, context)
