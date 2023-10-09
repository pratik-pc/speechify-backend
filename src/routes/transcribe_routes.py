from flask import request
from flask.views import MethodView
from src.aws_services.transcription_service import Transcribe

class Transcription(MethodView):
  def post(self):
    audio_file = request.files.get('audio')
    if not audio_file:
      return "Error Audio file is missing"
    if audio_file:
      transcribe = Transcribe()
      return transcribe.transcribe_audio(audio_file)