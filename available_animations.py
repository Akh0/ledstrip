from anim_color_wheel import ColorWheelAnimation
from anim_flag import FlagAnimation
from anim_rainbow import RainbowAnimation
from anim_red_alarm import RedAlarmAnimation
from anim_split_snake import SplitSnakeAnimation
from anim_stroboscope import StroboscopeAnimation

AVAILABLE_ANIMATIONS = {
  'color_wheel': {
    'name': 'Color wheel',
    'construct': ColorWheelAnimation,
  },
  'flag': {
    'name': 'French Flag',
    'construct': FlagAnimation,
  },
  'rainbow': {
    'name': 'Rainbow',
    'construct': RainbowAnimation,
  },
   'red_alarm': {
    'name': 'Red Alarm',
    'construct': RedAlarmAnimation,
  },
   'split_snake': {
    'name': 'Split Snake',
    'construct': SplitSnakeAnimation,
  },
   'stroboscope': {
    'name': 'Stroboscope',
    'construct': StroboscopeAnimation,
  },
}