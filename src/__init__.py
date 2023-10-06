from flask import Flask
from src.routes import Transcription

app = Flask(__name__)


app.add_url_rule('/api/transcribe', view_func=Transcription.as_view('transcribe'))