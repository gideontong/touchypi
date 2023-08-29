import pygame
import os

from time import sleep

from touchypi.const import RUNNING_ON_PI

if RUNNING_ON_PI:
    os.putenv('SDL_FBDEV', '/dev/fb1')

if __name__ == '__main__':
    pygame.init()
    pygame.mouse.set_visible(False)
    lcd = pygame.display.set_mode((240, 320))
    lcd.fill((255,0,0))
    pygame.display.update()
    sleep(5)

    lcd.fill((0,0,0))
    pygame.display.update()