from kafka import KafkaProducer
import os
from dotenv import load_dotenv

load_dotenv()

class kafkaProducer():
  def __init__(self):
    self.producer = KafkaProducer(bootstrap_servers=os.getenv('broker_ip'), value_serializer=lambda v: str(v).encode('utf-8'))
    self.topic = os.getenv('kafka_topic')

  def publish_message(self, text):
    self.producer.send(self.topic, value=text)