from stats.models import Position


class PositionService:
    @staticmethod
    def create_position(x, y, z):
        position = Position(
            x=x,
            y=y,
            z=z
        )
        position.save()
        return position

    @classmethod
    def create_empty_position(cls):
        return cls.create_position(0, 0, 0)

    @staticmethod
    def sum_position(position_a, position_b):
        return Position(
            x=position_a.x + position_b.x,
            y=position_a.y + position_b.y,
            z=position_a.z + position_b.z,
        )
