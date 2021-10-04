#! /usr/bin/env python

from strip import Strip, NB_LEDS
from time import sleep

strip = Strip(1, 0x000000)
leds = strip.leds

half_nb_leds = int(NB_LEDS / 2)

def center_to_sides(color, speed = 0.01):
  for i in range(half_nb_leds, 0, -1):
    leds[i] = color
    leds[NB_LEDS-i-1] = color
    leds.show()
    sleep(speed)

def sides_to_center(color, speed = 0.01):
  for i in range(0, half_nb_leds):
    leds[i] = color
    leds[NB_LEDS-i-1] = color
    leds.show()
    sleep(speed)

light = 0xffffff
dark = 0x000000

try:
  while True:
    center_to_sides(light)
    sleep(0.2)
    center_to_sides(dark)
    sleep(0.1)
    sides_to_center(light)
    sides_to_center(dark)
    sleep(0.2)

except KeyboardInterrupt:
  strip.off()