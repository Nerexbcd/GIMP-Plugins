#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from gimpfu import *

def ctt_label_extractor_blue_international(image, layer):
    
    crop_x, crop_y = 1080, 0
    crop_w, crop_h = 1400, 1748

    canvas_width, canvas_height = 1200, 1800 

    

    # Duplicate the image to work on a copy
    new_image = pdb.gimp_image_duplicate(image)
    new_layer = new_image.active_layer

    pdb.gimp_image_crop(new_image, crop_w, crop_h, crop_x, crop_y)

    
    final_image = pdb.gimp_image_new(canvas_width, canvas_height, RGB)
    bg_layer = pdb.gimp_layer_new(final_image, canvas_width, canvas_height, RGB_IMAGE, "Background", 100, NORMAL_MODE)
    pdb.gimp_image_add_layer(final_image, bg_layer, 0)
    pdb.gimp_context_set_foreground((255, 255, 255))  # Set white background
    pdb.gimp_edit_fill(bg_layer, FOREGROUND_FILL)

    # Scale cropped image to fit inside 6x4 inches
    img_w, img_h = new_layer.width, new_layer.height
    scale_ratio = min(float(canvas_width) / img_w, float(canvas_height) / img_h)
    new_w = int(img_w * scale_ratio)
    new_h = int(img_h * scale_ratio)
    pdb.gimp_layer_scale(new_layer, new_w, new_h, True)

    # Center the cropped image on the new canvas
    x_offset = (canvas_width - new_w) // 2
    y_offset = (canvas_height - new_h) // 2
    layer_copy = pdb.gimp_layer_new_from_drawable(new_layer, final_image)
    pdb.gimp_image_insert_layer(final_image, layer_copy, None, 0)
    pdb.gimp_layer_set_offsets(layer_copy, x_offset, y_offset)

    #flaten image
    pdb.gimp_image_merge_visible_layers(final_image, 0)

    # Display the new image in a new tab
    gimp.Display(final_image)
    gimp.displays_flush()

    # Clean up
    pdb.gimp_image_delete(new_image)  # Delete the duplicated cropped image


register(
    "CTT_Label_Extractor_Blue_International",
    "Automatically Converts the PDF Received for Shipping in to a 4x6 Standard Shipping Label",
    "",
    "Nerexbcd",
    "Nerexbcd",
    "2025",
    "<Image>/Nerexbcd/Label Extraction/CTT Blue International",
    "*",
    [],
    [],
    ctt_label_extractor_blue_international
)

main()
