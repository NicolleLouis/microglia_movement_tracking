from django.core.management.base import BaseCommand

from stats.models import Cell
from stats.service.cell import CellService


class Command(BaseCommand):
    def handle(self, *args, **options):
        cells = Cell.objects.all()
        for cell in cells:
            CellService.compute_final_position(cell)
