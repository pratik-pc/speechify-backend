import boto3
from flask import current_app
from src.aws_services.s3_service import S3_bucket

def transcribe(audio):
  s3 = S3_bucket()
  return s3.upload(audio)




class Transcribe:
  def __init__(self):
    self.transcribe_client = boto3.client(
      'transcribe',
      aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
      aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
      region_name=current_app.config['AWS_REGION']
    )
    self.bucket_name = current_app.config['S3_BUCKET_NAME']


  def transcribe_audio(self, audio):
    self.s3 = S3_bucket()
    filename = self.s3.upload(audio)
    self.transcription_response = self.transcribe_client.start_transcription_job(
      TranscriptionJobName='transcription-job',
      LanguageCode='hi-IN',
      MediaFormat='wav',
      Media={
        'MediaFileUri': f's3://{self.bucket_name}/{filename}'
      }
    )
    return "success"