import boto3
import time
import requests
import datetime
from flask import current_app
from src.aws_services.s3_service import S3_bucket


class Transcribe:
  def __init__(self):
    self.transcribe_client = boto3.client(
      'transcribe',
      aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
      aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
      region_name=current_app.config['AWS_REGION']
    )
    self.bucket_name = current_app.config['S3_BUCKET_NAME']
    self.transcription_response = None
    self.transcription_job_name = 'speechify-job-'+ datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S%z") # generate unique job name for aws transcribe

  def transcribe_audio(self, audio, lang):
    self.s3 = S3_bucket()
    filename = self.s3.upload(audio)
    self.transcription_response = self.transcribe_client.start_transcription_job(
      TranscriptionJobName= self.transcription_job_name,
      LanguageCode=lang,
      MediaFormat='wav',
      Media={
        'MediaFileUri': f's3://{self.bucket_name}/{filename}'
      }
    )

  def transcription_text(self):
    transcription_uri = self.transcription_response['TranscriptionJob']['Transcript']['TranscriptFileUri']
    transcription_text = requests.get(transcription_uri).json()['results']['transcripts'][0]['transcript']
    return transcription_text
  

  def transcribe_waiter(self):
    while True:
      response = self.transcribe_client.get_transcription_job(
        TranscriptionJobName= self.transcription_job_name
      )

      status = response['TranscriptionJob']['TranscriptionJobStatus']

      if status in ['COMPLETED', 'FAILED']:
        self.transcription_response = response
        return status

      time.sleep(2)