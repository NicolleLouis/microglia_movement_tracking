from django.core.management.base import BaseCommand

from stats.models import Position


class Command(BaseCommand):
    def handle(self, *args, **options):
        Position.objects.all().delete()
