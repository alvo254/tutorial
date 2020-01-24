#!/usr/bin/python3
import arcade

screen_width = 600
screen_height = 600

arcade.open_window(screen_width, screen_width, "drawing example")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

# draw the face
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)
# draw the right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
# draw the LEFT EYE
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
# draw the smile
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
radius = 200
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)
arcade.finish_render()
arcade.run()

