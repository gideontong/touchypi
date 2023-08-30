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

# URL = f'rtsp://{secrets["username"]}:{secrets["password"]}@{secrets["ip"]}/stream2'
URL = f'rtsp://localhost/fpv.mkv'

if RUNNING_ON_PI:
    print("Pi detected, setting display out to framebuffer")
    os.environ['SDL_FBDEV'] = '/dev/fb1'


EMULATOR_SCALE = 3
RES = (240, 320)
TARGET_RES = RES
SCALE = 1
if not RUNNING_ON_PI:
    SCALE = EMULATOR_SCALE
    RES = tuple(SCALE * value for value in RES)

if __name__ == '__main__':
    pygame.init()
    lcd = pygame.display.set_mode(RES)
    cap = cv2.VideoCapture(URL)
    for i in range(300):
        buffer = pygame.Surface(TARGET_RES)
        buffer.fill((0,0,0))
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_surface = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], 'RGB')
        image_surface = pygame.transform.scale(image_surface, (200, 113))
        buffer.blit(image_surface, (20, 190))
        
        font = pygame.font.Font(None, 32)
        text_surface = font.render('WiFi Connected', True, (255, 255, 255))
        buffer.blit(text_surface, (20, 20))

        if not RUNNING_ON_PI:
            buffer = pygame.transform.scale_by(buffer, SCALE)
        lcd.blit(buffer, (0, 0))
        pygame.display.update()
        pygame.mouse.set_visible(False)
        pygame.display.update()
        # sleep(0.1)