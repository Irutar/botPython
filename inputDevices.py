"""Mouse and keyboard functions"""

import pyautogui
import random
import config
import screen


def move_to(image_coordinates):
    change_in_movement_x = random.randint(0, 3)
    change_in_movement_y = random.randint(0, 3)
    pyautogui.moveTo(image_coordinates[0] + change_in_movement_x, image_coordinates[1] + change_in_movement_y,
                     config.DELAY_IN_MOVEMENT, pyautogui.easeInOutQuad)


def left_click():
    pyautogui.click(button='left')


def click_image(image):
    image_coordinates = screen.locate_image_on_full_screen(image)
    move_to(image_coordinates)
    left_click()


def reset_position():
    pyautogui.moveTo(1, 1, 3)


def key_press(key):
    pyautogui.press(key)
