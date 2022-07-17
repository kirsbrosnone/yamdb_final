from core.csv_reader import main
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Команда создающая dummy data'

    def handle(self, *args, **kwargs):
        main()
