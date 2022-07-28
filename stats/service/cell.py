from stats.models import Cell
from stats.repositories.step import StepRepository


class CellService:
    @staticmethod
    def compute_final_position(cell: Cell):
        steps = StepRepository.get_by_cell(cell)
        final_step = max(
            steps,
            key=lambda step: step.time
        )
        cell.current_time = final_step.time
        cell.current_position = final_step.position
        cell.save()
