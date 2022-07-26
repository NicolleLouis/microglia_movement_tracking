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
