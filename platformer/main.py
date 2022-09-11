import time
import arcade
from player import Player
from ground import Ground
from enemy import Enemy



class Game(arcade.Window):
    def __init__(self):
        self.w = 1000
        self.h = 500
        self.gravity = 0.4
        super().__init__(self.w , self.h ,"platformer game")
        self.background_image = arcade.load_texture("background.png")

        self.t1 = time.time()

        self.me = Player()
        self.ground_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        

        for i in range(0,1000,120):
            ground = Ground(i , 40)
            self.ground_list.append(ground)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.me, self.ground_list, gravity_constant = self.gravity)
        



    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0 ,0 , self.w , self.h , self.background_image)

        self.me.draw()
        for ground in self.ground_list:
            ground.draw()



    def on_update(self, delta_time: float):
        self.physics_engine.update()
        
        self.t2 = time.time()
        if self.t2 - self.t1 > 5:
            self.enemy_list.append(Enemy())

    def on_key_press(self, symbol, modifiers):
        match symbol:
            case arcade.key.LEFT:
                self.me.change_x = -1 * self.me.speed
            case arcade.key.RIGHT:
                self.me.change_x = +1 *self.me.speed
            case arcade.key.UP:
                if self.physics_engine.can_jump():
                    self.me.change_y = 10


    def on_key_release(self, symbol, modifiers):
        self.me.change_x = 0


game = Game()
arcade.run()
