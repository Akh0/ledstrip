from threading import Thread
from animation import Animation

class AnimationThread(Thread):
  def set_animation(self, animation: Animation):
    if self.is_alive():
      raise Exception('Thread must be stopped before setting an animation')
  
    self.current_animation = animation

  def run(self):
    if not hasattr(self, 'current_animation'):
      raise Exception('An animation must be set before running the thread')

    self.current_animation.start()

  def stop(self):
    self.current_animation.stop()