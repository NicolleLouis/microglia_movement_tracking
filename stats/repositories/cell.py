from stats.models import Cell


class CellRepository:
    @staticmethod
    def get_or_create_by_id(cell_id: int):
        cell, created = Cell.objects.get_or_create(
            id=cell_id
        )
        return cell, created

    @staticmethod
    def get_all():
        return Cell.objects.all()

    @staticmethod
    def get_all_valid_cell():
        minimum_steps = 60
        return Cell.objects.filter(current_time__gte=minimum_steps)
