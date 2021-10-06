from animations.color_wheel import ColorWheelAnimation
from animations.flag import FlagAnimation
from animations.rainbow import RainbowAnimation
# from animations.red_alarm import RedAlarmAnimation
from animations.split_snake import SplitSnakeAnimation
from animations.stroboscope import StroboscopeAnimation

import glob
import importlib
from os.path import dirname, basename, isfile, join

animation_files = glob.glob(join(dirname(__file__)+ '/animations', '*.py'))
animation_module_names = [ basename(f)[:-3] for f in animation_files if isfile(f) and not f.endswith('__init__.py') ]

AVAILABLE_ANIMATIONS = {}

for module_name in animation_module_names:
  module = importlib.import_module('animations.' + module_name)
  AVAILABLE_ANIMATIONS[module_name] = { 'name': module.EXPORT['label'], 'construct': module.EXPORT['class'] }
