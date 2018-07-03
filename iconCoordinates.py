"""Function to collect and save coordinets of images located on the screen. It is necessary to increase the speed
execution of the program, thanks giving the program approximate coordinates of looking images"""


import images
import config
import screen
import multiprocessing as mp
import time


def locate_af_icons():
    AImage()
    BImage()
    ResourceImage()


def dispatcher_for_a_coordinates(n):
    if n == 0:
        return screen.locate_image_on_full_screen(images.A_LIGHT)
    if n == 1:
        return screen.locate_image_on_full_screen(images.A_DARK)


def AImage():
    if config.GET_EXECUTION_TIME_INFO is True:
        start = time.time()
    screen.full_screen_screen_shoot()
    pool = mp.Pool(processes=2)
    v = pool.map(dispatcher_for_a_coordinates, range(2))
    pool.close()
    pool.join()
    a_light_coordinates = v[0]
    a_dark_coordinates = v[1]

    checkNumber1 = check_if_none(a_light_coordinates)
    checkNumber2 = check_if_none(a_dark_coordinates)

    a_minimum = min(checkNumber1, checkNumber2)

    if a_minimum == checkNumber1:
        config.a_icon_coordinates = image_coordinates_with_safe_buffer(a_light_coordinates)
    elif a_minimum == checkNumber2:
        config.a_icon_coordinates = image_coordinates_with_safe_buffer(a_dark_coordinates)

    if config.GET_EXECUTION_TIME_INFO is True:
        end = time.time()
        print('getting icon coordinates in: {} '.format(end - start))


def dispatcher_for_b_coordinates(n):
    if n == 0:
        return screen.locate_image_on_full_screen(images.B_LIGHT)
    if n == 1:
        return screen.locate_image_on_full_screen(images.B_DARK)


def BImage():
    if config.GET_EXECUTION_TIME_INFO is True:
        start = time.time()
    screen.full_screen_screen_shoot()
    pool = mp.Pool(processes=2)
    v = pool.map(dispatcher_for_b_coordinates, range(2))
    pool.close()
    pool.join()
    b_light_coordinates = v[0]
    b_dark_coordinates = v[1]

    checkNumber1 = check_if_none(b_light_coordinates)
    checkNumber2 = check_if_none(b_dark_coordinates)

    b_minimum = min(checkNumber1, checkNumber2)

    if b_minimum == checkNumber1:
        config.b_icon_coordinates = image_coordinates_with_safe_buffer(b_light_coordinates)
    elif b_minimum == checkNumber2:
        config.b_icon_coordinates = image_coordinates_with_safe_buffer(b_dark_coordinates)

    if config.GET_EXECUTION_TIME_INFO is True:
        end = time.time()
        print('getting icon coordinates in: {} '.format(end - start))


def image_coordinates_with_safe_buffer(coordinates):
    coordinates = list(coordinates)
    coordinates[0] -= config.IMAGE_SAFE_BUFFOR
    coordinates[1] -= config.IMAGE_SAFE_BUFFOR
    coordinates[2] += config.IMAGE_SAFE_BUFFOR * 2
    coordinates[3] += config.IMAGE_SAFE_BUFFOR * 2
    coordinates = tuple(coordinates)
    return coordinates


def dispatcher_for_resources_coordinates(n):
    if n == 0:
        return screen.locate_image_on_full_screen(images.BLANK_LIGHT)
    if n == 1:
        return screen.locate_image_on_full_screen(images.BLANK_DARK)
    if n == 2:
        return screen.locate_image_on_full_screen(images.FULL_LIGHT)
    if n == 3:
        return screen.locate_image_on_full_screen(images.FULL_DARK)


def ResourceImage():
    if config.GET_EXECUTION_TIME_INFO is True:
        start = time.time()
    screen.full_screen_screen_shoot()
    pool = mp.Pool(processes=4)
    v = pool.map(dispatcher_for_resources_coordinates, range(4))
    pool.close()
    pool.join()

    resourceBlankLightTemp = v[0]
    resourceBlankDarkTemp = v[1]
    resourceFullLightTemp = v[2]
    resourceFullDarkTemp = v[3]

    checkNumber1 = check_if_none(resourceBlankLightTemp)
    checkNumber2 = check_if_none(resourceBlankDarkTemp)
    checkNumber3 = check_if_none(resourceFullLightTemp)
    checkNumber4 = check_if_none(resourceFullDarkTemp)

    resourceMinimum = min(checkNumber1, checkNumber2, checkNumber3, checkNumber4)

    if resourceMinimum == checkNumber1:
        config.resource_icon_coordinates = image_coordinates_with_safe_buffer(resourceBlankLightTemp)
    elif resourceMinimum == checkNumber2:
        config.resource_icon_coordinates = image_coordinates_with_safe_buffer(resourceBlankDarkTemp)
    elif resourceMinimum == checkNumber3:
        config.resource_icon_coordinates = image_coordinates_with_safe_buffer(resourceFullLightTemp)
    elif resourceMinimum == checkNumber4:
        config.resource_icon_coordinates = image_coordinates_with_safe_buffer(resourceFullDarkTemp)

    if config.GET_EXECUTION_TIME_INFO is True:
        end5 = time.time()
        print('getting resource icon in: {} '.format(end5 - start))


def check_if_none(value):
    if value is None:
        result = 2000
    else:
        result = value[1]

    return result
