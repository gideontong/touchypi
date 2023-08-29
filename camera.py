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
    cap = cv2.VideoCapture(URL)
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_surface = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], 'RGB')
    image_surface = pygame.transform.scale(image_surface, (200, 113))
    lcd.blit(image_surface, (20, 190))
    
    font = pygame.font.Font(None, 32)
    text_surface = font.render('WiFi Connected', True, (255, 255, 255))
    lcd.blit(text_surface, (20, 20))

    pygame.display.update()
    pygame.mouse.set_visible(False)
    pygame.display.update()
    sleep(10)