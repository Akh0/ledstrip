#! /usr/bin/env python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
from strip import Strip
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
      self.animation_thread.join()

  def update_strip(self, payload):
      self.stop_animation_thread()
    
      if 'animation' in payload and payload['animation'] is not None:
        self.animation_thread = AnimationThread()
        animation = AVAILABLE_ANIMATIONS[payload['animation']]['construct'](Strip())
        self.animation_thread.set_animation(animation)
        self.animation_thread.start()
      else:
        strip = Strip()
        strip.leds.fill(int('0x' + payload['color'], 16))
        strip.leds.brightness = payload['brightness'] / 100
        strip.leds.show()

strip_handler = StripHandler()

class HTTPRequestHandler(BaseHTTPRequestHandler):
  def __init__(self, *args):
    BaseHTTPRequestHandler.__init__(self, *args)

  def _set_headers(self, status_code = 200):
    self.send_response(status_code)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

  # POST Requests
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
        response = {"status": "nok", "code": 400}

      # send the message back
      self.wfile.write(json.dumps(response).encode('utf-8'))

PORT = 8888
server = HTTPServer(('', PORT), HTTPRequestHandler)
print('Server running on port %s' % PORT)

try:
  server.serve_forever()
except:
  print("\n\nClosing server...")
  strip_handler.stop_animation_thread()
  server.shutdown()