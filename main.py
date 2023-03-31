import gensim
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import warnings
import gensim.downloader as api
from flask import *
import json
import io

# model = gensim.models.KeyedVectors.load_word2vec_format('venv/data/wiki-news-300d-1M.vec')

# model = gensim.models.KeyedVectors.load_word2vec_format('venv/data/wiki-news-300d-1M.vec', encoding='unicode_escape')

model = gensim.models.KeyedVectors.load_word2vec_format('venv/data/GoogleNews-vectors-negative300.bin', binary=True)

# corpus = api.load('fasttext-wiki-news-subwords-300')
# model = Word2Vec.load(corpus)

app = Flask(__name__)


@app.route('/request/', methods=['GET'])
def request_page():
    words_query = str(request.args.get('user_words')) # localhost:7777/request?user_words=word1,word2,word3
    word_list = words_query.split(',')

    sim_list = model.most_similar(positive=word_list, topn=250000)

    json_dump = json.dumps(sim_list)

    return json_dump


app.run(port=7777)
