import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)

            for cell in phone_reader:
                Phone.objects.create(
                        id=cell[0],
                        name=cell[1],
                        image=cell[2],
                        price=cell[3],
                        release_date=cell[4],
                        lte_exists=cell[5],
                        slug=slugify(cell[1])
                )
