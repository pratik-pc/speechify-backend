from flask import request
from flask.views import MethodView
from src.aws_services.transcription_service import Transcribe

class Transcription(MethodView):
  def post(self):
    audio_file = request.files.get('audio')
    language = request.form.get('language')
    if not audio_file:
      return "Error Audio file is missing"
    if audio_file:
      transcribe = Transcribe()
      transcribe.transcribe_audio(audio_file, language)
      status = transcribe.transcribe_waiter()
      if status == "COMPLETED":
        text = transcribe.transcription_text()
      return text