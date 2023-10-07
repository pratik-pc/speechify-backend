from flask import Flask
from src.routes.transcribe_routes import Transcription
from src.routes.translation_routes import Translation
from src.config import Config

app = Flask(__name__)
app.config.from_object(Config)


app.add_url_rule('/api/transcribe', view_func=Transcription.as_view('transcribe'))
app.add_url_rule('/api/translate', view_func=Translation.as_view('translate'))