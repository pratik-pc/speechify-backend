from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
  return ('<p>Speechify Backend</p>')


if __name__ == '__main__':
  app.run