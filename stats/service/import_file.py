import csv
import pdb

from stats.constants.cell_type import CellType
from stats.repositories.cell import CellRepository
from stats.service.position import PositionService


class RawData:
    def __init__(
            self,
            x,
            y,
            z,
            time,
            cell_type,
            cell_id,
    ):
        self.x = x
        self.y = y
        self.z = z
        self.time = time
        self.cell_type = cell_type
        self.cell_id = cell_id


class ImportFile:
    filepath = 'stats/files/data.csv'

    @classmethod
    def read_file(cls):
        file = open(cls.filepath, mode='r')
        lines = csv.reader(file, delimiter=';')
        return cls.convert_lines(lines)

    @classmethod
    def convert_lines(cls, lines):
        return list(
            map(
                lambda line: cls.extract_data(line),
                lines
            )
        )

    @staticmethod
    def extract_data(line):
        x = line[0]
        y = line[1]
        z = line[2]
        time = line[3]
        cell_type = line[4]
        cell_id = line[5]
        return RawData(
            x=x,
            y=y,
            z=z,
            time=time,
            cell_type=cell_type,
            cell_id=cell_id,
        )

    @staticmethod
    def get_or_create_cell(data: RawData):
        cell, created = CellRepository.get_or_create_by_id(data.cell_id)
        if created:
            cell.type = CellType.MICROGLIA if data.cell_type == 'Microglia' else CellType.MENINGE
            cell.current_time = 0
            cell.current_position = PositionService.create_empty_position()
            cell.save()
        return cell
