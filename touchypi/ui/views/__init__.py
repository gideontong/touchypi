import pygame

from typing import Tuple

SIZE = 24

signal_low = pygame.image.load('icons/signal-low.png')

def status_bar(draw_res: Tuple[int, int]) -> pygame.Surface:
    width, height = draw_res
    
    buffer = pygame.Surface((width, SIZE))

    buffer.fill((0, 0, 0))
    pygame.draw.line(buffer, (255, 255, 255), (0, SIZE - 1), (width, SIZE - 1))
    buffer.blit(signal_low, (2, 1))

    return buffer
