from django.core.management.base import BaseCommand

from stats.models import Position
from stats.service.import_file import ImportFile


class Command(BaseCommand):
    def handle(self, *args, **options):
        positions = Position.objects.all().delete()

