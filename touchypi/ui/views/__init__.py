import pygame

from typing import Tuple

SIZE = 24

font = pygame.font.Font('fonts/grand9k.ttf', 18)
signal_low = pygame.image.load('icons/signal-low.png')

def status_bar(draw_res: Tuple[int, int]) -> pygame.Surface:
    width, height = draw_res
    
    buffer = pygame.Surface((width, SIZE))

    buffer.fill((0, 0, 0))
    pygame.draw.line(buffer, (255, 255, 255), (0, SIZE - 1), (width, SIZE - 1))
    buffer.blit(signal_low, (2, 1))

    text_surface = font.render("GidHub IoT", True, (255, 255, 255))
    buffer.blit(text_surface, (36, -3))

    return buffer
