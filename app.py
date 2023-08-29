import pygame
import pygame.image
import pygame.transform
import os
import io


from time import sleep

from touchypi.const import RUNNING_ON_PI

from requests import request

URL = 'https://www.kcscout.net/TransSuite.VCS.CameraSnapshots/K070WBC-01.jpg'

if RUNNING_ON_PI:
    print("Running on pi")
    os.environ['SDL_FBDEV'] = '/dev/fb1'

pygame.init()
print(pygame.display.Info())

if __name__ == '__main__':
    pygame.mouse.set_visible(False)
    lcd = pygame.display.set_mode((240, 320))
    lcd.fill((0,0,0))
    r = request('GET', URL)
    img = io.BytesIO(r.content)
    print(r.status_code)
    image_surface = pygame.image.load(img)
    image_surface = pygame.transform.scale(image_surface, (200, 113))
    lcd.blit(image_surface, (20, 190))
    pygame.display.update()
    sleep(10)