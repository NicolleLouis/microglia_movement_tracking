import matplotlib.pyplot as plt

from stats.constants.cell_type import CellType
from stats.repositories.cell import CellRepository
from stats.repositories.step import StepRepository


class TrajectoryGraphService:
    @classmethod
    def call(cls):
        cells = cls.get_all_cells()
        for cell in cells:
            cls.plot_trajectory_cell(cell)

        cls.add_options()
        cls.show()

    @staticmethod
    def add_options():
        plt.axis([-70, 125, -70, 125])
        plt.xlabel('x')
        plt.ylabel('y')

        plt.title('Trajectories')

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def get_all_cells():
        return CellRepository.get_all_valid_cell()

    @staticmethod
    def generate_trajectory_cell(cell):
        unordered_steps = StepRepository.get_by_cell(cell)
        steps = sorted(
            unordered_steps,
            key=lambda step: step.time
        )
        x = list(
            map(
                lambda step: step.position.x,
                steps
            )
        )
        y = list(
            map(
                lambda step: step.position.y,
                steps
            )
        )
        return x, y

    @classmethod
    def plot_trajectory_cell(cls, cell):
        x, y = cls.generate_trajectory_cell(cell)
        plt.plot(x, y)
