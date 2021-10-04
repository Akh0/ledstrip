#! /usr/bin/env python

from strip import Strip, NB_LEDS
from time import sleep

strip = Strip()
leds = strip.leds

nb_leds_by_color = 7
colors = [0xff0000, 0xffffff, 0x0000ff]

color_index = 0

for c in range(0, NB_LEDS, nb_leds_by_color):
  next_color = colors[color_index]

  for i in range(c, c+nb_leds_by_color):
    leds[i] = colors[color_index]

  color_index = 0 if color_index == 2 else color_index + 1

try:
  while True:
    for i in range(0, NB_LEDS):
      index = i+1 if i < NB_LEDS-1 else 0
      leds[i] = leds[index]

    sleep(0.01)
    leds.show()
except KeyboardInterrupt:
  strip.off()

