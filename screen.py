"""Here are functions that are connected with the screen i.e:

        Functions that take screen shoots of the screen or its part and save it to the .png file
        Functions that locate images of the screen
"""

import mss
import mss.tools
import pyautogui
import config


def full_screen_screen_shoot():
    mss.mss().shot(output='images/fullscreen.png')


def part_screen_screen_shoot(icon_coordinates, output):
    r = icon_coordinates[0]
    r1 = icon_coordinates[1]
    r2 = icon_coordinates[2]
    r3 = icon_coordinates[3]

    monitor = {'top': r1, 'left': r, 'width': r2, 'height': r3}

    # Grab the data
    sct_img = mss.mss().grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)


def locate_image_on_full_screen(image):
    full_screen_screen_shoot()
    image_coordinates = pyautogui.locate(image, 'images/fullscreen.png', grayscale=config.GRAY_VALUE)
    return image_coordinates


def locate_image_on_part_screen(resource_image, screen_image, icon_coordinates):
    resource_icon_coordinates = pyautogui.locate(resource_image, screen_image, grayscale=config.GRAY_VALUE)
    if resource_icon_coordinates is not None:
        resource_icon_coordinates = list(resource_icon_coordinates)
        resource_icon_coordinates[0] = resource_icon_coordinates[0] + icon_coordinates[0]
        resource_icon_coordinates[1] = resource_icon_coordinates[1] + icon_coordinates[1]
        resource_icon_coordinates[2] = resource_icon_coordinates[2] + icon_coordinates[2]
        resource_icon_coordinates[3] = resource_icon_coordinates[3] + icon_coordinates[3]
        resource_icon_coordinates = tuple(resource_icon_coordinates)
    return resource_icon_coordinates
