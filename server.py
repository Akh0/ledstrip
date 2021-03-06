#! /usr/bin/env python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
from strip import Strip
from config import config
from animation_thread import AnimationThread
from available_animations import AVAILABLE_ANIMATIONS

class StripHandler:
  def __init__(self):
    self.animation_thread = None

  def check_payload(self, payload):
    if 'animation' in payload and payload['animation'] is not None:
      if payload['animation'] not in AVAILABLE_ANIMATIONS:
        return False
      
    # TODO: check color and brightness
    return True

  def stop_animation_thread(self):
    if self.animation_thread and self.animation_thread.is_alive():
      self.animation_thread.stop()

  def update_strip(self, payload):
    self.stop_animation_thread()

    strip = Strip()

    has_brightness = 'brightness' in payload and payload['brightness'] is not None
    has_color = 'color' in payload and payload['color'] is not None
    has_animation = 'animation' in payload and payload['animation'] is not None

    if has_brightness or has_color:
      if has_brightness:
        strip.leds.brightness = payload['brightness'] / 100
      
      if has_color and not has_animation:
        strip.leds.fill(int('0x' + payload['color'], 16))

      strip.leds.show()

    if has_animation:
      self.animation_thread = AnimationThread()
      animation = AVAILABLE_ANIMATIONS[payload['animation']]['construct'](strip)
      self.animation_thread.set_animation(animation)
      self.animation_thread.start()

# Strip handle need to be initialized globally to keep an unique thread
strip_handler = StripHandler()

class HTTPRequestHandler(BaseHTTPRequestHandler):
  def _set_headers(self, status_code = 200):
    self.send_response(status_code)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

  ###
  ### GET Requests
  ###
  def do_GET(self):
    if self.path == '/animations':
      self._set_headers()

      response = {}
      for key in AVAILABLE_ANIMATIONS:
        response[key] = AVAILABLE_ANIMATIONS[key]["name"]
      
      self.wfile.write(json.dumps(response).encode('utf-8'))

  ###
  ### POST Requests
  ###
  def do_POST(self):
    if self.path == '/set':
      ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

      # Refuse to receive non-json content
      if ctype != 'application/json':
        self.send_response(400)
        self.end_headers()
        return

      # Read and convert payload to dictionary
      length = int(self.headers.get('content-length'))
      payload = json.loads(self.rfile.read(length))

      if strip_handler.check_payload(payload):
        self._set_headers()
        response = {"status": "ok", "code": 200}
        strip_handler.update_strip(payload)
      else:
        self._set_headers(400)
        response = {"status": "Bad Request", "code": 400}
    else:
      self._set_headers(403)
      response = {"status": "Bad Request", "code": 403}

    # send the message back
    self.wfile.write(json.dumps(response).encode('utf-8'))

port = config['server']['port']
server = HTTPServer(('', port), HTTPRequestHandler)
print('Server running on port %s' % port)

try:
  server.serve_forever()
except:
  print("\n\nClosing server...")
  strip_handler.stop_animation_thread()
  server.shutdown()