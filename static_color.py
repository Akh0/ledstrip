#! /usr/bin/env python

import sys
from strip import Strip

def error(message, showUsage = False):
  print(message)

  if showUsage:
    print("\n\nUsage: ./static_color hexa_color [brightness 0-100]\n\nExample: ./static_color ff0000 80")

  sys.exit()

# Program

argc = len(sys.argv)

if argc < 2:
  error("Missing argument", true)

color = int('0x' + sys.argv[1], 16)

if color < 0x000000 or color > 0xffffff:
  error("Invalid argument: color must be an hexadecimal value between 000000 and FFFFFF")

try:
  brightness = 1 if argc == 2 else float(sys.argv[2]) / 100
except:
    error("Invalid argument: brightness must be a number between 0 and 100")

if brightness < 0 or brightness > 1:
  error("Invalid argument: brightness must be between 0 and 100")

Strip(brightness, color)