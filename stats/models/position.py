from django.db import models
from django.contrib import admin


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'x',
        'y',
        'z',
    )
