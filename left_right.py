#! /usr/bin/env python

from strip import Strip
from time import sleep

strip = Strip()
leds = strip.leds

left_leds = range(59,70)
right_leds = range(0,11)

for r in right_leds:
  leds[r] = 0xff0000

for l in left_leds:
  leds[l] = 0x0000ff

print(leds)
leds.show()
