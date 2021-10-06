from strip import Strip
from time import sleep
from animation import Animation

class RedAlarmAnimation(Animation):
  def init(self):
    self.strip.leds.fill(0xff0000)

  def run(self):
    leds = self.strip.leds

    brightness = 0
    blink_velocity = 0.1
    is_increasing_brighness = True

    while self.is_running:
      if brightness >= 1:
        is_increasing_brighness = False
        sleep(0.3)
      elif brightness <= 0:
        is_increasing_brighness = True
        sleep(0.1)

      brightness = brightness + blink_velocity if is_increasing_brighness else brightness - blink_velocity

      leds.brightness = brightness
      leds.show()
      sleep(0.01)

EXPORT = {
  'label': 'Red Alarm',
  'class': RedAlarmAnimation,
}
