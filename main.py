import pyglet
from pyglet.window import key

from game import player, constants, load


game_window = pyglet.window.Window(
    constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH)
main_batch = pyglet.graphics.Batch()

terrain_group = pyglet.graphics.OrderedGroup(0)
objects_group = pyglet.graphics.OrderedGroup(1)

player_sprite = player.Player(batch=main_batch, group=objects_group)
tiles = load.terrain(100, 100, batch=main_batch, group=terrain_group)

game_objects = [player_sprite]


# Register event handlers
for obj in game_objects:
    for handler in obj.event_handlers:
        game_window.push_handlers(handler)

for tile in tiles:
    for handler in tile.event_handlers:
        game_window.push_handlers(handler)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    # Update all objects
    for obj in game_objects:
        obj.update(dt)

    for tile in tiles:
        tile.update(dt, player_sprite)


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120.0)

    pyglet.app.run()
