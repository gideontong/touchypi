import os

import pygame
import pygame.image
import pygame.transform

pygame.init()

from touchypi.const import EMULATOR_SCALE, PI_RES, RUNNING_ON_PI
from touchypi.tools import logger
from touchypi.ui.views import status_bar

if RUNNING_ON_PI:
    logger.info("Pi detected, setting display out to framebuffer")
    os.environ["SDL_FBDEV"] = "/dev/fb1"


TARGET_RES = PI_RES
SCALE = 1
if not RUNNING_ON_PI:
    SCALE = EMULATOR_SCALE
    TARGET_RES = tuple(SCALE * value for value in PI_RES)

if __name__ == "__main__":
    lcd = pygame.display.set_mode(TARGET_RES)
    for i in range(10000):
        events = pygame.event.get()
        buffer = pygame.Surface(TARGET_RES)
        buffer.fill((0, 0, 0))

        font = pygame.font.Font(None, 32)
        text_surface = font.render(str(i), True, (255, 255, 255))
        buffer.blit(text_surface, (20, 40))

        if not RUNNING_ON_PI:
            buffer = pygame.transform.scale_by(buffer, SCALE)
        lcd.blit(buffer, (0, 0))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                logger.debug(event)

        status_bar_buffer = status_bar(PI_RES)
        if not RUNNING_ON_PI:
            status_bar_buffer = pygame.transform.scale_by(status_bar_buffer, SCALE)
        lcd.blit(status_bar_buffer, (0, 0))
        pygame.display.update()
        if RUNNING_ON_PI:
            pygame.mouse.set_visible(False)
            pygame.display.update()
