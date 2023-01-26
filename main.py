import gensim
from gensim.models import Word2Vec

BANNED_CHARACTERS = "\"!@#$%^&.`*()-+?_=,<>/123456789\'"
EMPTY_WORD = "___________"

model = gensim.models.KeyedVectors.load_word2vec_format('venv/data/GoogleNews-vectors-negative300.bin', binary=True)

sim_list = model.most_similar(positive="chelsea")

print(sim_list)