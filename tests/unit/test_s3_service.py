import unittest
import boto3
from src.aws_services.s3_service import S3_bucket
from moto import mock_s3
from src.config import Config
from src import app
from io import BytesIO

class TestS3Service(unittest.TestCase):

  def setUp(self):
    self.app = app.test_client()


  @mock_s3
  def test_s3_upload(self):
    config = Config()
    s3_test_client = boto3.client('s3',
      aws_access_key_id=config.AWS_ACCESS_KEY_ID,
      aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
      region_name=config.AWS_REGION
    )
    s3_test_client.create_bucket(Bucket=config.S3_BUCKET_NAME)
    test_data = b'This is a test file content'
    fileobj = BytesIO(test_data)
    
    with app.app_context():
      s3_service = S3_bucket()
      s3_service.upload(fileobj)
    
    response = s3_test_client.get_object(Bucket=config.S3_BUCKET_NAME, Key='sample.wav')
    uploaded_data = response['Body'].read()

    self.assertEqual(uploaded_data, test_data)


if __name__ == '__main__':
  unittest.main()