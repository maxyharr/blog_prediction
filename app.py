from flask import Flask, jsonify, request
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('gutenberg')
nltk.download('punkt')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
  sample = gutenberg.raw('bible-kjv.txt')
  tok = sent_tokenize(sample)
  start = request.args.get('start', default = 0, type = int)
  end = request.args.get('end', default = 10, type = int)
  return jsonify({'tok': tok[start:end]})

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000, debug=True)