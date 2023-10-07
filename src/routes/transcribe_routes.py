from flask.views import MethodView

class Transcription(MethodView):
  def get(self):
    return "Transcription route"