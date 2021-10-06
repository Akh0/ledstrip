from strip import Strip
from time import sleep
from animation import Animation

class ColorWheelAnimation(Animation):
  def init(self):
    self.leds.fill(0x000000)

  def run(self):
    leds = self.leds
    nb_leds = self.nb_leds

    nb_leds_by_color = 7
    colors = [0xff0000, 0xffffff, 0x0000ff]

    color_index = 0

    for c in range(0, nb_leds, nb_leds_by_color):
      next_color = colors[color_index]

      for i in range(c, c+nb_leds_by_color):
        leds[i] = colors[color_index]

      color_index = 0 if color_index == 2 else color_index + 1

    while self.is_running:
      for i in range(0, nb_leds):
        index = i+1 if i < nb_leds-1 else 0
        leds[i] = leds[index]

      sleep(0.01)
      leds.show()

EXPORT = {
  'label': 'Color Wheel',
  'class': ColorWheelAnimation,
}
