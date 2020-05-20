import pyglet
from pyglet.window import key

from game import player


game_window = pyglet.window.Window()
main_batch = pyglet.graphics.Batch()

player_sprite = player.Player(batch=main_batch)


game_objects = [player_sprite]


# Register event handlers
for obj in game_objects:
    for handler in obj.event_handlers:
        game_window.push_handlers(handler)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    # Update all objects
    for obj in game_objects:
        obj.update(dt)


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120.0)

    pyglet.app.run()
