# Touchscreen Driver
# Top Left - (240, 320)
# Top Right - (0, 320)
# Bottom Left - (240, 0)
# Bottom Right - (0, 0)
# 40x40 square is good for touchscreen event

import time

from typing import Union

from touchypi.events.constants import DELAY_ALLOWED_NS

last_click = None
last_click_time = time.time_ns()

def touch_cycle_clock() -> Union[None, tuple]:
    if time.time_ns() - last_click_time < DELAY_ALLOWED_NS:
        return last_click