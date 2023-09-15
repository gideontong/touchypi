import json
import os

import pygame
import pygame.image
import pygame.transform

from touchypi.const import EMULATOR_SCALE, RUNNING_ON_PI

import logging

log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

with open('secrets.json') as fp:
    secrets = json.load(fp)

URL = f'rtsp://{secrets["username"]}:{secrets["password"]}@{secrets["ip"]}/stream2'
# URL = f'rtsp://localhost/fpv.mkv'

if RUNNING_ON_PI:
    logger.info("Pi detected, setting display out to framebuffer")
    os.environ['SDL_FBDEV'] = '/dev/fb1'


RES = (240, 320)
TARGET_RES = RES
SCALE = 1
if not RUNNING_ON_PI:
    SCALE = EMULATOR_SCALE
    RES = tuple(SCALE * value for value in RES)

if __name__ == '__main__':
    pygame.init()
    lcd = pygame.display.set_mode(RES)
    for i in range(10000):
        events = pygame.event.get()
        buffer = pygame.Surface(TARGET_RES)
        buffer.fill((0,0,0))
        
        font = pygame.font.Font(None, 32)
        text_surface = font.render(str(i), True, (255, 255, 255))
        buffer.blit(text_surface, (20, 20))

        if not RUNNING_ON_PI:
            buffer = pygame.transform.scale_by(buffer, SCALE)
        lcd.blit(buffer, (0, 0))
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                logger.debug(event)
        pygame.display.update()
        if RUNNING_ON_PI:
            pygame.mouse.set_visible(False)
            pygame.display.update()