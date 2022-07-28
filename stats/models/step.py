from django.db import models
from django.contrib import admin


class Step(models.Model):
    id = models.AutoField(primary_key=True)
    position = models.ForeignKey(
        'Position',
        on_delete=models.PROTECT,
        null=True,
    )
    time = models.IntegerField(
        null=False
    )
    cell = models.ForeignKey(
        'Cell',
        on_delete=models.PROTECT,
        null=False,
    )

    def __str__(self):
        return f'{self.cell.id}: {self.position} at {self.time}'


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = (
        'cell',
        'time',
        'position',
    )
