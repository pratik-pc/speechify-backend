import boto3
from flask import current_app


class Translate:
  def __init__(self):
    self.translate_client = boto3.client(
      'translate',
      aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
      aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
      region_name=current_app.config['AWS_REGION']
    )


  def translate_text(self, text):
    translation_response = self.translate_client.translate_text(
      Text=text,
      SourceLanguageCode='hi',
      TargetLanguageCode='en'
    )
    return translation_response