from flask import request
from flask.views import MethodView
from src.aws_services.transcription_service import Transcribe
from src.aws_services.translation_service import Translate
from src.kafka.kafka_producer import kafkaProducer
import json

producer = kafkaProducer()

class Transcription(MethodView):
  def post(self):
    audio_file = request.files.get('audio')
    language = request.form.get('language')
    user_id = request.form.get('user_id')
    if not audio_file:
      return "Error Audio file is missing"
    if audio_file:
      transcribe = Transcribe()
      transcribe.transcribe_audio(audio_file, language)
      status = transcribe.transcribe_waiter()
      if status == "COMPLETED":
        text = transcribe.transcription_text()
        translate = Translate()
        translated_text = translate.translate_text(text, language)
        kafka_producer = producer.publish_message(json.dumps({"message": "translated_text", "user_id": user_id}))
      return "success"
    return "Error"