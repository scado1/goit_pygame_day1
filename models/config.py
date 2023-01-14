from pydantic import BaseModel


class GameConfig(BaseModel):
    screen: tuple = (1200, 1000)
    ball_size: tuple = (20, 20)
    velocity: list = [1, 1]


config = GameConfig()
