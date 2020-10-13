from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/test', methods = ['POST'])
@cross_origin(supports_credentials=True)
def testSentence():
  text = request.get_json()
  print(text['message'])
  return jsonify(text)
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)

