import inputDevices
import images
import time
import multiprocessing as mp
import config
import keyboardConfig


def sendAttack():
    previousPosition = 100
    inputDevices.click_image(images.AF_ICON)
    time.sleep(config.DELAY_FOR_LOAD)
    inputDevices.key_press(keyboardConfig.HIDING_AF_ICONS)
    getRegion.AFImages()
    for i in range(0, config.ATTACKS_PER_1_WILLAGE):

        if config.GET_TIME_FOR_1_ATTACK == 1:
            start = time.time()

        x = randomDelayBetweenAttacks()
        time.sleep(x)
        '''Resources 0-fullLight, 1-fullDark, 2-blankLight,
         3-blankDark'''
        resources = checkResources()
        if (resources == 0):
            if (previousPosition == 0):
                mouse.LeftClick()
                if config.GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}'.format(end - start))
            else:
                mouse.MovementToALight()
                mouse.LeftClick()
                previousPosition = 0
                if config.GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}'.format(end - start))
        if (resources == 1):
            if (previousPosition == 0):
                mouse.LeftClick()
                if config.GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}'.format(end - start))
            else:
                mouse.MovementToADark()
                mouse.LeftClick()
                previousPosition = 0
                if config.GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}'.format(end - start))
        if (resources == 2):
            if (previousPosition == 1):
                mouse.LeftClick()
                if config.GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}'.format(end - start))
            else:
                mouse.MovementToBLight()
                mouse.LeftClick()
                previousPosition = 1
                if config.GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}'.format(end - start))
        if (resources == 3):
            if (previousPosition == 1):
                mouse.LeftClick()
                if config.GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}'.format(end - start))
            else:
                mouse.MovementToBDark()
                mouse.LeftClick()
                previousPosition = 1
                if config.GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}'.format(end - start))


def dispatcherForCheckResources(n):
    if n == 0:
        return iconPosition.blankLightResources()
    if n == 1:
        return iconPosition.blankDarkResources()
    if n == 2:
        return iconPosition.fullLightResources()
    if n == 3:
        return iconPosition.fullDarkResources()


'''Resources 0-fullLight, 1-fullDark, 2-blankLight, 3-blankDark'''


def checkResources():
    if config.GET_EXECUTION_TIME_INFO == 1:
        start = time.time()

    pool = mp.Pool(processes=4)
    v = pool.map(dispatcherForCheckResources, range(4))

    pool.close()
    pool.join()

    blankLight = v[0]
    blankDark = v[1]
    fullLight = v[2]
    fullDark = v[3]

    if ((blankLight == None) and (blankDark == None)
            and (fullLight == None) and (fullDark == None)):
        end = time.time()
        if config.GET_EXECUTION_TIME_INFO == 1:
            end = time.time()
            print('None checking resources in: {} '.format(end - start))
        return None

    if (blankLight == None):
        BL = 2000
    else:
        BL = blankLight[1]

    if (blankDark == None):
        BD = 2000
    else:
        BD = blankDark[1]

    if (fullLight == None):
        FL = 2000
    else:
        FL = fullLight[1]

    if (fullDark == None):
        FD = 2000
    else:
        FD = fullDark[1]

    minimum = min(BL, BD, FL, FD)

    if (minimum == FL):
        if config.GET_EXECUTION_TIME_INFO == 1:
            end = time.time()
            print('checking resources in: {} '.format(end - start))
        return 0
    elif (minimum == FD):
        if config.GET_EXECUTION_TIME_INFO == 1:
            end = time.time()
            print('checking resources in: {} '.format(end - start))
        return 1
    elif (minimum == BL):
        if config.GET_EXECUTION_TIME_INFO == 1:
            end = time.time()
            print('checking resources in: {} '.format(end - start))
        return 2
    elif (minimum == BD):
        if config.GET_EXECUTION_TIME_INFO == 1:
            end = time.time()
            print('checking resources in: {} '.format(end - start))
        return 3


def randomDelayBetweenAttacks():
    x = random.randint(config.LOW_DELAY, config.HIGH_DELAY)
    return (x / 1000)