from flask import Flask,request,jsonify
from readmdict import MDX
from bs4 import BeautifulSoup
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

filename = "OxfordAdvancedDictionary(10thEdition)V3.mdx"
headwords = [*MDX(filename)]  # 单词名列表
items = [*MDX(filename).items()]  # 释义html源码列表

def lookup_phon_us(word):
    word = word.strip().lower()
    wordIndex = headwords.index(word.encode())
    word, html = items[wordIndex]
    word, html = word.decode(), html.decode()

    soup = BeautifulSoup(html, "html.parser")
    phon_us = soup.find(class_='top-container').find(class_='phons_n_am').find(class_='phon')

    assert phon_us is not None, "No phonetic symbol found"
    return phon_us.text[1:-1]

# Path: /api/dict/phon_us?q=<word>
# Example: /api/dict/phon_us?q=word
@app.route("/api/dict/phon_us")
def dict_phon_us():
    word = request.args.get('q')
    phon_us = lookup_phon_us(word)
    return jsonify({"phon_us": phon_us})