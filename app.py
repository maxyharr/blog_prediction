from flask import Flask, jsonify, request
from nltk.corpus import gutenberg, wordnet
from nltk.tokenize import sent_tokenize
import nltk
import os

nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('wordnet')

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  print(app.url_map)
  return jsonify(['/bible', '/wordnet'])

@app.route('/bible', methods=['GET'])
def bible():
  sample = gutenberg.raw('bible-kjv.txt')
  tok = sent_tokenize(sample)
  start = request.args.get('start', default = 0, type = int)
  end = request.args.get('end', default = 10, type = int)
  return jsonify(tok[start:end])

@app.route('/wordnet', methods=['GET'])
def synsets():
  syns = wordnet.synsets('program')
  return jsonify(map(lambda a: str(a), syns))

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=port)