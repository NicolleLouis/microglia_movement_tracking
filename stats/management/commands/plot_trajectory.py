from django.core.management.base import BaseCommand

from stats.service.trajectory_graph import TrajectoryGraphService


class Command(BaseCommand):
    def handle(self, *args, **options):
        TrajectoryGraphService().call()
