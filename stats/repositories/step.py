from stats.models import Cell


class CellRepository:
    @staticmethod
    def get_or_create_by_id(cell_id: int):
        cell, created = Cell.objects.get_or_create(
            id=cell_id
        )
        return cell, created
