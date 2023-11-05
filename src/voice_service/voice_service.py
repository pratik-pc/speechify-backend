import pyttsx3


class Voice:
  def __init__(self):
    self.engine = pyttsx3.init()

  def synthesize(self, text):
    self.engine.say(text)
    self.engine.runAndWait()

  def save_to_file(self, text):
    self.engine.save_to_file(text, 'output.wav')
    self.engine.runAndWait()