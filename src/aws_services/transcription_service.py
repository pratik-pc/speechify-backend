from src.aws_services.s3_service import S3_bucket

def transcribe(audio):
  s3 = S3_bucket()
  return s3.upload(audio)