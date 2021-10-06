from strip import Strip
from time import sleep
from animation import Animation

class StroboscopeAnimation(Animation):
  def init(self):
    self.leds.fill(0x000000)

  def color_leds(self, led_range, color):
    for l in led_range:
      self.leds[l] = color

  def run(self):
    leds = self.leds
    left_leds = range(59,70)
    center_leds = range(11,59)
    right_leds = range(0,11)

    left_color = 0xffffff
    right_color = 0xffffff
    center_color = 0xffffff

    off_color = 0x000000

    while self.is_running:
      for i in range(0,3):
        self.color_leds(left_leds, left_color)
        self.color_leds(right_leds, right_color)
        leds.show()
        sleep(0.1)
        self.color_leds(left_leds, off_color)
        self.color_leds(right_leds, off_color)
        leds.show()
        sleep(0.02)

      for i in range(0,3):
        self.color_leds(center_leds, center_color)
        leds.show()
        sleep(0.1)
        self.color_leds(center_leds, off_color)
        leds.show()
        sleep(0.02)

      for i in range(0,3):
        self.color_leds(left_leds, left_color)
        self.color_leds(right_leds, right_color)
        self.color_leds(center_leds, center_color)
        leds.show()
        sleep(0.1)
        self.color_leds(left_leds, off_color)
        self.color_leds(right_leds, off_color)
        self.color_leds(center_leds, off_color)
        leds.show()
        sleep(0.02)

EXPORT = {
  'label': 'Stroboscope',
  'class': StroboscopeAnimation,
}
