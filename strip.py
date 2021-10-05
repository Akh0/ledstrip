import board
import adafruit_ws2801

O_CLOCK = board.SCK
O_DATA = board.MOSI
NB_LEDS = 70

class Strip:
  def __init__(self, default_brightness=1, default_color=None, auto_write=False):
    self.leds = adafruit_ws2801.WS2801(O_CLOCK, O_DATA, NB_LEDS, brightness=default_brightness, auto_write=auto_write)
    self.nb_leds = NB_LEDS

    if default_color:
      self.leds.fill(default_color)
      self.leds.show()

  def off(self):
    self.leds.fill(0x000000)
    self.leds.brightness = 0
    self.leds.show()