from stats.models import Step


class StepRepository:
    @staticmethod
    def get_or_create_by_cell_and_time(cell, time: int):
        step, created = Step.objects.get_or_create(
            cell=cell,
            time=time
        )
        return step, created

    @staticmethod
    def get_by_cell(cell):
        return Step.objects.filter(cell=cell)
