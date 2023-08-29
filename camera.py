import pygame
import pygame.image
import pygame.transform
import os
import io


from time import sleep

from touchypi.const import RUNNING_ON_PI

from requests import request

import json
import cv2

with open('secrets.json') as fp:
    secrets = json.load(fp)

URL = f'rtsp://{secrets["username"]}:{secrets["password"]}@{secrets["ip"]}/stream2'

if RUNNING_ON_PI:
    print("Pi detected, setting display out to framebuffer")
    os.environ['SDL_FBDEV'] = '/dev/fb1'


if __name__ == '__main__':
    pygame.init()
    lcd = pygame.display.set_mode((240, 320))
    lcd.fill((0,0,0))
    # r = request('GET', URL)
    # img = io.BytesIO(r.content)
    # print(r.status_code)
    cap = cv2.VideoCapture(URL)
    ret, frame = cap.read()
    image_surface = pygame.image.frombuffer(frame.tostring(), frame.shape[1::-1], 'BGR')
    image_surface = pygame.transform.scale(image_surface, (200, 113))
    lcd.blit(image_surface, (20, 190))
    pygame.display.update()
    pygame.mouse.set_visible(False)
    pygame.display.update()
    sleep(10)