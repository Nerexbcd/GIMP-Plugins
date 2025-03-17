#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from gimpfu import *

# Customization Configuration
edit_on_new_tab = False

# Specific Label Configuration
# Amazon Return Label
crop_x, crop_y = 1623, 349
crop_w, crop_h = 1048, 1620

# Cover Areas
areas = [
    (0, 0, image.width, 10),  # Top border
]

# Static Label Configuration
canvas_width, canvas_height = 1200, 1800 # 4x6 inches Label


def amazon_return_label_extractor(image, layer):



    old_w, old_h = image.width, image.height

    # Rotate the active layer (not just the whole image metadata)
    pdb.gimp_item_transform_rotate(layer, 90 * (3.14159 / 180), True, old_w / 2, old_h / 2)

    new_w, new_h = old_h, old_w
    pdb.gimp_image_resize(image, new_w, new_h, 0, 0)

    # Move the layer to the center
    pdb.gimp_layer_set_offsets(layer, 0, 0)

    
    gimp.displays_flush()

    

    

    # Duplicate the image to work on a copy


    

    # new_image = pdb.gimp_image_duplicate(image)
    # new_layer = new_image.active_layer
    # pdb.gimp_image_crop(new_image, crop_w, crop_h, crop_x, crop_y)
    # final_image = pdb.gimp_image_new(canvas_width, canvas_height, RGB)
    # bg_layer = pdb.gimp_layer_new(final_image, canvas_width, canvas_height, RGB_IMAGE, "Background", 100, NORMAL_MODE)
    # pdb.gimp_image_add_layer(final_image, bg_layer, 0)
    # pdb.gimp_context_set_foreground((255, 255, 255))  # Set white background
    # pdb.gimp_edit_fill(bg_layer, FOREGROUND_FILL)

    # # Scale cropped image to fit inside 6x4 inches
    # img_w, img_h = new_layer.width, new_layer.height
    # scale_ratio = min(float(canvas_width) / img_w, float(canvas_height) / img_h)
    # new_w = int(img_w * scale_ratio)
    # new_h = int(img_h * scale_ratio)
    # pdb.gimp_layer_scale(new_layer, new_w, new_h, True)

    # new_image = pdb.gimp_image_duplicate(image)
    # pdb.gimp_image_crop(new_image, crop_w, crop_h, crop_x, crop_y)

    pdb.gimp_image_crop(image, crop_w, crop_h, crop_x, crop_y)
    pdb.gimp_image_resize(image, canvas_width, canvas_height, 0, 0)
    



    # Scale cropped image to fit inside 6x4 inches
    img_w, img_h = layer.width, layer.height
    scale_ratio = min(float(canvas_width) / img_w, float(canvas_height) / img_h)
    new_w = int(img_w * scale_ratio)
    new_h = int(img_h * scale_ratio)
    pdb.gimp_layer_scale(layer, new_w, new_h, True)

    # # Center the cropped image on the new canvas
    x_offset = (canvas_width - new_w) // 2
    y_offset = (canvas_height - new_h) // 2
    # layer_copy = pdb.gimp_layer_new_from_drawable(new_layer, final_image)
    # pdb.gimp_image_insert_layer(final_image, layer_copy, None, 0)
    pdb.gimp_layer_set_offsets(layer, x_offset, y_offset)

    #flaten image
    # pdb.gimp_image_merge_visible_layers(final_image, 0)

    # # Display the new image in a new tab
    # gimp.Display(final_image)
    gimp.displays_flush()

    # Clean up
    # pdb.gimp_image_delete(new_image)  # Delete the duplicated cropped image


register(
    "Amazon_Return_Label_Extractor",
    "Automatically Converts the PDF Received for Shipping in to a 4x6 Standard Shipping Label",
    "",
    "Nerexbcd",
    "Nerexbcd",
    "2025",
    "<Image>/Nerexbcd/Label Extraction/Amazon Return Label",
    "*",
    [],
    [],
    amazon_return_label_extractor
)

main()
