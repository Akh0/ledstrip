#! /usr/bin/env python

from strip import Strip

strip = Strip()
leds = strip.leds
leds.show()

blue_leds = range(48,70)
white_leds = range(22,48)
red_leds = range(0,22)

for i in blue_leds:
  leds[i] = 0x0000ff

for i in white_leds:
  leds[i] = 0xffffff

for i in red_leds:
  leds[i] = 0xff0000

leds.show()
