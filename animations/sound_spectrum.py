from strip import Strip
from time import sleep
from animation import Animation

class SoundSpectrumAnimation(Animation):
  def init(self):
    self.leds.fill(0x000000)

  def run(self):
    import sounddevice as sd
    import numpy as np

    leds = self.leds
    nb_leds = self.nb_leds

    low_color = 0x1c0822
    medium_color = 0x4d175e
    high_color = 0x972eb8
    max_color = 0xc30eff

    def get_level_color(level):
      if level < 0.60:
        return low_color
      elif level < 0.70:
        return medium_color
      elif level < 0.80:
        return high_color
      else:
        return max_color

    def audio_callback(indata, frames, time, status):
      volume = int(np.linalg.norm(indata) * 80)
      max_volume_leds = min(volume, nb_leds) // 2
      half_nb_leds = nb_leds // 2

      leds.fill(0x000000)
    
      for i in range(half_nb_leds, half_nb_leds + max_volume_leds):
        self.leds[i] = get_level_color(i / nb_leds)
        
      for i in range(half_nb_leds-1, half_nb_leds - max_volume_leds, -1):
        self.leds[i] = get_level_color(1 - i / nb_leds)

      self.leds.show()

      sleep(0.01)

    stream = sd.InputStream(callback=audio_callback)

    with stream:
      while self.is_running:
        sleep(0.1) # allow thread stop every 0.1 seconds

EXPORT = {
  'label': 'Sound Spectrum',
  'class': SoundSpectrumAnimation,
}
