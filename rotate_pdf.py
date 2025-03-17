#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from gimpfu import *

def rotate_open_image(image, layer):
    # Ensure we have a valid image and layer
    if not image or not layer:
        gimp.message("Error: No active image or layer found!")
        return

    # Get current dimensions
    old_width, old_height = image.width, image.height

    # Rotate the active layer (not just the whole image metadata)
    pdb.gimp_item_transform_rotate(layer, 90 * (3.14159 / 180), True, old_width / 2, old_height / 2)

    # Resize the canvas to fit the rotated content
    new_width, new_height = old_height, old_width
    pdb.gimp_image_resize(image, new_width, new_height, 0, 0)

    # Move the layer to the center
    pdb.gimp_layer_set_offsets(layer, 0, 0)

    # Ensure the display updates
    gimp.displays_flush()
    gimp.message("Image rotated to landscape mode!")

register(
    "rotate_open_image",
    "Rotate the current image 90 degrees",
    "Rotates the active image by 90 degrees clockwise",
    "Your Name",
    "Your Name",
    "2025",
    "<Image>/Filters/Python-Fu/Rotate 90°",
    "*",
    [],
    [],
    rotate_open_image
)

main()
