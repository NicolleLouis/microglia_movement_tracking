import csv

from stats.repositories.cell import CellRepository


class ExportCellDataService:
    filepath = 'stats/files/export/cell.csv'

    def __init__(self):
        self.file = None
        self.writer = None

    def export(self):
        self.read_file()
        self.generate_writer()
        self.generate_header()
        self.generate_lines()
        self.close_file()

    def read_file(self):
        self.file = open(self.filepath, mode='w')

    def close_file(self):
        self.file.close()

    def generate_writer(self):
        self.writer = csv.writer(self.file, delimiter=";")

    def generate_header(self):
        self.writer.writerow(["type", "x", "y", "z"])

    def generate_lines(self):
        cells = CellRepository.get_all_valid_cell()
        for cell in cells:
            self.generate_line(cell)

    def generate_line(self, cell):
        self.writer.writerow(
            [
                cell.type,
                cell.current_position.x,
                cell.current_position.y,
                cell.current_position.z,
            ]
        )
