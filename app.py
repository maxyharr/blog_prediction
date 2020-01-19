from flask import Flask, jsonify, request
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
import nltk
import os
nltk.download('gutenberg')
nltk.download('punkt')

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
  sample = gutenberg.raw('bible-kjv.txt')
  tok = sent_tokenize(sample)
  start = request.args.get('start', default = 0, type = int)
  end = request.args.get('end', default = 10, type = int)
  return jsonify(tok[start:end])

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=port)