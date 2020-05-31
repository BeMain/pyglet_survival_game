import pyglet
from pyglet import gl

from game import constants


pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

# We don't want images to be blurry when scaled
gl.glEnable(gl.GL_TEXTURE_2D)
gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)


def center_image(image):
    # Sets an image's anchor point to its center
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def get_background_scale_factor(background):
    # Used to scale background to fill screen
    scale_x = constants.SCREEN_WIDTH / background.width
    scale_y = constants.SCREEN_HEIGHT / background.height

    return max(scale_x, scale_y)


player_image = pyglet.resource.image("player.png", rotate=-90)
player_image.width /= 10
player_image.height /= 10
center_image(player_image)

tile_image = pyglet.resource.image("tiles/stone.png")
tile_image.width = tile_image.height = constants.TILE_SIZE
center_image(tile_image)


background_image = pyglet.resource.image("backgrounds/space.png")
scale_factor = get_background_scale_factor(background_image)
background_image.width *= scale_factor
background_image.height *= scale_factor
background_image.anchor_x = 0
background_image.anchor_y = 0
