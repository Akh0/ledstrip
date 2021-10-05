from abc import ABC, abstractmethod
from strip import Strip

class Animation(ABC):
  def __init__(self, strip: Strip):
    self.strip = strip
    self.is_running = False
    self.init()

  @abstractmethod
  def init():
    pass
  
  @abstractmethod
  def run():
    pass

  def start(self):
    self.is_running = True
    self.run()

  def stop(self):
    self.is_running = False
    self.strip.off()

  @property
  def leds(self):
    return self.strip.leds

  @property
  def nb_leds(self):
    return len(self.strip.leds)