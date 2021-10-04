#! /usr/bin/env python

from strip import Strip
from time import sleep

strip = Strip()
leds = strip.leds

def color_leds(led_range, color):
  for l in led_range:
    leds[l] = color


left_leds = range(59,70)
center_leds = range(11,59)
right_leds = range(0,11)

left_color = 0xFF0075
right_color = 0xFF0075
center_color = 0x77D970

while True:
  for i in range(0,3):
    color_leds(left_leds, left_color)
    color_leds(right_leds, right_color)
    leds.show()
    sleep(0.1)
    color_leds(left_leds, 0x000000)
    color_leds(right_leds, 0x000000)
    leds.show()
    sleep(0.02)

  for i in range(0,3):
    color_leds(center_leds, center_color)
    leds.show()
    sleep(0.1)
    color_leds(center_leds, 0x000000)
    leds.show()
    sleep(0.02)

  for i in range(0,3):
    color_leds(left_leds, left_color)
    color_leds(right_leds, right_color)
    color_leds(center_leds, center_color)
    leds.show()
    sleep(0.2)
    color_leds(left_leds, 0x000000)
    color_leds(right_leds, 0x000000)
    color_leds(center_leds, 0x000000)
    leds.show()
    sleep(0.04)
