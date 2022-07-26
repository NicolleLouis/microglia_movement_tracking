from django.db import models
from django.contrib import admin

from stats.constants.cell_type import CellType


class Cell(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(
        max_length=25,
        choices=CellType.choices,
        default=None,
        null=True
    )
    current_position = models.ForeignKey(
        'Position',
        on_delete=models.CASCADE,
        null=True,
    )
    current_time = models.IntegerField(
        default=0,
        null=False
    )

    def __str__(self):
        return f'{self.type}: {self.current_position} at {self.current_time}'


@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    list_display = (
        'current_time',
        'current_position',
    )

    list_filter = (
        'type',
    )
