from strip import Strip
from time import sleep
from animation import Animation
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class FadeColorsAnimation(Animation):
  def init(self):
    pass

  def run(self):
    n = 300
    
    while self.is_running:
      range_colors = ['#FF0000', '#00FF00', '#0000FF']
      nb_colors = len(range_colors)

      for i in range(len(range_colors)):
        color_from = range_colors[i]
        color_to= range_colors[i + 1 if i < nb_colors - 1 else 0]

        for x in range(n + 1):
          # see https://stackoverflow.com/a/50784012/1343257
          color_from = np.array(mpl.colors.to_rgb(color_from))
          color_to = np.array(mpl.colors.to_rgb(color_to))
          color = mpl.colors.to_hex((1 - x / n) * color_from + x / n * color_to)

          color_int_16 = int('0x' + color[1:], 16)

          self.leds.fill(color_int_16)
          self.leds.show()
          sleep(0.4)

EXPORT = {
  'label': 'Fade Colors',
  'class': FadeColorsAnimation,
}
