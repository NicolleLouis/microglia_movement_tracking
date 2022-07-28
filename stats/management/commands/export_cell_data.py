from django.core.management.base import BaseCommand

from stats.service.export_cell_data import ExportCellDataService


class Command(BaseCommand):
    def handle(self, *args, **options):
        ExportCellDataService().export()
