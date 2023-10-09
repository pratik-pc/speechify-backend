import boto3
from flask import current_app
from flask.cli import with_appcontext



class S3_bucket:
  def __init__(self):
    self.client = boto3.client(
        's3',
          aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
          aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
          region_name=current_app.config['AWS_REGION']
      )
    

  def upload(self, audio):
    self.client.upload_fileobj(
      audio,
      current_app.config['S3_BUCKET_NAME'],
      'sample.wav'
    )

    return "uploaded successfully"