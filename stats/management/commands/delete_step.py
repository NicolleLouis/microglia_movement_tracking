from django.core.management.base import BaseCommand

from stats.models import Step


class Command(BaseCommand):
    def handle(self, *args, **options):
        Step.objects.all().delete()
