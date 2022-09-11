import random
import arcade


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture(":resources:images/tiles/bomb.png")
        self.center_x = random.randint(0, 1000)
        self.center_y = 400
        self.speed = 4
