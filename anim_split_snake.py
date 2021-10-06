from strip import Strip
from time import sleep
from animation import Animation

class SplitSnakeAnimation(Animation):
  def init(self):
    self.half_nb_leds = int(self.nb_leds / 2)

  def center_to_sides(self, color, speed = 0.01):
    leds = self.leds

    for i in range(self.half_nb_leds, 0, -1):
      leds[i] = color
      leds[self.nb_leds-i-1] = color
      leds.show()
      sleep(speed)

  def sides_to_center(self, color, speed = 0.01):
    leds = self.leds
   
    for i in range(0, self.half_nb_leds):
      leds[i] = color
      leds[self.nb_leds-i-1] = color
      leds.show()
      sleep(speed)

  def run(self):
    self.leds.fill(0x000000)
    
    light = 0xffffff
    dark = 0x000000

    while self.is_running:
      self.center_to_sides(light)
      sleep(0.2)
      self.center_to_sides(dark)
      sleep(0.1)
      self.sides_to_center(light)
      self.sides_to_center(dark)
      sleep(0.2)
