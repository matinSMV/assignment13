import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")

        self.center_x = 100
        self.center_y = 400
        self.speed = 4


