from gtts import gTTS


class Voice:
  def save_to_file(self, text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save('src/discord/output.wav')