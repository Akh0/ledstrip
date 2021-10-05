from strip import Strip
from time import sleep
from animation import Animation

class RainbowAnimation(Animation):
  def init(self):
    self.leds.fill(0x000000)

  def wheel_color(self, pos):
    if pos < 85:
      return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
      pos -= 85
      return (255 - pos * 3, 0, pos * 3)
    else:
      pos -= 170
      return (0, pos * 3, 255 - pos * 3)

  def run(self):
    nb_leds = self.strip.nb_leds
    leds = self.strip.leds

    while self.is_running:
      for j in range(256): # one cycle of all 256 colors in the wheel
        for i in range(nb_leds):
            leds[i] = self.wheel_color(((i * 256 // nb_leds) + j) % 256)
        
        leds.show()
        sleep(0.01)
