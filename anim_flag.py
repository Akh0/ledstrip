from strip import Strip
from time import sleep
from animation import Animation

class FlagAnimation(Animation):
  def init(self):
    self.leds.fill(0x000000)

  def run(self):
    leds = self.leds
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
