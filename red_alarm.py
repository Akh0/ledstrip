#! /usr/bin/env python

from strip import Strip
from time import sleep

strip = Strip(0, 0xff0000)
leds = strip.leds

brightness = 0
blink_velocity = 0.1
is_increasing_brighness = True

try:
  while True:
    if brightness >= 1:
      is_increasing_brighness = False
      sleep(0.3)
    elif brightness <= 0:
      is_increasing_brighness = True
      sleep(0.1)

    brightness = brightness + blink_velocity if is_increasing_brighness else brightness - blink_velocity

    leds.brightness = brightness
    leds.show()
    sleep(0.01)
except KeyboardInterrupt:
  strip.off()