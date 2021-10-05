#! /usr/bin/env python

import sys
import argparse
from strip import Strip
from available_animations import AVAILABLE_ANIMATIONS

parser = argparse.ArgumentParser(description='Control LED Strip')
parser.add_argument('-c', '--color', dest='color', help='Hexadecimal color value (eg: FF0000)')
parser.add_argument('-b', '--brightness', dest='brightness', help='Brightness value between 0 and 100')
parser.add_argument('-a', '--animation', dest='animation', help='Run an animation : ' + ', '.join(AVAILABLE_ANIMATIONS.keys()))
parser.add_argument('--off', dest='off', action='store_true', help='Turn off the LED Strip')

if len(sys.argv) == 1:
  parser.print_help(sys.stderr)
  sys.exit(1)

args = parser.parse_args()

strip = Strip()

if args.off:
  strip.off()

###
### Color and Brightness
###
if args.brightness and not args.color and not args.animation:
  sys.exit('-b, --brightness must be set with --color or --animation argument')

if args.color:
  color = int('0x' + args.color, 16)

  if color < 0x000000 or color > 0xffffff:
    sys.exit('-c, --color must be an hexadecimal value between 000000 and FFFFFF')

  strip.leds.fill(color)

if args.brightness:
  try:
    brightness = float(args.brightness) / 100

    if brightness < 0 or brightness > 1:
      raise Exception()

    strip.leds.brightness = brightness
  except:
      sys.exit('-b, --brightness must be a number between 0 and 100')

strip.leds.show()

###
### Animation
###
if args.animation:
  if args.animation not in AVAILABLE_ANIMATIONS:
        sys.exit(args.animation + ' animation not available :-(\n\nChoose between ' + ', '.join(AVAILABLE_ANIMATIONS.keys()))

  AVAILABLE_ANIMATIONS[args.animation]['construct'](strip).start()
