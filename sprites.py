#!/usr/bin/python3
import arcade

screen_width = 600
screen_height = 600

arcade.open_window(screen_width, screen_width, "drawing example")
arcade.set_background_color(arcade.color.WHITE)
sprite_scaling_017 = 0.2
im = arcade.Sprite("017.png", sprite_scaling_017)
arcade.start_render()
arcade.finish_render()
arcade.run()


