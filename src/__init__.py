from flask import Flask
from src.routes import Transcription
from src.config import Config

app = Flask(__name__)
app.config.from_object(Config)


app.add_url_rule('/api/transcribe', view_func=Transcription.as_view('transcribe'))