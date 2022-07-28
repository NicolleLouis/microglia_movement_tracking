from django.core.management.base import BaseCommand

from stats.service.import_file import ImportFile


class Command(BaseCommand):
    def handle(self, *args, **options):
        lines = ImportFile.read_file()
        for line in lines:
            cell = ImportFile.get_or_create_cell(line)
            step = ImportFile.get_or_create_step(line, cell)
            print(step)
